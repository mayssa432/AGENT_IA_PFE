import os
import subprocess
from typing import List, Optional


class DeviceManager:
    """Gestion des devices Android via ADB."""

    def __init__(self, adb_path: str = None):
        self.adb_path = adb_path or os.getenv("ADB_PATH", "adb")

    def _run_adb(self, args: List[str], device_serial: Optional[str] = None) -> str:
        cmd = [self.adb_path]
        if device_serial:
            cmd += ["-s", device_serial]
        cmd += args
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return result.decode("utf-8", errors="ignore").strip()

    def list_devices(self) -> List[str]:
        output = self._run_adb(["devices"])
        lines = [line.strip() for line in output.splitlines()[1:] if line.strip()]
        devices = []
        for line in lines:
            parts = line.split() 
            if len(parts) >= 2 and parts[1] == "device":
                devices.append(parts[0])
        return devices

    def is_device_connected(self, device_serial: str) -> bool:
        return device_serial in self.list_devices()

    def shell(self, command: str, device_serial: Optional[str] = None) -> str:
        return self._run_adb(["shell", command], device_serial=device_serial)

    def get_device_properties(self, device_serial: Optional[str] = None) -> dict:
        output = self.shell("getprop", device_serial=device_serial)
        properties = {}
        for line in output.splitlines():
            if ": " in line:
                key, value = line.split(": ", 1)
                properties[key.strip()] = value.strip()
        return properties

    def get_device_model(self, device_serial: Optional[str] = None) -> Optional[str]:
        props = self.get_device_properties(device_serial)
        return props.get("ro.product.model")

    def get_android_version(self, device_serial: Optional[str] = None) -> Optional[str]:
        props = self.get_device_properties(device_serial)
        return props.get("ro.build.version.release")
