# 🤖 Agent IA Appium — PFE Project

An intelligent agent for analyzing and validating **Appium Page Object Java files**.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)
- [Author](#author)

---

## 🎯 Overview

This project is an AI-powered agent that automatically analyzes Java Page Object files
used in **Appium mobile test automation**. It detects issues such as :
- ❌ Invalid XPath selectors
- 🔁 Duplicate fields across files
- ⚠️ Missing or incorrect annotations
- 🐛 Unbalanced brackets/parentheses in XPath

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Analysis** | Scans all Java PO files in a project |
| 🐛 **XPath Validation** | Detects invalid XPath expressions |
| 🔁 **Duplicate Detection** | Finds duplicate fields across files |
| 🛠️ **Fix Suggestions** | Provides correction recommendations |
| 📊 **Detailed Reports** | Generates complete analysis reports |
| 💬 **Interactive Chat** | Conversational interface for results |
| 🌐 **Web Interface** | Modern browser-based UI |

---

## 📁 Project Structure

AGENT_IA_PFE/
│
├── 📁 AGENT_IA_PFE/       # Core agent module
├── 📁 analyzers/          # XPath, duplicate, annotation analyzers
├── 📁 models/             # Data models & schemas
├── 📁 output/             # Generated reports
├── 📁 static/             # Web interface (HTML/CSS/JS)
├── 📁 utils/              # Helper utilities
├── 📄 agent.py            # Main AI Agent
├── 📄 chat_server.py      # Flask API server
├── 📄 gherkin_parser.py   # Gherkin feature parser
├── 📄 prompt_builder.py   # AI prompt builder
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md           # This file
