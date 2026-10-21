import multiprocessing as mp
import time
import numpy as np


def simulate_weather_data(region_id):
    
    np.random.seed(region_id)
    data_points = np.random.normal(loc=30, scale=5, size=1_000_000)
    
    
    avg_temp = np.mean(data_points)
    extreme_count = np.sum(data_points > 38)
    
    return {
        'region_id': region_id,
        'avg_temp': round(avg_temp, 2),
        'extreme_events': int(extreme_count)
    }

if __name__ == '__main__':
    regions = list(range(1, 9)) # 8 Wilayah lokal
    print(f"--- Memulai Simulasi HPC untuk {len(regions)} Wilayah ---")
    
    start_time = time.time()
    
    
    num_cores = mp.cpu_count()
    print(f"Menggunakan {num_cores} CPU Cores secara paralel...")
    
    with mp.Pool(processes=num_cores) as pool:
        results = pool.map(simulate_weather_data, regions)
        
    end_time = time.time()
    
    print("\n--- Hasil Analisis Simulasi HPC ---")
    for res in results:
        print(f"Wilayah {res['region_id']}: Suhu Rata-rata = {res['avg_temp']}°C, Kejadian Ekstrem = {res['extreme_events']}")
        
    print(f"\nWaktu Eksekusi Total dengan HPC: {end_time - start_time:.4f} detik")