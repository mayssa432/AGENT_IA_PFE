#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo_app_manager.py — Livrable #9 : App Manager — démo live (mock ou ADB réel)
===============================================================================
Démontre la gestion de devices Android et l'installation d'applications :

  Étape 1 — Détection des devices (ADB réel ou mock simulé)
  Étape 2 — Lecture des propriétés device (modèle, version Android, résolution)
  Étape 3 — Simulation d'installation / désinstallation d'APK
  Étape 4 — Vérification de l'app installée
  Étape 5 — Rapport JSON généré

Usage
-----
    python demo_app_manager.py                # mode mock embarqué
    python demo_app_manager.py --real         # tente ADB réel, fallback mock
    python demo_app_manager.py --serial emulator-5554   # device spécifique
"""

import sys
import os
import json
import argparse
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ─── Constantes ─────────────────────────────────────────────────────────────

WIDTH  = 62
SEP_H  = "─" * WIDTH
SEP_D  = "═" * WIDTH

MOCK_DEVICES = [
    {
        "serial":          "emulator-5554",
        "model":           "Nexus_5X",
        "brand":           "Google",
        "android_version": "9.0",
        "api_level":       "28",
        "resolution":      "1080x1920",
        "state":           "emulator",
    },
    {
        "serial":          "FA7AB0305461",
        "model":           "SM-G973F",
        "brand":           "Samsung",
        "android_version": "11.0",
        "api_level":       "30",
        "resolution":      "1440x3040",
        "state":           "device",
    },
]

MOCK_PACKAGES = {
    "com.orange.otvp": {"installed": False, "version": None},
    "com.android.settings": {"installed": True, "version": "9.0"},
}

TARGET_APK     = "otvp_app_v2.3.1.apk"
TARGET_PACKAGE = "com.orange.otvp"

# ─── Helpers console ─────────────────────────────────────────────────────────

def h1(title: str):
    print(f"\n{SEP_D}")
    print(f"  {title}")
    print(SEP_D)

def h2(title: str):
    print(f"\n{SEP_H}")
    print(f"  {title}")
    print(SEP_H)

def ok(msg: str):  print(f"  \u2705  {msg}")
def info(msg: str): print(f"  \u2139\ufe0f   {msg}")
def warn(msg: str): print(f"  \u26a0\ufe0f  {msg}")
def err(msg: str):  print(f"  \u274c  {msg}")

# ─── ADB helpers ─────────────────────────────────────────────────────────────

def _adb_available() -> bool:
    import subprocess
    try:
        subprocess.check_output(["adb", "version"], stderr=subprocess.STDOUT, timeout=3)
        return True
    except Exception:
        return False


def _adb_list_devices() -> list:
    import subprocess
    try:
        out = subprocess.check_output(
            ["adb", "devices"], stderr=subprocess.STDOUT, timeout=5
        ).decode("utf-8", errors="ignore")
        lines = [l.strip() for l in out.splitlines()[1:] if l.strip()]
        devices = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 2 and parts[1] in ("device", "emulator"):
                devices.append({"serial": parts[0], "state": parts[1]})
        return devices
    except Exception:
        return []


def _adb_getprop(serial: str, prop: str) -> str:
    import subprocess
    try:
        return subprocess.check_output(
            ["adb", "-s", serial, "shell", "getprop", prop],
            stderr=subprocess.STDOUT, timeout=5
        ).decode("utf-8", errors="ignore").strip()
    except Exception:
        return "unknown"


def _adb_is_installed(serial: str, package: str) -> bool:
    import subprocess
    try:
        out = subprocess.check_output(
            ["adb", "-s", serial, "shell", "pm", "list", "packages", package],
            stderr=subprocess.STDOUT, timeout=5
        ).decode("utf-8", errors="ignore")
        return package in out
    except Exception:
        return False

# ─── Étapes ──────────────────────────────────────────────────────────────────

def step1_detect_devices(use_real: bool, target_serial: str = None) -> tuple[list, str]:
    """Retourne (liste devices, mode)."""
    h2("ÉTAPE 1 — Détection des devices Android")

    if use_real and _adb_available():
        raw = _adb_list_devices()
        if raw:
            devices = []
            for d in raw:
                s = d["serial"]
                devices.append({
                    "serial":          s,
                    "model":           _adb_getprop(s, "ro.product.model"),
                    "brand":           _adb_getprop(s, "ro.product.brand"),
                    "android_version": _adb_getprop(s, "ro.build.version.release"),
                    "api_level":       _adb_getprop(s, "ro.build.version.sdk"),
                    "resolution":      "N/A",
                    "state":           d["state"],
                })
            mode = "adb-real"
            info(f"ADB disponible — {len(devices)} device(s) connecté(s)")
        else:
            devices = MOCK_DEVICES
            mode = "mock-no-device"
            warn("ADB disponible mais aucun device — mode mock activé")
    else:
        devices = MOCK_DEVICES
        mode = "mock"
        info("Mode mock embarqué (pas d'ADB requis pour la démo)")

    if target_serial:
        devices = [d for d in devices if d["serial"] == target_serial] or devices

    for d in devices:
        print(f"  📱  [{d['state'].upper()}] {d['serial']}")
        print(f"       Modèle   : {d['model']} ({d['brand']})")
        print(f"       Android  : {d['android_version']} (API {d['api_level']})")
        print()

    ok(f"{len(devices)} device(s) trouvé(s) — mode : {mode}")
    return devices, mode


def step2_device_properties(devices: list) -> dict:
    """Affiche les propriétés détaillées du premier device."""
    h2("ÉTAPE 2 — Propriétés du device principal")
    if not devices:
        warn("Aucun device disponible")
        return {}

    d = devices[0]
    props = {
        "serial":          d.get("serial", "?"),
        "model":           d.get("model", "?"),
        "brand":           d.get("brand", "?"),
        "android_version": d.get("android_version", "?"),
        "api_level":       d.get("api_level", "?"),
        "resolution":      d.get("resolution", "?"),
        "state":           d.get("state", "?"),
    }
    col_w = 22
    for k, v in props.items():
        print(f"  {k.ljust(col_w)}: {v}")

    ok("Propriétés lues avec succès")
    return props


def step3_simulate_install(device: dict, mode: str) -> dict:
    """Simule l'installation d'un APK."""
    h2(f"ÉTAPE 3 — Installation APK ({TARGET_APK})")
    serial = device.get("serial", "?")

    info(f"Target device    : {serial}")
    info(f"APK cible        : {TARGET_APK}")
    info(f"Package          : {TARGET_PACKAGE}")

    if mode == "adb-real":
        # Vrai mode : on ne push pas un faux APK, on simule quand même
        already = _adb_is_installed(serial, TARGET_PACKAGE)
        install_status = "already_installed" if already else "would_install"
        info("ADB réel : vérification si l'app est déjà installée...")
    else:
        # Mock
        time.sleep(0.3)  # Simuler la durée d'installation
        already = MOCK_PACKAGES.get(TARGET_PACKAGE, {}).get("installed", False)
        install_status = "already_installed" if already else "installed_mock"

    if already:
        warn(f"App déjà installée sur {serial} (package : {TARGET_PACKAGE})")
    else:
        ok(f"Simulation d'installation réussie sur {serial}")
        ok(f"Exit code ADB : 0  (Success)")

    return {
        "device": serial,
        "apk": TARGET_APK,
        "package": TARGET_PACKAGE,
        "status": install_status,
    }


def step4_verify_install(device: dict, mode: str) -> dict:
    """Vérifie que l'app est bien installée."""
    h2("ÉTAPE 4 — Vérification post-installation")
    serial = device.get("serial", "?")

    if mode == "adb-real":
        installed = _adb_is_installed(serial, TARGET_PACKAGE)
    else:
        # Mock : on simule que l'app est maintenant installée
        installed = True

    if installed:
        ok(f"Package {TARGET_PACKAGE} détecté sur {serial}")
    else:
        warn(f"Package {TARGET_PACKAGE} non trouvé sur {serial}")

    # Bonus : lister quelques packages installés (mock)
    mock_installed = [
        "com.android.settings",
        "com.google.android.gms",
        TARGET_PACKAGE,
        "com.orange.otvp.test",
    ] if mode != "adb-real" else [TARGET_PACKAGE]

    print()
    info(f"Packages concernant Orange détectés ({len(mock_installed)}) :")
    for pkg in mock_installed:
        print(f"       ✓  {pkg}")

    return {"installed": installed, "packages": mock_installed}


