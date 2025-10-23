import json
import os
from datetime import datetime

JADWAL_FILE = "data/jadwal.json"

def load_jadwal():
    if not os.path.exists(JADWAL_FILE):
        return {}
    with open(JADWAL_FILE, "r") as f:
        return json.load(f)

def tampilkan_hari(hari):
    jadwal = load_jadwal()
    pelajaran = jadwal.get(hari.lower(), [])
    if not pelajaran:
        return f"[📭] Tidak ada jadwal untuk {hari.title()}."
    result = f"[📅] Jadwal {hari.title()}:\n"
    for i, pel in enumerate(pelajaran, 1):
        result += f"{i}. {pel}\n"
    return result

def tampilkan_semua():
    jadwal = load_jadwal()
    if not jadwal:
        return "[❌] Jadwal kosong."
    result = "[🗓️] Jadwal Mingguan:\n"
    for hari, daftar in jadwal.items():
        result += f"\n{hari.title()}:\n"
        for i, pel in enumerate(daftar, 1):
            result += f"  {i}. {pel}\n"
    return result

def tampilkan_hari_ini():
    hari_ini = datetime.now().strftime("%A").lower()
    mapping = {
        "monday": "senin",
        "tuesday": "selasa",
        "wednesday": "rabu",
        "thursday": "kamis",
        "friday": "jumat",
        "saturday": "sabtu",
        "sunday": "minggu"
    }
    hari_indo = mapping.get(hari_ini, "senin")
    return tampilkan_hari(hari_indo)

def handle(cmd):
    print("[Jadwal Mode]")
    print("1. Lihat Jadwal Hari Ini")
    print("2. Lihat Semua Jadwal")
    print("3. Lihat Jadwal Hari Tertentu")
    sub = input(">> ").strip()

    if sub == "1":
        print(tampilkan_hari_ini())
    elif sub == "2":
        print(tampilkan_semua())
    elif sub == "3":
        hari = input("Hari apa? ").strip()
        print(tampilkan_hari(hari))
