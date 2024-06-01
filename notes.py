import numpy as np
import sounddevice as sd

def sound(x,z):
	frequency = x # the played note
	fs = 44100  # 44100 samples per second
	seconds = z  # Note duration in seconds
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

C=32.70
D=36.71
E=41.20
F=43.65
G=49.00
A=55.00
B=61.74
octave=2 * 4
sound(C * octave, 1)
sound(D * octave, 1)
sound(E * octave, 1)
sound(F * octave, 1)
sound(G * octave, 1)
sound(A * octave, 1)
sound(B * octave, 1)
sound(C * (octave * 2), 1)
