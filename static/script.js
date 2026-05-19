/* ===========================================================
   Agent IA Appium — PFE Dashboard v2.0
   script.js
   =========================================================== */

const messagesDiv = document.getElementById("messages");
const userInput   = document.getElementById("userInput");
const statsDiv    = document.getElementById("stats");

// ─── Utilitaires Chat ─────────────────────────────────────

function handleKeyPress(event) {
    if (event.key === "Enter") sendMessage();
}

function addMessage(content, role) {
    const msg    = document.createElement("div");
    msg.classList.add("message", role);
    const avatar = document.createElement("div");
    avatar.classList.add("avatar");
    avatar.textContent = role === "user" ? "👤" : "🤖";
    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.innerHTML = content.replace(/\n/g, "<br>").replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
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
    const t = document.getElementById("typing");
    if (t) t.remove();
}

// ─── Onglets ──────────────────────────────────────────────

function switchTab(name) {
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
    document.getElementById("tab-"   + name).classList.add("active");
    document.getElementById("panel-" + name).classList.add("active");
    // Chargement automatique
    if (name === "history") loadHistory();
    if (name === "metrics") loadMetrics();
}

// ─── TAB 1 — Chat ────────────────────────────────────────

async function sendMessage() {
    const message = userInput.value.trim();
    const path    = document.getElementById("projectPath").value.trim();
    if (!message) return;
    addMessage(message, "user");
    userInput.value = "";
    addTyping();
    try {
        const resp = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message, path }),
        });
        const data = await resp.json();
        removeTyping();
        addMessage(data.response || "❌ Pas de réponse.", "bot");
    } catch {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

async function analyzeProject() {
    const path = document.getElementById("projectPath").value.trim();
    if (!path) { addMessage("⚠️ Veuillez entrer un chemin de projet.", "bot"); return; }
    addMessage(`🔍 Analyse du projet : ${path}`, "user");
    addTyping();
    try {
        const resp = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ path }),
        });
        const data = await resp.json();
        removeTyping();
        if (data.error) { addMessage(`❌ Erreur : ${data.error}`, "bot"); return; }
        updateStats(data);
        addMessage(
            `✅ **Analyse terminée !**\n\n` +
            `📂 Fichiers analysés : **${data.files_analyzed || 0}**\n` +
            `⚠️ Problèmes détectés : **${data.total_issues || 0}**\n` +
            `🔴 Critiques : **${data.critical || 0}**\n\n` +
            `Tapez **critiques** pour voir les problèmes urgents.`, "bot");
    } catch {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

function updateStats(data) {
    statsDiv.innerHTML = `
        <strong style="color:#cba6f7">📊 Dernière analyse</strong><br><br>
        📂 Fichiers : <strong>${data.files_analyzed || 0}</strong><br>
        ⚠️ Problèmes : <strong>${data.total_issues || 0}</strong><br>
        🔴 Critiques : <strong>${data.critical || 0}</strong><br>
        🟠 Importants : <strong>${data.important || 0}</strong>
    `;
}

async function loadSnapshots() {
    try {
        const resp = await fetch("/dom/snapshots");
        const data = await resp.json();
        const sel  = document.getElementById("snapshotSelect");
        sel.innerHTML = '<option value="">Choisir un snapshot...</option>';
        Object.keys(data.snapshots || {}).forEach(snap => {
            const opt = document.createElement("option");
            opt.value = snap;
            opt.textContent = snap;
            sel.appendChild(opt);
        });
    } catch { /* silencieux au démarrage */ }

    // Ping status
    try {
        const s = await fetch("/status");
        const d = await s.json();
        const pill = document.getElementById("pill-status");
        if (d.status === "online") {
            pill.textContent = "● En ligne";
            pill.style.color = "#a6e3a1";
        }
        if (d.last_analysis) updateStats(d.last_analysis);
    } catch { /* silencieux */ }
}

async function validateFile() {
    const fi  = document.getElementById("javaFile");
    const sel = document.getElementById("snapshotSelect");
    if (!fi.files[0])  { addMessage("⚠️ Veuillez sélectionner un fichier Java.", "bot"); return; }
    if (!sel.value)    { addMessage("⚠️ Veuillez choisir un snapshot DOM.", "bot");    return; }
    const fd = new FormData();
    fd.append("java_file", fi.files[0]);
    fd.append("snapshot_name", sel.value);
    addMessage(`✅ Validation de ${fi.files[0].name} contre ${sel.value}`, "user");
    addTyping();
    try {
        const resp = await fetch("/validate", { method: "POST", body: fd });
        const data = await resp.json();
        removeTyping();
        if (data.error) { addMessage(`❌ Erreur : ${data.error}`, "bot"); return; }
        const issues = data.issues || [];
        addMessage(
            `✅ **Validation terminée !**\n\n` +
            `📄 Fichier : ${data.file}\n` +
            `📱 Snapshot : ${data.snapshot}\n` +
            `⚠️ Problèmes : **${data.issues_count}**\n\n` +
            (issues.length ? `Détails :\n${issues.map(i => `• ${i}`).join("\n")}` : "Aucun problème détecté !"),
            "bot"
        );
    } catch {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

async function fixFile() {
    const fi  = document.getElementById("javaFile");
    const sel = document.getElementById("snapshotSelect");
    if (!fi.files[0])  { addMessage("⚠️ Veuillez sélectionner un fichier Java.", "bot"); return; }
    if (!sel.value)    { addMessage("⚠️ Veuillez choisir un snapshot DOM.", "bot");    return; }
    const fd = new FormData();
    fd.append("java_file", fi.files[0]);
    fd.append("snapshot_name", sel.value);
    addMessage(`🔧 Correction automatique de ${fi.files[0].name}`, "user");
    addTyping();
    try {
        const resp = await fetch("/fix", { method: "POST", body: fd });
        const data = await resp.json();
        removeTyping();
        if (data.error) { addMessage(`❌ Erreur : ${data.error}`, "bot"); return; }
        const fx = data.fix_result || {};
        addMessage(
            `🔧 **Correction terminée !**\n\n` +
            `📄 Fichier : ${data.file}\n` +
            `📱 Snapshot : ${data.snapshot}\n` +
            `✅ Corrections appliquées : **${fx.corrections_applied || 0}**\n` +
            `💾 Sauvegarde créée : ${fx.backup_created ? "Oui" : "Non"}`,
            "bot"
        );
    } catch {
        removeTyping();
        addMessage("❌ Erreur de connexion au serveur.", "bot");
    }
}

// ─── TAB 2 — Correction XPath ────────────────────────────

async function runSelectorFix() {
    const poFile = document.getElementById("selectorPoFile").value.trim();
    const btn    = document.querySelector("#panel-selector .btn-action");
    const load   = document.getElementById("selectorLoading");
    const result = document.getElementById("selectorResult");

    btn.disabled = true;
    load.style.display = "block";
    result.style.display = "none";

    try {
        const resp = await fetch("/selector-fix", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ po_file: poFile }),
        });
        const data = await resp.json();

        if (data.error) {
            showResult("selector", "error",
                `❌ Erreur : ${data.error}`, [], [], []);
            return;
        }

        const headerCls = data.broken_count === 0 ? "success" : "warning";
        const headerTxt = data.broken_count === 0
            ? `✅ Aucun sélecteur cassé — ${data.po_file} est valide !`
            : `⚠️  ${data.broken_count} sélecteur(s) cassé(s) détecté(s) dans ${data.po_file}`;

        // Stats grid
        document.getElementById("selectorResultGrid").innerHTML = `
            <div class="stat-box"><div class="stat-num">${data.broken_count}</div><div class="stat-lbl">Sélecteurs cassés</div></div>
            <div class="stat-box"><div class="stat-num">${data.fixed_count}</div><div class="stat-lbl">Auto-corrigés</div></div>
            <div class="stat-box"><div class="stat-num">${data.broken_count - data.fixed_count}</div><div class="stat-lbl">À corriger manuellement</div></div>
        `;

        // Issues table
        let tableHtml = "";
        if (data.issues && data.issues.length) {
            tableHtml = `<h4 style="color:#a6adc8;font-size:.82rem;margin-bottom:10px">Sélecteurs invalides détectés</h4>
            <table class="result-table">
            <thead><tr><th>Champ</th><th>Sélecteur</th><th>Raison</th></tr></thead><tbody>`;
            data.issues.forEach(i => {
                tableHtml += `<tr>
                    <td class="badge-critical">${i.field || "?"}</td>
                    <td class="code-sm">${i.selector || "?"}</td>
                    <td>${i.reason || "Sélecteur invalide"}</td>
                </tr>`;
            });
            tableHtml += "</tbody></table>";
        }
        if (data.fixes && data.fixes.length) {
            tableHtml += `<h4 style="color:#a6e3a1;font-size:.82rem;margin:14px 0 10px">Corrections appliquées</h4>
            <table class="result-table">
            <thead><tr><th>Champ</th><th>Ancien</th><th>Nouveau</th><th>Fiabilité</th></tr></thead><tbody>`;
            data.fixes.forEach(f => {
                tableHtml += `<tr>
                    <td class="badge-fixed">${f.field}</td>
                    <td class="code-sm" style="color:#f38ba8">${f.old}</td>
                    <td class="code-sm" style="color:#a6e3a1">${f.new}</td>
                    <td>${f.confidence || "medium"}</td>
                </tr>`;
            });
            tableHtml += "</tbody></table>";
        }

        document.getElementById("selectorResultHeader").className = `result-header ${headerCls}`;
        document.getElementById("selectorResultHeader").textContent = headerTxt;
        document.getElementById("selectorIssuesTable").innerHTML = tableHtml;
        result.style.display = "block";

    } catch (e) {
        document.getElementById("selectorResultHeader").className = "result-header error";
        document.getElementById("selectorResultHeader").textContent = "❌ Erreur de connexion au serveur.";
        result.style.display = "block";
    } finally {
        btn.disabled = false;
        load.style.display = "none";
    }
}

