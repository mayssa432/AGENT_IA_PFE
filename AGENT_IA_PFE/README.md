# Agent IA : Gherkin → Java Automation 🤖

Un agent Python qui lit un fichier **Gherkin** (`.feature`) et génère automatiquement un **projet d'automatisation Java** complet (Selenium + Cucumber + JUnit 5).

---

## 🏗️ Architecture du projet

```
AGENT_IA_PFE/
│
├── main.py               ← Point d'entrée CLI
├── gherkin_parser.py     ← Parsing des fichiers .feature
├── prompt_builder.py     ← Construction du prompt OpenAI
├── agent.py              ← Appel à l'API OpenAI (GPT-4o)
├── file_writer.py        ← Écriture des fichiers Java générés
│
├── examples/
│   └── login.feature     ← Exemple de fichier Gherkin
│
├── output/               ← Fichiers Java générés (créé automatiquement)
│   └── src/test/
│       ├── java/
│       │   ├── pages/    ← Page Objects (POM)
│       │   ├── steps/    ← Step Definitions Cucumber
│       │   └── runners/  ← Test Runners JUnit
│       └── resources/
│           └── features/ ← Fichiers .feature copiés
│
├── .env                  ← Clé API OpenAI (à configurer)
└── requirements.txt      ← Dépendances Python
```

---

## ⚙️ Installation

### 1. Prérequis
- Python 3.11+
- Un compte OpenAI avec une clé API

### 2. Installer les dépendances
```powershell
pip install -r requirements.txt
```

### 3. Configurer la clé API
Éditez le fichier `.env` :
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🚀 Utilisation

### Commande de base
```powershell
python main.py examples/login.feature
```

### Avec répertoire de sortie personnalisé
```powershell
python main.py examples/login.feature --output ./mon_projet_java
```

### Avec un modèle spécifique
```powershell
python main.py examples/login.feature --model gpt-4o --output ./output
```

### Mode test (sans appel API)
```powershell
python main.py examples/login.feature --dry-run
```

---

## 📤 Fichiers Java générés

Pour chaque fichier `.feature`, l'agent génère **5 fichiers** :

| Fichier | Description |
|--------|-------------|
| `*.feature` | Copie du scénario Gherkin |
| `*StepDefinitions.java` | Implémentation des steps (`@Given`, `@When`, `@Then`) |
| `*Page.java` | Page Object avec `@FindBy` et Selenium |
| `BasePage.java` | Classe de base avec WebDriver et WebDriverWait |
| `*TestRunner.java` | Runner JUnit 5 + Cucumber |

---

## 📦 Dépendances Maven requises dans le projet Java

```xml
<!-- Selenium -->
<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>4.18.1</version>
</dependency>

<!-- Cucumber -->
<dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>7.15.0</version>
    <scope>test</scope>
</dependency>

<!-- JUnit 5 -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
</dependency>

<!-- WebDriverManager -->
<dependency>
    <groupId>io.github.bonigarcia</groupId>
    <artifactId>webdrivermanager</artifactId>
    <version>5.7.0</version>
    <scope>test</scope>
</dependency>
```

---

## 🔄 Flux de traitement

```
.feature file
     │
     ▼
[GherkinParser]       ← Parse les scenarios, steps, tags
     │
     ▼
[PromptBuilder]       ← Construit le prompt pour GPT-4o
     │
     ▼
[GherkinToJavaAgent]  ← Appelle l'API OpenAI
     │
     ▼
[JavaFileWriter]      ← Écrit les fichiers Java sur le disque
     │
     ▼
output/ (Java project)
```
