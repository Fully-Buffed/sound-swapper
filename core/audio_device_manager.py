import subprocess

# Manages system audio output devices using PowerShell's AudioDeviceCmdlets module.
class AudioDeviceManager:

    # Returns a list of all active output (Playback) device names.
    # Uses PowerShell to query audio devices and filters for Playback type only.
    def list_devices(self):

        try:
            # PowerShell command to get all playback devices and return only their names
            command = (
                'Get-AudioDevice -List | '
                'Where-Object { $_.Type -eq "Playback" } | '
                'ForEach-Object { $_.Name }'
            )

            # Run the PowerShell command from Python
            result = subprocess.run(
                ['powershell', '-Command', command],
                capture_output=True,  # Capture the output instead of printing it to the console
                text=True,            # Decode output as text (not bytes)
                check=True            # Raise an exception on non-zero exit
            )

            # Split result into lines, remove empty ones
            devices = result.stdout.strip().splitlines()
            return [d for d in devices if d.strip()]

        except subprocess.CalledProcessError as e:
            print(f"Error listing devices: {e}")
            return []

    # Sets the specified device as the default output device using its name.
    def set_default_device(self, name):

        try:
            # Build the PowerShell command string
            command = f'Set-AudioDevice -Name "{name}"'

            # Run the command to set the default device
            subprocess.run(['powershell', '-Command', command], check=True)

            print(f"Switched to device: {name}")

        except subprocess.CalledProcessError as e:
            print(f"Failed to switch device: {e}")

    # Returns the name of the current default output (Playback) device.
    def get_current_device(self):

        try:
            command = (
                'Get-AudioDevice -Playback | Select-Object -ExpandProperty Name'
            )
            result = subprocess.run(
                ['powershell', '-Command', command],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error getting current device: {e}")
            return None
