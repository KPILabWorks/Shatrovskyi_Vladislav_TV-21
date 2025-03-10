import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt
from scipy.fft import fft, fftfreq

# Генерація синтетичних даних споживання енергії (випадковий тренд + гармоніки)
np.random.seed(42)
time = np.arange(0, 1000)
energy_consumption = (50 + 10 * np.sin(2 * np.pi * time / 200)  # сезонний тренд
                      + 5 * np.sin(2 * np.pi * time / 50)        # короткотермінові коливання
                      + np.random.normal(0, 2, len(time)))       # шум

# Візуалізація часових рядів
plt.figure(figsize=(10, 5))
plt.plot(time, energy_consumption, label='Energy Consumption')
plt.title('Synthetic Energy Consumption Time Series')
plt.legend()
plt.show()

# Вейвлет-перетворення (Discrete Wavelet Transform - DWT)
wavelet = 'db4'
coeffs = pywt.wavedec(energy_consumption, wavelet, level=4)

# Реконструкція сигналу для кожного рівня
plt.figure(figsize=(12, 8))
for i, coef in enumerate(coeffs):
    plt.subplot(len(coeffs), 1, i + 1)
    plt.plot(coef)
    plt.title(f'Wavelet Level {i} (db4)')
plt.tight_layout()
plt.show()

# Фур'є-аналіз (перетворення Фур'є)
N = len(time)
T = 1.0  # припустимо, 1 одиниця часу між вимірами
fft_values = fft(energy_consumption)
frequencies = fftfreq(N, T)

# Візуалізація частотного спектра
plt.figure(figsize=(10, 5))
plt.plot(frequencies[:N // 2], np.abs(fft_values[:N // 2]))
plt.title('Fourier Transform Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
