from audio_controller import list_audio_sessions, list_output_device_type, print_system_volume

if __name__ == "__main__":
    print("Active Audio Sessions:")
    list_audio_sessions()
    list_output_device_type()
    print_system_volume()

