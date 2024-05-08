import soundcard as sc
import numpy as np
import time
# import keyboard
import pyautogui

# Define constants
CHUNK = 1024  # Number of frames per buffer
SILENCE_THRESHOLD = -40 # Adjust this threshold according to your environment
SILENCE_LIMIT = 3  # Silence limit in seconds

def list_audio_devices():
    print("Available audio devices:")
    for i, dev in enumerate(sc.all_microphones(include_loopback=True)):
        print(f"Device {i}: {dev.name}")

def calculate_rms(data):
    return np.sqrt(np.mean(np.square(data)))

def listen_microphone(device_index):
    mic = sc.all_microphones(include_loopback=True)[device_index]

    print("Listening...")
    silence_counter = 0

    with mic.recorder(samplerate=44100, blocksize=CHUNK) as recorder:
        while True:
            data = recorder.record(numframes=CHUNK)
            rms = calculate_rms(data)

            # Calculate volume level in dBFS (decibels relative to full scale)
            volume_level = 20 * np.log10(rms) if rms > 0 else -120

            # print(f"Volume level: {volume_level:.2f} dBFS")

            # if rms < SILENCE_THRESHOLD:
            if volume_level < SILENCE_THRESHOLD:
                silence_counter += 1
            else:
                silence_counter = 0

            if silence_counter > int(SILENCE_LIMIT * 44100 / CHUNK):
                print(f"Silence detected for {SILENCE_LIMIT} seconds. Exiting.")
                break

if __name__ == "__main__":
    list_audio_devices()
    # device_index = int(input("Enter the index of the desired audio input device: "))
    device_index = 27
    print("Device selected:", device_index)
    listen_microphone(device_index)
    print("Goodbye!")
    pyautogui.hotkey("alt", "f4")