// ─── TAB 3 — Scénarios BDD ───────────────────────────────

async function runScenarioGenerate() {
    const poFile = document.getElementById("scenarioPoFile").value.trim();
    const mode   = document.querySelector('input[name="scenarioMode"]:checked').value;
    const btn    = document.querySelector("#panel-scenario .btn-action");
    const load   = document.getElementById("scenarioLoading");
    const result = document.getElementById("scenarioResult");

    btn.disabled = true;
    load.style.display = "block";
    result.style.display = "none";
    load.textContent = mode === "llm"
        ? "⏳ Génération via Groq LLM en cours..."
        : "⏳ Génération offline en cours...";

    try {
        const resp = await fetch("/scenario-generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ po_file: poFile, mode }),
        });
        const data = await resp.json();

        if (data.error) {
            document.getElementById("scenarioResultHeader").className = "result-header error";
            document.getElementById("scenarioResultHeader").textContent = `❌ Erreur : ${data.error}`;
            document.getElementById("scenarioResultGrid").innerHTML = "";
            document.getElementById("scenarioResultFiles").innerHTML = "";
            result.style.display = "block";
            return;
        }

        const ok = data.success;
        document.getElementById("scenarioResultHeader").className = `result-header ${ok ? "success" : "warning"}`;
        document.getElementById("scenarioResultHeader").textContent = ok
            ? `✅ Génération réussie pour ${data.po_file} (source: ${data.feature_source})`
            : `⚠️  Génération partielle pour ${data.po_file}`;

        document.getElementById("scenarioResultGrid").innerHTML = `
            <div class="stat-box"><div class="stat-num">${data.scenario_count}</div><div class="stat-lbl">Scénarios Gherkin</div></div>
            <div class="stat-box"><div class="stat-num">${data.step_count}</div><div class="stat-lbl">Step Definitions</div></div>
            <div class="stat-box"><div class="stat-num">3</div><div class="stat-lbl">Fichiers générés</div></div>
        `;

        const files = data.files || {};
        document.getElementById("scenarioResultFiles").innerHTML = `
            <div class="file-row">
                <span class="file-icon">🥒</span>
                <span class="file-type">.feature</span>
                <span class="file-path">${files.feature || "—"}</span>
            </div>
            <div class="file-row">
                <span class="file-icon">☕</span>
                <span class="file-type">Steps.java</span>
                <span class="file-path">${files.steps || "—"}</span>
            </div>
            <div class="file-row">
                <span class="file-icon">🏃</span>
                <span class="file-type">Runner.java</span>
                <span class="file-path">${files.runner || "—"}</span>
            </div>`;

        result.style.display = "block";

    } catch {
        document.getElementById("scenarioResultHeader").className = "result-header error";
        document.getElementById("scenarioResultHeader").textContent = "❌ Erreur de connexion au serveur.";
        result.style.display = "block";
    } finally {
        btn.disabled = false;
        load.style.display = "none";
    }
}

