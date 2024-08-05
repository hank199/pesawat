import os
import time

def toggle_airplane_mode():
    # Mengaktifkan mode pesawat
    os.system("su -c 'settings put global airplane_mode_on 1'")
    os.system("su -c 'am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true'")
    time.sleep(3)
    # Menonaktifkan mode pesawat
    os.system("su -c 'settings put global airplane_mode_on 0'")
    os.system("su -c 'am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false'")

def check_internet_connection():
    response = os.system("ping -c 1 google.com")
    return response == 0

if __name__ == "__main__":
    while True:
        toggle_airplane_mode()
        if check_internet_connection():
            print("Koneksi internet ditemukan. Menghentikan proses.")
            break
        else:
            print("Tidak ada koneksi internet. Mengulangi proses...")
