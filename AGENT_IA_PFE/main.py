# -*- coding: utf-8 -*-
import os
import sys

# ── FORCER UTF-8 AVANT TOUT ─────────────────────────────
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["PYTHONUTF8"]       = "1"
os.environ["OPENAI_LOG"]       = "none"

# Patch Windows console
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    ctypes.windll.kernel32.SetConsoleCP(65001)

import argparse
from gherkin_parser import GherkinParser
from agent import GherkinToJavaAgent
from file_writer import JavaFileWriter
"""
Main - Point d'entree de l'agent Gherkin -> Java Automation

Usage:
    python main.py <chemin_fichier.feature> [--output <repertoire>] [--model <modele>]

Exemples:
    python main.py examples/login.feature
    python main.py examples/login.feature --output ./generated
    python main.py examples/login.feature --output ./generated --model llama-3.3-70b-versatile
"""

import argparse
import os
import sys

# ── Forcer UTF-8 via variable d'environnement ────────────
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["PYTHONUTF8"] = "1"

from gherkin_parser import GherkinParser
from agent import GherkinToJavaAgent
from file_writer import JavaFileWriter


def parse_args():
    parser = argparse.ArgumentParser(
        description="Agent IA : Gherkin (.feature) -> Java Selenium/Cucumber"
    )
    parser.add_argument(
        "feature_file",
        help="Chemin vers le fichier .feature Gherkin"
    )
    parser.add_argument(
        "--output", "-o",
        default="./output",
        help="Repertoire de sortie (defaut: ./output)"
    )
    parser.add_argument(
        "--model", "-m",
        default="llama-3.3-70b-versatile",
        help="Modele OpenAI a utiliser (defaut: llama-3.3-70b-versatile)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Affiche le prompt sans appeler l'API"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # ── 1. Validation du fichier d'entree ──────────────────
    feature_path = os.path.abspath(args.feature_file)
    if not os.path.exists(feature_path):
        print(f"[ERROR] Fichier introuvable : {feature_path}")
        sys.exit(1)

    if not feature_path.endswith(".feature"):
        print(f"[WARNING] Le fichier n'a pas l'extension .feature : {feature_path}")

    # ── 2. Parsing Gherkin ─────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  AGENT GHERKIN -> JAVA AUTOMATION")
    print(f"{'='*60}")
    print(f"[PARSER] Lecture du fichier : {feature_path}")

    gherkin_parser = GherkinParser()
    try:
        feature = gherkin_parser.parse_file(feature_path)
    except Exception as e:
        print(f"[ERROR] Erreur de parsing Gherkin : {e}")
        sys.exit(1)

    print(f"[PARSER] OK Feature : '{feature.name}'")
    print(f"[PARSER] OK Scenarios trouves : {len(feature.scenarios)}")
    for s in feature.scenarios:
        print(f"           -> {s.name} ({len(s.steps)} steps)")

    # ── 3. Mode Dry Run ────────────────────────────────────
    if args.dry_run:
        from prompt_builder import build_user_prompt, SYSTEM_PROMPT
        print("\n[DRY-RUN] SYSTEM PROMPT:")
        print(SYSTEM_PROMPT[:500] + "...")
        print("\n[DRY-RUN] USER PROMPT:")
        print(build_user_prompt(feature))
        print("\n[DRY-RUN] Aucun appel API effectue.")
        return

    # ── 4. Appel de l'agent IA ─────────────────────────────
    print(f"\n[AGENT] Modele utilise : {args.model}")
    agent = GherkinToJavaAgent(model=args.model)

    try:
        generated = agent.generate_with_retry(feature, max_retries=3)
    except Exception as e:
        print(f"[ERROR] Echec de la generation : {e}")
        sys.exit(1)

    # ── 5. Ecriture des fichiers ───────────────────────────
    output_dir = os.path.abspath(args.output)
    print(f"\n[WRITER] Repertoire de sortie : {output_dir}")

    writer = JavaFileWriter(output_dir)
    written = writer.write_all(generated)
    writer.write_summary(written, feature.name)

    # ── 6. Resume final ────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  GENERATION TERMINEE")
    print(f"{'='*60}")
    print(f"  {len(written)} fichier(s) cree(s) dans : {output_dir}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
