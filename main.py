import androidhelper
import time
import requests

droid = androidhelper.Android()

def toggle_airplane_mode():
    # Memeriksa status mode pesawat saat ini
    is_enabled = droid.checkAirplaneMode().result
    # Mengaktifkan atau menonaktifkan mode pesawat
    droid.toggleAirplaneMode(not is_enabled)
    # Memberikan waktu untuk perubahan status
    time.sleep(3)
    # Memeriksa kembali status mode pesawat
    new_status = droid.checkAirplaneMode().result
    return new_status

def check_internet_connection():
    # Memeriksa koneksi internet
    result = droid.checkNetworkConnection().result
    return result

def check_internet_speed():
    try:
        # Mengukur kecepatan unduh dengan mengunduh file kecil
        start_time = time.time()
        response = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', stream=True)
        total_time = time.time() - start_time
        file_size = int(response.headers.get('content-length', 0))
        speed = file_size / total_time / 1024  # kecepatan dalam KB/s
        return speed
    except Exception as e:
        print(f"Error saat mengukur kecepatan internet: {e}")
        return 0

if __name__ == "__main__":
    while True:
        current_status = toggle_airplane_mode()
        print(f"Mode pesawat sekarang {'aktif' jika current_status else 'nonaktif'}")
        if check_internet_connection():
            speed = check_internet_speed()
            print(f"Koneksi internet ditemukan dengan kecepatan {speed:.2f} KB/s.")
            if speed > 0:
                print("Menghentikan proses.")
                break
        else:
            print("Tidak ada koneksi internet. Mengulangi proses...")
