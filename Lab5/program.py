import pandas as pd
import numpy as np
from multiprocessing import Pool, cpu_count

def process_chunk(chunk):
    """
    Обробка окремого фрагмента даних.
    """
    chunk['processed'] = chunk['value'] ** 2  # Наприклад, піднесення до квадрата
    return chunk

def parallel_processing(data, chunk_size=10000):
    """
    Оптимізована обробка великих наборів даних за допомогою багатопроцесорності.
    """
    num_workers = cpu_count()
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    with Pool(num_workers) as pool:
        results = pool.map(process_chunk, chunks)
    
    return pd.concat(results)

# Приклад використання:
if __name__ == "__main__":
    # Генеруємо великий набір даних
    data_size = 1000000  # 1 млн записів
    df = pd.DataFrame({'value': np.random.rand(data_size)})
    
    # Обробка
    processed_df = parallel_processing(df)
    print(processed_df.head())
