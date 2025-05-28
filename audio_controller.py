from pycaw.api.endpointvolume import IAudioEndpointVolume
from pycaw.pycaw import AudioUtilities, AudioDevice, EDataFlow, ERole
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import subprocess


def list_audio_sessions():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process:
            print(f"{session.Process.name()}")


def list_output_device_type():
    device = AudioUtilities.GetSpeakers()
    print(f"Got default output device object: {device}")


def print_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    print(f"Current system volume: {round(current_volume * 100)}%")


def list_audio_devices():
    cmd = ['powershell', '-Command', 'Get-AudioDevice -List']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().splitlines()


def set_audio_device(name):
    cmd = ['powershell', '-Command', f'Set-AudioDevice -Name "{name}"']
    subprocess.run(cmd)
