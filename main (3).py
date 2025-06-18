import csv
from datetime import datetime

def mark_attendance(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    # Cutoff time
    cutoff_time = datetime.strptime("09:00:00", "%H:%M:%S")
    status = "Hadir Awal" if now.time() <= cutoff_time.time() else "Lambat Hadir"

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, current_date, current_time, status])

    print(f"{name}, Kehadiran anda telah direkodkan sebagai '{status}' pada pukul {current_time} pada hari {current_date}.")

def view_attendance():
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            print("\n📋 Rekod Kehadiran:")
            print("-" * 50)
            for row in reader:
                print(f" {row[0]} | {row[1]} | {row[2]} | {row[3]}")
    except FileNotFoundError:
        print("Tiada rekod kehadiran dijumpai")

def main():
    print("🎓 SISTEM KEHADIRAN PYTHON")
    print("==========================")
    while True:
        print("\n1. Daftar Kehadiran")
        print("2. Lihat Kehadiran")
        print("3. Eksport Senarai Kehadiran dan Keluar")

        choice = input("Pilih antara pilihan di bawah dengan 1,2 atau 3: ")

        if choice == "1":
            name = input("Masukkan nama anda: ").strip()
            if name:
                mark_attendance(name)
            else:
                print("Nama wajib diisi")
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Sedang keluar. Sekian terima kasih")
            break
        else:
            print("Pilihan salah X. Sila cuba sekali lagi")

if __name__ == "__main__":
    main()
