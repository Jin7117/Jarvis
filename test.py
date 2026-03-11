import pyaudio
import wave
import time

# Mic device indices
mic_indices = [1, 5, 9, 17, 18, 19]

# Common sample rates to try
sample_rates = [44100, 48000, 16000, 22050]

# Recording settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024
RECORD_SECONDS = 5

audio = pyaudio.PyAudio()

def list_devices():
    print("Available audio devices:")
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"{i}: {info['name']} — {info['maxInputChannels']} input channels")

def record_audio(device_index, filename):
    for rate in sample_rates:
        try:
            print(f"\nTrying device {device_index} at {rate} Hz...")
            stream = audio.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=rate,
                                input=True,
                                input_device_index=device_index,
                                frames_per_buffer=CHUNK)
            frames = []
            for _ in range(0, int(rate / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)

            stream.stop_stream()
            stream.close()

            wf = wave.open(filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            print(f"Saved: {filename} at {rate} Hz")
            return True
        except OSError as e:
            print(f"Failed at {rate} Hz: {e}")
    print(f"Could not record from device {device_index}")
    return False

# Optional: list devices first
list_devices()

# Loop through mics
for idx in mic_indices:
    record_audio(idx, f"mic_{idx}.wav")
    time.sleep(1)

audio.terminate()
print("\nAll recordings done!")