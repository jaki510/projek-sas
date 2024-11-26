import time
from datetime import datetime

def reminder_system():
    print("Sistem Pengingat Sederhana")
    
    while True:

        reminder_time_str = input("Masukkan waktu pengingat (format HH:MM, contoh 14:30): ")
        
        try:
            reminder_time = datetime.strptime(reminder_time_str, "%H:%M").time()
            break  
        except ValueError:
            print("Waktu yang dimasukkan tidak valid. Harap menggunakan format HH:MM.")

    reminder_message = input("Masukkan pesan pengingat: ")
    
    print(f"Pengingat telah diset untuk {reminder_time.strftime('%H:%M')}.")
    print("Sistem akan memantau waktu...\n")
    
    while True:
        current_time = datetime.now().time()
        
        if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
            print(f"\nPengingat: {reminder_message}")
            break  
        time.sleep(1)  

if __name__ == "__main__":
    reminder_system()
