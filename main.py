import os
import os
import sys
from modules import study_mode
import time
import random


def typewriter(text, delay=0.0015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(text=None):
    phrases = [
        "Menyambungkan ke dunia bawah tanah...",
        "Sinkronisasi dengan terminal Ponyoo...",
        "Membuka jalur bypass sistem sekolah...",
        "Menstabilkan kepribadian digital...",
        "Menyalakan protokol glitch mode..."
    ]
    text = text or random.choice(phrases)

    typewriter(f"\033[1;36m{text}\033[0m", delay=0.04)
    for i in range(1, 21):
        time.sleep(0.04)
        filled = "#" * i
        empty = " " * (20 - i)
        percent = f"{i*5}%".rjust(4)
        print(f"\r[\033[1;32m{filled}\033[0m{empty}] {percent}", end="")
    print("\n\033[1;32m[✔] Sistem N0Hfacee siap digunakan.\033[0m")
    time.sleep(0.5)
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    loading_bar()
    ascii = r"""
███╗░░██╗░█████╗░██╗░░██╗███████╗░█████╗░░█████╗░███████╗███████╗
████╗░██║██╔══██╗██║░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██╔██╗██║██║░░██║███████║█████╗░░███████║██║░░╚═╝█████╗░░█████╗░░
██║╚████║██║░░██║██╔══██║██╔══╝░░██╔══██║██║░░██╗██╔══╝░░██╔══╝░░
██║░╚███║╚█████╔╝██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗███████╗
╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝
"""
    typewriter(ascii, delay=0.0015)
def write_mode():
    tprint("[✏️] Masuk ke mode edit Python.")
    tprint("[!] Ketik `q` di baris baru untuk keluar dari mode edit.")
    lines = []
    while True:
        line = input("... ")
        if line.strip().lower() == 'q':
            break
        lines.append(line)
    code = "\n".join(lines)
    try:
        exec(code)
    except Exception as e:
        tprint(f"[!] Error saat eksekusi: {e}")

# === ANSI COLOR WRAPPER ===
def cprint(text, color="white"):
    colors = {
        "black": "30", "red": "31", "green": "32",
        "yellow": "33", "blue": "34", "magenta": "35",
        "cyan": "36", "white": "37"
    }
    code = colors.get(color.lower(), "37")
    print(f"\033[1;{code}m{text}\033[0m")

# === WHOAMI ===
def whoami():
    ascii_logo = r"""
⣿⣿⡻⠿⣳⠸⢿⡇⢇⣿⡧⢹⠿⣿⣿⣿⣿⣾⣿⡇⣿⣿⣿⣿⡿⡐⣯⠁⠄⠄
⠟⣛⣽⡳⠼⠄⠈⣷⡾⣥⣱⠃⠣⣿⣿⣿⣯⣭⠽⡇⣿⣿⣿⣿⣟⢢⠏⠄ ⠄
⢠⡿⠶⣮⣝⣿⠄⠄⠈⡥⢭⣥⠅⢌⣽⣿⣻⢶⣭⡿⠿⠜⢿⣿⣿⡿⠁⠄⠄.
⠄⣼⣧⠤⢌⣭⡇⠄⠄⠄⠭⠭⠭⠯⠴⣚⣉⣛⡢⠭⠵⢶⣾⣦⡍⠁⠄⠄⠄⠄
⠄⣿⣷⣯⣭⡷⠄⠄⢀⣀⠩⠍⢉⣛⣛⠫⢏⣈⣭⣥⣶⣶⣦⣭⣛⠄⠄⠄⠄⠄
⢀⣿⣿⣿⡿⠃⢀⣴⣿⣿⣿⣎⢩⠌⣡⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄⠄
⢸⡿⢟⣽⠎⣰⣿⣿⣿⣿⣿⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠄
⣰⠯⣾⢅⣼⣿⣿⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄
⢰⣄⡉⣼⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄
⢯⣌⢹⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
⢸⣇⣽⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
⢸⣟⣧⡻⣿⣿⣿⣿⣿⣿⣿⣧⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
⠈⢹⡧⣿⣸⠿⢿⣿⣿⣿⣿⡿⠗⣈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄
⠄⠘⢷⡳⣾⣷⣶⣶⣶⣶⣶⣾⣿⣿⢀⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄
⠄⠄⠈⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄
    """

    info = [   
        "\033[1;35mPonyoo - Bot\033[0m",
        "\033[1;35mN0Hfacee Terminal v3.5-beta\033[0m",
        "-----------------------------",
        "\033[1;32mUSERNAME   : Samuel\033[0m",
        "\033[1;36mCODE       : N0Hfacee\033[0m",
        "\033[1;35mALIAS      : Ponyoo\033[0m",
        "\033[1;33mROLE       : Glitch in the Matrix\033[0m",
        "\033[1;34mSYSTEM     : N0HF-OS v3.0-beta\033[0m",
        "\033[1;32mSTATE      : Flow Zone Active\033[0m",
        "\033[1;36mFOCUS      : 88% — Syntax Awareness Boosted\033[0m",
        "\033[1;31mTHREAT     : Moderate — Guru Killer Sensor Active\033[0m",
        "\033[1;33mLOCATION   : ~/Desktop/N0Hfacee-local\033[0m",
        "\033[1;31mQUOTE      : \"Rewrite. Don't obey.\"\033[0m"
    ]

    logo_lines = ascii_logo.strip("\n").split("\n")
    max_logo_len = max(len(line) for line in logo_lines)

    for i in range(max(len(logo_lines), len(info))):
        logo = logo_lines[i] if i < len(logo_lines) else " " * max_logo_len
        text = info[i] if i < len(info) else ""
        tprint(f"{logo}   {text}")

# === KILL COMMAND ===
def guru_killer_mode():
    cprint("[🚨] Sensor menangkap pergerakan mencurigakan...", "red")
    cprint("[💀] Guru killer terdeteksi.", "red")
    cprint("[💨] Sistem auto-eject diaktifkan...", "yellow")
    cprint("👋 Semoga lo selamat, glitch terakhir...\n", "magenta")
    sys.exit()

def tprint(text, delay=0.01):
    typewriter(text, delay)

def input_typewriter(prompt, delay=0.03):
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()
    

def main():
    os.system("clear")
    banner()
    tprint("Ketik `help` untuk melihat daftar perintah.\n")

    while True:
        try:
            cmd = input_typewriter("N0Hfacee >> ").strip().lower()
            
            if cmd == "exit":
                tprint("🛑 Keluar dari sistem. Sampai jumpa, Agent S.")
                break
            elif cmd == "clear":
                os.system("clear")
                banner()
            elif cmd == "help":
                tprint("""
[DAFTAR PERINTAH]
clear           → Bersihkan layar terminal
exit            → Keluar dari terminal N0Hfacee
help            → Lihat perintah yang tersedia
whoami          → Tampilkan informasi pengguna
kill            → Mode guru killer (auto-eject)
write           → Mode edit Python langsung
mode belajar    → Masuk ke STUDY MODE (jadwal, task, catatan)
""")
            elif cmd == "write":
                write_mode()
            elif cmd == "whoami":
                whoami()
            elif cmd == "kill":
                guru_killer_mode()
            elif cmd == "mode belajar":
                study_mode.start()
            else:
                tprint("[!] Perintah tidak dikenal. Gunakan `help` untuk melihat daftar perintah.")
        except KeyboardInterrupt:
            tprint("\n[⚠️] Gunakan perintah `exit` untuk keluar dengan aman.")

if __name__ == "__main__":
    main()

