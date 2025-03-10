import pandas as pd
import numpy as np
import time

# Створимо випадковий DataFrame для енергетичних даних
np.random.seed(42)
n = 1_000_000
df = pd.DataFrame({
    'hour': np.random.randint(0, 24, n),
    'day_of_week': np.random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], n),
    'category': np.random.choice(['Residential', 'Commercial', 'Industrial'], n),
    'energy_consumption': np.random.uniform(50, 500, n)
})

print(df.head())

# Оптимізовані обчислення через pd.eval()
start = time.time()
result = pd.eval("df['energy_consumption'] * 1.1")  # Наприклад, підняття тарифу на 10%
print(f"Eval computation time: {time.time() - start:.4f} seconds")

# Альтернативний підхід без eval
start = time.time()
result = df['energy_consumption'] * 1.1
print(f"Standard computation time: {time.time() - start:.4f} seconds")

# Складний вираз з eval
start = time.time()
complex_result = pd.eval(
    "df['energy_consumption'] * 1.1 + df['hour'] * 0.5 - (df['day_of_week'] == 'Sun') * 100"
)
print(f"Complex eval computation time: {time.time() - start:.4f} seconds")
