import os
import subprocess
import time
from typing import Optional


class AppLauncher:
    """Lancement, fermeture et gestion d'état d'applications Android."""

    def __init__(self, adb_path: str = None):
        self.adb_path = adb_path or os.getenv("ADB_PATH", "adb")

    def _run_adb(self, args: list, device_serial: Optional[str] = None) -> str:
        cmd = [self.adb_path]
        if device_serial:
            cmd += ["-s", device_serial]
        cmd += args
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return result.decode("utf-8", errors="ignore").strip()

    def launch(
        self,
        package_name: str,
        activity_name: str,
        device_serial: Optional[str] = None,
        wait_seconds: float = 2.0,
    ) -> str:
        """Lance une application et attend qu'elle soit au premier plan."""
        output = self._run_adb(
            ["shell", "am", "start", "-n", f"{package_name}/{activity_name}"],
            device_serial=device_serial,
        )
        time.sleep(wait_seconds)
        return output

    def force_stop(self, package_name: str, device_serial: Optional[str] = None) -> str:
        """Force l'arrêt d'une application."""
        return self._run_adb(
            ["shell", "am", "force-stop", package_name],
            device_serial=device_serial,
        )

    def is_running(self, package_name: str, device_serial: Optional[str] = None) -> bool:
        """Vérifie si l'application est en cours d'exécution."""
        output = self._run_adb(
            ["shell", "pidof", package_name],
            device_serial=device_serial,
        )
        return bool(output.strip())

    def clear_app_data(self, package_name: str, device_serial: Optional[str] = None) -> str:
        """Efface les données de l'application (état propre)."""
        return self._run_adb(
            ["shell", "pm", "clear", package_name],
            device_serial=device_serial,
        )

    def capture_logcat(
        self,
        device_serial: Optional[str] = None,
        lines: int = 200,
        tag_filter: Optional[str] = None,
    ) -> str:
        """Capture les dernières lignes de logcat."""
        args = ["logcat", "-d", "-t", str(lines)]
        if tag_filter:
            args += ["-s", tag_filter]
        return self._run_adb(args, device_serial=device_serial)

