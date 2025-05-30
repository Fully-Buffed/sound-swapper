import os
import json


class ProfileManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.profiles = {}  # for storing loaded profile data

    def load_profiles(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                data = json.load(f)
                self.profiles = data.get("profiles", {})
        else:
            # Create default structure
            self.profiles = {
                "device_1": None,
                "device_2": None
            }
            self.save_profiles()

    def save_profiles(self):
        with open(self.config_path, "w") as f:
            json.dump({"profiles": self.profiles}, f, indent=2)

    def set_profile(self, slot, device_name, eq_command=None):
        self.profiles[slot] = {
            "device": device_name,
            "eq_command": eq_command
        }
        self.save_profiles()

    def get_device(self, slot):
        profile = self.profiles.get(slot)
        if profile:
            return profile.get("device")
        return None

    def get_eq_command(self, slot):
        profile = self.profiles.get(slot)
        if profile:
            return profile.get("eq_command")
        return None
