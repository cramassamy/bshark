import numpy as np
import sounddevice as sd

frequency = 440 #Hz the played note (LA du téléphone)
fs = 44100  # 44100 samples per second (fréquence audible)
seconds = 3  # Note duration in seconds
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, int(seconds * fs), False)
# Generate a frequency Hz sine wave
note = np.sin(frequency * t * 2 * np.pi)
# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)
# Start playback
sd.play(audio, fs) 
# Wait for playback to finish before exiting
sd.wait()
