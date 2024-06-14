import scipy.io.wavfile as wav
from scipy.io import wavfile
from scipy.fft import fft
import sounddevice as sd
import numpy as np
import fft



# Configuración de la grabación
duration = 2  # Duración de la grabación en segundos
sample_rate = 44100  # Frecuencia de muestreo en Hz
channels = 1  # Número de canales (1 para mono, 2 para estéreo)

print(f"Grabando...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
sd.wait()

print("Grabacion finalizada.")

file_name = f"muestra_comparacion.wav"
wav.write(file_name,sample_rate, audio)
 
fft_aquitoy = fft.calculate_fft(file_name)
p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = fft.split(fft_aquitoy)
em1 = fft.calculate_energy(p1)
em2 = fft.calculate_energy(p2)
em3 = fft.calculate_energy(p3)
em4 = fft.calculate_energy(p4)
em5 = fft.calculate_energy(p5)
em6 = fft.calculate_energy(p6)
em7 = fft.calculate_energy(p7)
em8 = fft.calculate_energy(p8)
em9 = fft.calculate_energy(p9)
em10 = fft.calculate_energy(p10)
l=[em1, em2, em3, em4, em5, em6, em7, em8, em9, em10]
print("holi")
print(l)
resp = fft.respuesta(em1, em2, em3, em4, em5, em6, em7, em8, em9, em10)
print("Has dicho con mucho cuidado ")
print(resp)