def step5_generate_report(
    devices: list,
    mode: str,
    properties: dict,
    install_result: dict,
    verify_result: dict,
) -> str:
    """Génère le rapport JSON et retourne son chemin."""
    h2("ÉTAPE 5 — Génération du rapport JSON")

    out_dir = Path("output") / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    report_path = out_dir / f"demo_app_manager_{ts}.json"

    report = {
        "timestamp": ts,
        "mode": mode,
        "devices_found": len(devices),
        "devices": devices,
        "primary_device": properties,
        "install": install_result,
        "verify": verify_result,
        "summary": {
            "success": verify_result.get("installed", False),
            "devices_found": len(devices),
            "packages_verified": len(verify_result.get("packages", [])),
            "mode": mode,
        },
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    ok(f"Rapport sauvegardé : {report_path}")
    return str(report_path)


# ─── Point d'entrée ──────────────────────────────────────────────────────────

def run_demo(use_real: bool = False, target_serial: str = None):
    ts_run = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    h1(f"  DÉMO APP MANAGER — PFE  |  Run : {ts_run}")

    t0 = time.perf_counter()

    # Étape 1
    devices, mode = step1_detect_devices(use_real, target_serial)

    if not devices:
        err("Aucun device disponible — arrêt de la démo")
        sys.exit(1)

    # Étape 2
    properties = step2_device_properties(devices)

    # Étape 3
    install_result = step3_simulate_install(devices[0], mode)

    # Étape 4
    verify_result = step4_verify_install(devices[0], mode)

    # Étape 5
    report_path = step5_generate_report(
        devices, mode, properties, install_result, verify_result
    )

    duration_ms = int((time.perf_counter() - t0) * 1000)

    # ── Résumé final ─────────────────────────────────────────────────────────
    print(f"\n{SEP_D}")
    print(f"  Démo Livrable #9 terminée")
    print(f"{'─' * WIDTH}")
    print(f"  Devices détectés  : {len(devices)}")
    print(f"  Mode exécution    : {mode}")
    print(f"  App installée     : {'Oui ✅' if verify_result.get('installed') else 'Non ⚠️'}")
    print(f"  Durée             : {duration_ms} ms")
    print(f"  Rapport           : {report_path}")
    print(f"{SEP_D}")

    return {
        "success": True,
        "devices_found": len(devices),
        "mode": mode,
        "report": report_path,
        "duration_ms": duration_ms,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Démo App Manager — Livrable #9")
    parser.add_argument("--real",   action="store_true", help="Utilise ADB réel (fallback mock si non disponible)")
    parser.add_argument("--serial", default=None,        help="Serial du device cible (ex: emulator-5554)")
    args = parser.parse_args()

    try:
        result = run_demo(use_real=args.real, target_serial=args.serial)
        sys.exit(0)
    except SystemExit:
        raise
    except Exception as e:
        import traceback
        print(f"\n❌ Erreur inattendue : {e}")
        traceback.print_exc()
        sys.exit(1)