// ─── TAB 4 — Sync Mocks ──────────────────────────────────

async function runMockSync() {
    const btn    = document.querySelector("#panel-mock .btn-action");
    const load   = document.getElementById("mockLoading");
    const result = document.getElementById("mockResult");

    btn.disabled = true;
    load.style.display = "block";
    result.style.display = "none";

    try {
        const resp = await fetch("/mock-sync", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({}),
        });
        const data = await resp.json();

        if (data.error) {
            document.getElementById("mockResultHeader").className = "result-header error";
            document.getElementById("mockResultHeader").textContent = `❌ Erreur : ${data.error}`;
            result.style.display = "block";
            return;
        }

        const hasDiffs = data.diffs_found > 0;
        document.getElementById("mockResultHeader").className = `result-header ${hasDiffs ? "warning" : "success"}`;
        document.getElementById("mockResultHeader").textContent = hasDiffs
            ? `⚠️  ${data.diffs_found} différence(s) détectée(s) — mock ${data.mock_id} mis à jour`
            : `✅ Mock ${data.mock_id} synchronisé — aucune différence`;

        document.getElementById("mockResultGrid").innerHTML = `
            <div class="stat-box"><div class="stat-num">${data.diffs_found}</div><div class="stat-lbl">Différences</div></div>
            <div class="stat-box"><div class="stat-num">${data.mock_updated ? "✅" : "—"}</div><div class="stat-lbl">Mock mis à jour</div></div>
            <div class="stat-box"><div class="stat-num">${data.deepdiff_used ? "DeepDiff" : "Basique"}</div><div class="stat-lbl">Mode diff</div></div>
        `;

        let diffHtml = "";
        if (data.diffs && data.diffs.length) {
            diffHtml = `<h4 style="color:#a6adc8;font-size:.82rem;margin-bottom:10px">Détail des différences</h4>
            <table class="result-table">
            <thead><tr><th>Chemin</th><th>Ancien</th><th>Nouveau</th><th>Type</th></tr></thead><tbody>`;
            data.diffs.forEach(d => {
                const typeCls = d.type === "added" ? "badge-added" : d.type === "removed" ? "badge-removed" : "badge-changed";
                diffHtml += `<tr>
                    <td class="code-sm">${d.path || "?"}</td>
                    <td style="color:#f38ba8">${d.old || "—"}</td>
                    <td style="color:#a6e3a1">${d.new || d.detail || "—"}</td>
                    <td class="${typeCls}">${d.type || "?"}</td>
                </tr>`;
            });
            diffHtml += "</tbody></table>";
            if (data.backup_path) {
                diffHtml += `<p style="color:#6c7086;font-size:.78rem;margin-top:10px">💾 Backup : <span class="code-sm">${data.backup_path}</span></p>`;
            }
        }
        document.getElementById("mockDiffsTable").innerHTML = diffHtml;
        result.style.display = "block";

    } catch {
        document.getElementById("mockResultHeader").className = "result-header error";
        document.getElementById("mockResultHeader").textContent = "❌ Erreur de connexion au serveur.";
        result.style.display = "block";
    } finally {
        btn.disabled = false;
        load.style.display = "none";
    }
}

