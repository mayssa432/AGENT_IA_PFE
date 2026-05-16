const messagesDiv = document.getElementById("messages");
const userInput = document.getElementById("userInput");
const statsDiv = document.getElementById("stats");

function handleKeyPress(event) {
    if (event.key === "Enter") sendMessage();
}

function addMessage(content, role) {
    const msg = document.createElement("div");
    msg.classList.add("message", role);

    const avatar = document.createElement("div");
    avatar.classList.add("avatar");
    avatar.textContent = role === "user" ? "👤" : "🤖";

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.innerHTML = content.replace(/\n/g, "<br>");

    msg.appendChild(avatar);
    msg.appendChild(bubble);
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function addTyping() {
    const msg = document.createElement("div");
    msg.classList.add("message", "bot", "typing");
    msg.id = "typing";

    const avatar = document.createElement("div");
    avatar.classList.add("avatar");
    avatar.textContent = "🤖";

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.textContent = "⏳ En train de réfléchir...";

    msg.appendChild(avatar);
    msg.appendChild(bubble);
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById("typing");
    if (typing) typing.remove();
}

async function sendMessage() {
    const message = userInput.value.trim();
    const path = document.getElementById("projectPath").value.trim();

    if (!message) return;

    addMessage(message, "user");
    userInput.value = "";
    addTyping();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message, path })
        });

        const data = await response.json();
        removeTyping();
        addMessage(data.response || "❌ Pas de réponse.", "bot");

    } catch (error) {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

async function analyzeProject() {
    const path = document.getElementById("projectPath").value.trim();

    if (!path) {
        addMessage("⚠️ Veuillez entrer un chemin de projet.", "bot");
        return;
    }

    addMessage(`🔍 Analyse du projet : ${path}`, "user");
    addTyping();

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ path })
        });

        const data = await response.json();
        removeTyping();

        if (data.error) {
            addMessage(`❌ Erreur : ${data.error}`, "bot");
            return;
        }

        // Mise à jour des stats
        updateStats(data);

        const files = data.files_analyzed || 0;
        const total = data.total_issues || 0;
        const critical = data.critical || 0;

        addMessage(`✅ **Analyse terminée !**\n\n` +
            `📂 Fichiers analysés : **${files}**\n` +
            `⚠️ Problèmes détectés : **${total}**\n` +
            `🔴 Critiques : **${critical}**\n\n` +
            `Tapez **critiques** pour voir les problèmes urgents.`, "bot");

    } catch (error) {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

function updateStats(data) {
    statsDiv.innerHTML = `
        <strong>📊 Dernière analyse</strong><br><br>
        📂 Fichiers : <strong>${data.files_analyzed || 0}</strong><br>
        ⚠️ Problèmes : <strong>${data.total_issues || 0}</strong><br>
        🔴 Critiques : <strong>${data.critical || 0}</strong><br>
        🟠 Importants : <strong>${data.important || 0}</strong>
    `;
}

// Charger les snapshots DOM au démarrage
async function loadSnapshots() {
    try {
        const response = await fetch("/dom/snapshots");
        const data = await response.json();
        const select = document.getElementById("snapshotSelect");

        select.innerHTML = '<option value="">Choisir un snapshot...</option>';
        Object.keys(data.snapshots).forEach(snapshot => {
            const option = document.createElement("option");
            option.value = snapshot;
            option.textContent = snapshot;
            select.appendChild(option);
        });
    } catch (error) {
        console.error("Erreur chargement snapshots:", error);
    }
}

async function validateFile() {
    const fileInput = document.getElementById("javaFile");
    const snapshotSelect = document.getElementById("snapshotSelect");

    if (!fileInput.files[0]) {
        addMessage("⚠️ Veuillez sélectionner un fichier Java.", "bot");
        return;
    }

    if (!snapshotSelect.value) {
        addMessage("⚠️ Veuillez choisir un snapshot DOM.", "bot");
        return;
    }

    const formData = new FormData();
    formData.append("java_file", fileInput.files[0]);
    formData.append("snapshot_name", snapshotSelect.value);

    addMessage(`✅ Validation de ${fileInput.files[0].name} contre ${snapshotSelect.value}`, "user");
    addTyping();

    try {
        const response = await fetch("/validate", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        removeTyping();

        if (data.error) {
            addMessage(`❌ Erreur : ${data.error}`, "bot");
            return;
        }

        const issues = data.issues || [];
        addMessage(`✅ **Validation terminée !**\n\n` +
            `📄 Fichier : ${data.file}\n` +
            `📱 Snapshot : ${data.snapshot}\n` +
            `⚠️ Problèmes trouvés : **${data.issues_count}**\n\n` +
            (issues.length > 0 ? `Détails :\n${issues.map(i => `• ${i}`).join('\n')}` : "Aucun problème détecté !"), "bot");

    } catch (error) {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

async function fixFile() {
    const fileInput = document.getElementById("javaFile");
    const snapshotSelect = document.getElementById("snapshotSelect");

    if (!fileInput.files[0]) {
        addMessage("⚠️ Veuillez sélectionner un fichier Java.", "bot");
        return;
    }

    if (!snapshotSelect.value) {
        addMessage("⚠️ Veuillez choisir un snapshot DOM.", "bot");
        return;
    }

    const formData = new FormData();
    formData.append("java_file", fileInput.files[0]);
    formData.append("snapshot_name", snapshotSelect.value);

    addMessage(`🔧 Correction automatique de ${fileInput.files[0].name}`, "user");
    addTyping();

    try {
        const response = await fetch("/fix", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        removeTyping();

        if (data.error) {
            addMessage(`❌ Erreur : ${data.error}`, "bot");
            return;
        }

        const fixResult = data.fix_result || {};
        addMessage(`🔧 **Correction terminée !**\n\n` +
            `📄 Fichier : ${data.file}\n` +
            `📱 Snapshot : ${data.snapshot}\n` +
            `✅ Corrections appliquées : **${fixResult.corrections_applied || 0}**\n` +
            `💾 Sauvegarde créée : ${fixResult.backup_created ? 'Oui' : 'Non'}\n\n` +
            (fixResult.details ? `Détails :\n${fixResult.details.map(d => `• ${d}`).join('\n')}` : ""), "bot");

    } catch (error) {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

// Charger les snapshots au démarrage
window.onload = loadSnapshots;
