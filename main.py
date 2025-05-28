from core.audio_device_manager import AudioDeviceManager
from audio_controller import print_system_volume  # just this one for now

if __name__ == "__main__":
    print("\nAvailable Output Devices:")
    manager = AudioDeviceManager()
    devices = manager.list_devices()

    for i, device in enumerate(devices):
        print(f"{i + 1}. {device}")

    current = manager.get_current_device()
    print(f"\nCurrent Audio Device: {current}\n")
    print_system_volume()