// ─── TAB 5 — Historique SQLite ──────────────────────────

const EVT_LABELS = {
    analysis:    { label: "Analyse",       cls: "evt-analysis"  },
    selector_fix:{ label: "Correction XPath", cls: "evt-selector" },
    scenario_gen:{ label: "Scénarios BDD", cls: "evt-scenario"  },
    mock_sync:   { label: "Sync Mocks",    cls: "evt-mock_sync" },
    pipeline:    { label: "Pipeline E2E",  cls: "evt-pipeline"  },
};

async function loadHistory() {
    const typeFilter   = document.getElementById("historyTypeFilter").value;
    const statusFilter = document.getElementById("historyStatusFilter").value;
    const wrap         = document.getElementById("historyTableWrap");

    wrap.innerHTML = '<div style="color:#a6adc8;padding:20px 24px">⏳ Chargement...</div>';

    try {
        // Stats
        const sResp = await fetch("/history/stats");
        const stats = await sResp.json();
        const bt = stats.by_type || {};
        document.getElementById("hstatTotal").querySelector(".stat-num").textContent    = stats.total_events || 0;
        document.getElementById("hstatAnalysis").querySelector(".stat-num").textContent = bt.analysis     || 0;
        document.getElementById("hstatSelector").querySelector(".stat-num").textContent = bt.selector_fix || 0;
        document.getElementById("hstatScenario").querySelector(".stat-num").textContent = bt.scenario_gen || 0;
        document.getElementById("hstatMock").querySelector(".stat-num").textContent     = bt.mock_sync    || 0;

        // Événements filtrés
        let url = "/history?limit=100";
        if (typeFilter)   url += "&type="   + typeFilter;
        if (statusFilter) url += "&status=" + statusFilter;

        const eResp = await fetch(url);
        const eData = await eResp.json();
        const events = eData.events || [];

        if (!events.length) {
            wrap.innerHTML = '<div style="color:#6c7086;font-size:.85rem;padding:20px 24px">Aucun événement enregistré.</div>';
            return;
        }

        let html = `<table class="history-table">
        <thead><tr>
            <th>#</th><th>Date / Heure</th><th>Type</th><th>Statut</th><th>Résumé</th><th>Durée</th>
        </tr></thead><tbody>`;

        events.forEach(ev => {
            const evInfo  = EVT_LABELS[ev.event_type] || { label: ev.event_type, cls: "evt-default" };
            const ts      = ev.ts ? ev.ts.replace("T", " ").substring(0, 19) : "?";
            const statusCls = ev.status === "ok" ? "status-ok"
                            : ev.status === "error" ? "status-error" : "status-partial";
            const statusLbl = ev.status === "ok" ? "✅ OK"
                            : ev.status === "error" ? "❌ Erreur" : "⚠️ Partiel";
            const dur = ev.duration_ms != null ? ev.duration_ms + " ms" : "—";

            html += `<tr>
                <td style="color:#6c7086">${ev.id}</td>
                <td style="font-family:monospace;font-size:.76rem;color:#a6adc8">${ts}</td>
                <td><span class="evt-type-badge ${evInfo.cls}">${evInfo.label}</span></td>
                <td class="${statusCls}">${statusLbl}</td>
                <td>${ev.summary || "—"}</td>
                <td style="color:#6c7086">${dur}</td>
            </tr>`;
        });

        html += "</tbody></table>";
        wrap.innerHTML = html;

    } catch (e) {
        wrap.innerHTML = `<div style="color:#f38ba8;padding:20px 24px">❌ Erreur : ${e.message}</div>`;
    }
}

