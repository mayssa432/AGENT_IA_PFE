import os
import subprocess
from typing import Optional


class AppInstaller:
    """Installation et gestion d'applications mobiles sur Android."""

    def __init__(self, adb_path: str = None):
        self.adb_path = adb_path or os.getenv("ADB_PATH", "adb")

    def _run_adb(self, args, device_serial: Optional[str] = None) -> str:
        cmd = [self.adb_path]
        if device_serial:
            cmd += ["-s", device_serial]
        cmd += args
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return result.decode("utf-8", errors="ignore").strip()

    def install_apk(self, apk_path: str, device_serial: Optional[str] = None, replace: bool = True) -> str:
        if not os.path.exists(apk_path):
            raise FileNotFoundError(f"APK introuvable : {apk_path}")

        args = ["install"]
        if replace:
            args.append("-r")
        args.append(apk_path)
        return self._run_adb(args, device_serial=device_serial)

    def uninstall_app(self, package_name: str, device_serial: Optional[str] = None) -> str:
        return self._run_adb(["uninstall", package_name], device_serial=device_serial)

    def is_app_installed(self, package_name: str, device_serial: Optional[str] = None) -> bool:
        output = self._run_adb(["shell", "pm", "list", "packages", package_name], device_serial=device_serial)
        return package_name in output

    def launch_app(self, package_name: str, activity_name: str, device_serial: Optional[str] = None) -> str:
        return self._run_adb(
            ["shell", "am", "start", "-n", f"{package_name}/{activity_name}"],
            device_serial=device_serial
        )
