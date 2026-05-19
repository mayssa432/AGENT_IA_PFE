# DEMO_GUIDE.md — Guide rapide démo soutenance PFE

## Agent IA pour la Maintenance Automatisée des Tests Mobiles

---

## Prérequis

```batch
cd c:\Users\m.derwich\Downloads\AGENT_IA_PFE
venv\Scripts\activate
```

---

## Démo express (toute la présentation)

```batch
run_demo.bat
```

Ou directement :
```batch
set PYTHONUTF8=1
venv\Scripts\python demo_soutenance.py
```

→ **9/9 livrables validés en ~20 secondes**

---

## Démos individuelles par livrable

| # | Commande | Description |
|---|----------|-------------|
| 1 | `venv\Scripts\python orchestrate.py --pages AGENT_IA_PFE/src/test/java/.../mobile --dry-run` | Pipeline E2E 28 fichiers Java |
| 2 | `venv\Scripts\python demo_selector_fix.py` | Auto-correction sélecteurs XPath |
| 3 | `venv\Scripts\python demo_mock_manager.py` | Diff sémantique + mise à jour mocks |
| 4 | `venv\Scripts\python demo_scenario_generator.py --batch 3 --offline` | Génération scénarios BDD |
| 5 | `run_demo.bat server` → http://localhost:5000 | Dashboard Flask 6 onglets |
| 6 | *(onglet Historique dans le dashboard)* | SQLite persistant |
| 7 | *(fichier `.github/workflows/ci.yml`)* | GitHub Actions 4 jobs |
| 8 | *(onglet Métriques dans le dashboard)* | Temps d'exécution + KPIs |
| 9 | `venv\Scripts\python demo_app_manager.py` | App Manager mock / ADB |

---

## Serveur web (dashboard)

```batch
run_demo.bat server
```
Ouvrir : **http://localhost:5000**

Onglets disponibles :
- 💬 **Chat** — Interaction naturelle avec l'agent
- 🔧 **Correction XPath** — Détection et correction auto
- 🎬 **Scénarios BDD** — Génération Gherkin + step definitions
- 🔄 **Sync Mocks** — Diff sémantique real vs mock
- 📜 **Historique** — Journal SQLite filtrable
- 📈 **Métriques** — KPIs temps réel (durée, taux succès)

---

## Tests unitaires

```batch
run_demo.bat tests
# ou
venv\Scripts\pytest tests/ -q
```
**144 tests — 100% passage**

---

## Architecture du projet

```
AGENT_IA_PFE/
├── orchestrate.py           # Livrable #1 — pipeline E2E
├── demo_selector_fix.py     # Livrable #2 — correction XPath
├── demo_mock_manager.py     # Livrable #3 — mock diff
├── demo_scenario_generator.py  # Livrable #4 — BDD gen
├── chat_server.py           # Livrable #5 — serveur Flask
├── history/db.py            # Livrable #6 — SQLite historique
├── .github/workflows/ci.yml # Livrable #7 — CI/CD
├── metrics/tracker.py       # Livrable #8 — métriques
├── demo_app_manager.py      # Livrable #9 — App Manager
├── demo_soutenance.py       # Livrable #10 — démo complète
├── analyzers/               # Analyse XPath, annotations...
├── dom_inspector/           # Appium DOM, validation
├── app_manager/             # Gestion devices ADB
├── static/                  # UI : index.html, script.js, style.css
└── tests/                   # 144 tests unitaires
```

---

## Points clés pour le jury

1. **Sans device** — toutes les démos fonctionnent en mode mock
2. **Modulaire** — chaque livrable est indépendant et testable
3. **Production-ready** — CI/CD, métriques, historique, coverage
4. **LLM optionnel** — `--offline` désactive Groq pour CI/démo
5. **Extensible** — ajout simple de nouveaux analyseurs ou démos