async function clearHistoryDB() {
    const typeFilter = document.getElementById("historyTypeFilter").value;
    const label = typeFilter
        ? `les événements de type "${typeFilter}"`
        : "tout l'historique";
    if (!confirm(`Supprimer ${label} ?`)) return;
    try {
        const resp = await fetch("/history/clear", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ event_type: typeFilter || null }),
        });
        const data = await resp.json();
        addMessage(`🗑️ Historique vidé : ${data.deleted} événements supprimés.`, "bot");
        switchTab("history");
        await loadHistory();
    } catch {
        addMessage("❌ Erreur lors de la suppression de l'historique.", "bot");
    }
}

// ─── Init ─────────────────────────────────────────────────
window.onload = loadSnapshots;

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

// ─── TAB 6 — Métriques de performance ────────────────────

const OP_LABELS = {
    analysis:     "🔍 Analyse",
    selector_fix: "🔧 Correction XPath",
    scenario_gen: "🎬 Scénarios BDD",
    mock_sync:    "🔄 Sync Mocks",
    pipeline:     "⚙️ Pipeline E2E",
};

async function loadMetrics() {
    const opFilter = document.getElementById("metricsOpFilter")?.value || "";

    // --- KPIs globaux ---
    try {
        const resp = await fetch("/metrics");
        const kpis = await resp.json();

        const setKpi = (id, val) => {
            const el = document.getElementById(id);
            if (el) el.querySelector(".kpi-num").textContent = val;
        };
        setKpi("kpiTotal",        kpis.total_runs ?? "—");
        setKpi("kpiSuccessRate",  kpis.total_runs ? `${kpis.success_rate_pct ?? 0}%` : "—");
        setKpi("kpiAvgDuration",  kpis.total_runs ? `${kpis.avg_duration_ms ?? 0} ms` : "—");

        // Dernier run
        const lr = kpis.last_run_ts ? new Date(kpis.last_run_ts).toLocaleString("fr-FR") : "—";
        const lrEl = document.getElementById("kpiLastRun");
        if (lrEl) lrEl.querySelector(".kpi-num").textContent = lr;

        // Cartes par opération
        const byOpWrap = document.getElementById("metricsByOp");
        if (byOpWrap) {
            const byOp = kpis.by_operation || {};
            if (Object.keys(byOp).length === 0) {
                byOpWrap.innerHTML = `<div style="color:#6c7086;font-size:.85rem">Aucun run enregistré pour l'instant.</div>`;
            } else {
                const maxDur = Math.max(...Object.values(byOp).map(v => v.avg_duration_ms || 0), 1);
                byOpWrap.innerHTML = Object.entries(byOp).map(([op, v]) => {
                    const pct = Math.round((v.avg_duration_ms / maxDur) * 100);
                    const label = OP_LABELS[op] || op;
                    return `
                    <div class="op-card">
                        <div class="op-card-title">${label}</div>
                        <div class="op-card-row"><span>Runs</span><span>${v.count}</span></div>
                        <div class="op-card-row"><span>Succès</span><span>${v.success_rate_pct ?? 0}%</span></div>
                        <div class="op-card-row dur-bar-wrap">
                            <span>Moy.</span>
                            <div class="dur-bar"><div class="dur-bar-fill" style="width:${pct}%"></div></div>
                            <span>${v.avg_duration_ms} ms</span>
                        </div>
                    </div>`;
                }).join("");
            }
        }
    } catch (e) {
        console.error("Erreur chargement KPIs métriques", e);
    }

    // --- Timeline des runs ---
    const wrap = document.getElementById("metricsTableWrap");
    if (!wrap) return;
    wrap.innerHTML = `<div style="color:#6c7086;font-size:.85rem;padding:20px 24px">⏳ Chargement...</div>`;

    try {
        const url = "/metrics/history?limit=100" + (opFilter ? `&operation=${opFilter}` : "");
        const resp = await fetch(url);
        const data = await resp.json();
        const runs = data.runs || [];

        if (runs.length === 0) {
            wrap.innerHTML = `<div style="color:#6c7086;font-size:.85rem;padding:20px 24px">Aucun run enregistré.</div>`;
            return;
        }

        const rows = runs.map(r => {
            const label   = OP_LABELS[r.operation] || r.operation;
            const ts      = new Date(r.ts).toLocaleString("fr-FR");
            const statCls = r.status === "success" ? "status-ok" : (r.status === "error" ? "status-error" : "status-partial");
            const statLbl = r.status === "success" ? "✅ OK" : (r.status === "error" ? "❌ Erreur" : "⚠️ Partiel");
            const details = r.details ? Object.entries(r.details)
                .map(([k, v]) => `<span style="color:#7f849c">${k}:</span> <b>${v}</b>`)
                .join(" &nbsp;·&nbsp; ") : "";
            const barW    = Math.min(100, Math.round(r.duration_ms / 20));
            return `<tr>
                <td style="color:#6c7086;white-space:nowrap">${ts}</td>
                <td>${label}</td>
                <td><span class="${statCls}">${statLbl}</span></td>
                <td>
                    <div class="dur-bar-wrap">
                        <div class="dur-bar" style="min-width:60px">
                            <div class="dur-bar-fill" style="width:${barW}%"></div>
                        </div>
                        <span style="color:#cdd6f4">${r.duration_ms} ms</span>
                    </div>
                </td>
                <td style="font-size:.75rem;color:#7f849c">${details}</td>
            </tr>`;
        }).join("");

        wrap.innerHTML = `
            <table class="history-table">
                <thead><tr>
                    <th>Date</th>
                    <th>Opération</th>
                    <th>Statut</th>
                    <th>Durée</th>
                    <th>Détails</th>
                </tr></thead>
                <tbody>${rows}</tbody>
            </table>`;

    } catch (e) {
        wrap.innerHTML = `<div style="color:#f38ba8;padding:20px 24px">❌ Erreur : ${e.message}</div>`;
    }
}

async function clearMetricsDB() {
    const opFilter = document.getElementById("metricsOpFilter")?.value;
    const label    = opFilter ? `les runs de "${OP_LABELS[opFilter] || opFilter}"` : "toutes les métriques";
    if (!confirm(`Réinitialiser ${label} ?`)) return;
    try {
        const resp = await fetch("/metrics/clear", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ operation: opFilter || null }),
        });
        const data = await resp.json();
        addMessage(`🗑️ Métriques réinitialisées : ${data.deleted} runs supprimés.`, "bot");
        await loadMetrics();
    } catch {
        addMessage("❌ Erreur lors de la réinitialisation des métriques.", "bot");
    }
}
