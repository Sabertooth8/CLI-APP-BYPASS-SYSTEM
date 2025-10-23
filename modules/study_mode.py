import os
import time
from . import task, note, jadwal
from modules import search

def show_ascii_banner():
    print(r"""
  ██████ ▄▄▄█████▓ █    ██ ▓█████▄▓██   ██▓    ███▄ ▄███▓ ▒█████  ▓█████▄ ▓█████ 
▒██    ▒ ▓  ██▒ ▓▒ ██  ▓██▒▒██▀ ██▌▒██  ██▒   ▓██▒▀█▀ ██▒▒██▒  ██▒▒██▀ ██▌▓█   ▀ 
░ ▓██▄   ▒ ▓██░ ▒░▓██  ▒██░░██   █▌ ▒██ ██░   ▓██    ▓██░▒██░  ██▒░██   █▌▒███   
  ▒   ██▒░ ▓██▓ ░ ▓▓█  ░██░░▓█▄   ▌ ░ ▐██▓░   ▒██    ▒██ ▒██   ██░░▓█▄   ▌▒▓█  ▄ 
▒██████▒▒  ▒██▒ ░ ▒▒█████▓ ░▒████▓  ░ ██▒▓░   ▒██▒   ░██▒░ ████▓▒░░▒████▓ ░▒████▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░▒▓▒ ▒ ▒  ▒▒▓  ▒   ██▒▒▒    ░ ▒░   ░  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░
░ ░▒  ░ ░    ░    ░░▒░ ░ ░  ░ ▒  ▒ ▓██ ░▒░    ░  ░      ░  ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░
░  ░  ░    ░       ░░░ ░ ░  ░ ░  ░ ▒ ▒ ░░     ░      ░   ░ ░ ░ ▒   ░ ░  ░    ░   
      ░              ░        ░    ░ ░               ░       ░ ░     ░       ░  ░
                            ░      ░ ░                             ░             
""")

import sys

def loading_bar():
    steps = [
        "Initializing STUDY MODE",
        "Loading task module",
        "Loading catatan module",
        "Loading jadwal",
        "Applying anti-distraksi firewall",
        "Activating focus engine",
        "Injecting matrix shell",
        "Polishing your mindset",
        "Welcome, Agent Samuel"
    ]
    
    for i, msg in enumerate(steps):
        bar = "█" * (i + 1) + "▒" * (len(steps) - i - 1)
        sys.stdout.write(f"\r[{bar}] {msg}")
        sys.stdout.flush()
        time.sleep(0.3)

    # Clear bar
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()

def show_intro_text():
    print("\n[MODE BELAJAR DIAKTIFKAN]")
    print("Tugas sekolah tidak akan mengerjakan dirinya sendiri.")
    print("Jadilah glitch. Tapi glitch yang berprestasi.\n")
    print("Fitur yang tersedia:")
    print("1. jadwal        → Lihat jadwal sekolah")
    print("2. task          → Tambah & cek tugas")
    print("3. catatan       → Tulis / baca catatan")
    print("4. cari/search   → Cari isi catatan/materi")
    print("5. clean         → Bersihkan layar")
    print("6. help          → Lihat daftar perintah")
    print("0. out           → Keluar dari Mode Belajar\n")

def start():
    os.system("cls" if os.name == "nt" else "clear")
    show_ascii_banner()
    loading_bar()
    show_intro_text()

    while True:
        try:
            cmd = input("[STUDY MODE] >> ").strip().lower()

            if cmd == "out":
                print("📤 Selamat Beristirahat Tuan.\n")
                break
            elif cmd in ["clear", "clean"]:
                os.system("cls" if os.name == "nt" else "clear")
            elif cmd.startswith("task"):
                task.handle(cmd)
            elif cmd.startswith("catatan") or cmd.startswith("note"):
                note.handle(cmd)
            elif cmd.startswith("materi"):
                note.open_materi(cmd)
            elif cmd.startswith("jadwal"):
                jadwal.handle(cmd)
            elif cmd.startswith("cari") or cmd.startswith("search"):
                search.handle(cmd)
            elif cmd.startswith("help"):
                print("\n[DAFTAR PERINTAH MODE BELAJAR]")
                print("1. jadwal        → Lihat jadwal sekolah")
                print("2. task          → Tambah & cek tugas")
                print("3. catatan       → Tulis / baca catatan")
                print("4. cari          → Cari isi catatan/materi")
                print("5. clean         → Bersihkan layar")
                print("6. help          → Lihat daftar perintah")
                print("0. out           → Keluar dari Mode Belajar\n")
            else:
                print("[!] Perintah tidak dikenali.")
        except KeyboardInterrupt:
            print("\n[⚠️] Gunakan perintah `out` untuk keluar dari mode belajar.")
