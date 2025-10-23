import json
import os

NOTE_FILE = "data/notes.json"

def load_notes():
    if not os.path.exists(NOTE_FILE):
        return []
    with open(NOTE_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    os.makedirs(os.path.dirname(NOTE_FILE), exist_ok=True)
    with open(NOTE_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def tambah_note(judul, isi):
    notes = load_notes()
    notes.append({"judul": judul, "isi": isi})
    save_notes(notes)

def lihat_notes():
    notes = load_notes()
    if not notes:
        return "[📭] Tidak ada catatan."
    result = "[📚] Daftar Catatan:\n"
    for i, n in enumerate(notes, 1):
        result += f"{i}. {n['judul']}\n"
    return result

def baca_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        note = notes[index]
        return f"[📖] {note['judul']}\n{note['isi']}"
    else:
        return "[❌] Nomor catatan tidak valid."

def hapus_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        deleted = notes.pop(index)
        save_notes(notes)
        return f"[🗑️] Catatan '{deleted['judul']}' dihapus."
    else:
        return "[❌] Nomor catatan tidak valid."

def handle(cmd):
    print("[Note Mode]")
    print("1. Tambah Catatan")
    print("2. Lihat Semua Judul")
    print("3. Baca Catatan")
    print("4. Hapus Catatan")
    sub = input(">> ").strip()

    if sub == "1":
        judul = input("Judul catatan: ")
        isi = input("Isi catatan:\n")
        tambah_note(judul, isi)
        print("[✔] Catatan ditambahkan.")
    elif sub == "2":
        print(lihat_notes())
    elif sub == "3":
        print(lihat_notes())
        try:
            idx = int(input("Nomor catatan: ")) - 1
            print(baca_note(idx))
        except:
            print("[!] Input tidak valid.")
    elif sub == "4":
        print(lihat_notes())
        try:
            idx = int(input("Nomor yang mau dihapus: ")) - 1
            print(hapus_note(idx))
        except:
            print("[!] Input tidak valid.")
