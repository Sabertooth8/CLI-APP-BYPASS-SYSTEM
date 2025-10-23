import json
import os

TASK_FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    os.makedirs(os.path.dirname(TASK_FILE), exist_ok=True)
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def tambah_task(judul, deskripsi=""):
    tasks = load_tasks()
    tasks.append({"judul": judul, "deskripsi": deskripsi})
    save_tasks(tasks)

def lihat_task():
    tasks = load_tasks()
    if not tasks:
        return "[📭] Tidak ada task saat ini."
    result = "[📋] Daftar Task:\n"
    for i, t in enumerate(tasks, 1):
        result += f"{i}. {t['judul']} - {t['deskripsi']}\n"
    return result

def hapus_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        save_tasks(tasks)
        return f"[🗑️] Task '{deleted['judul']}' berhasil dihapus."
    else:
        return "[❌] Nomor task tidak valid."

def handle(cmd):
    print("[Task Mode]")
    print("1. Tambah Task")
    print("2. Lihat Task")
    print("3. Hapus Task")
    sub = input(">> ").strip()

    if sub == "1":
        judul = input("Judul tugas: ")
        desk = input("Deskripsi (opsional): ")
        tambah_task(judul, desk)
        print("[✔] Task ditambahkan.")
    elif sub == "2":
        print(lihat_task())
    elif sub == "3":
        print(lihat_task())
        try:
            idx = int(input("Nomor task yang mau dihapus: ")) - 1
            print(hapus_task(idx))
        except:
            print("[!] Input tidak valid.")
