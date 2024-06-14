import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.io import wavfile
from scipy.fft import fft
import numpy as np


# Configuración de la grabación
duration = 2  # Duración de la grabación en segundos
sample_rate = 44100  # Frecuencia de muestreo en Hz
channels = 1  # Número de canales (1 para mono, 2 para estéreo)

print("Inicia Esfera")

for i in range(0,50):
    print(f"Grabando esfera {i}...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()
    
    
    print("Grabacion finalizada.")
    
    file_name = f"muestra#{i}.wav"
    wav.write(file_name,sample_rate, audio)
    

print("inicia Cubo")

for i in range(0,50):
    print(f"Grabando cubo {i}...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()
    
    print("Grabacion finalizada.")
    
    file_name = f"muestrac#{i}.wav"
    wav.write(file_name,sample_rate, audio)

