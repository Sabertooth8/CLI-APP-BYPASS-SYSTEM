import json
import os

def search(keyword):
    keyword = keyword.lower()
    hasil = f"[🔎] Hasil Pencarian untuk: \"{keyword}\"\n\n"

    # Search di TASK
    task_file = "data/tasks.json"
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            tasks = json.load(f)
        task_matches = [
            f"- {t['judul']} - {t['deskripsi']}"
            for t in tasks
            if keyword in t['judul'].lower() or keyword in t['deskripsi'].lower()
        ]
        if task_matches:
            hasil += "TASK:\n" + "\n".join(task_matches) + "\n\n"
    
    # Search di NOTE
    note_file = "data/notes.json"
    if os.path.exists(note_file):
        with open(note_file, "r") as f:
            notes = json.load(f)
        note_matches = [
            f"- {n['judul']} → {n['isi'][:80]}..."
            for n in notes
            if keyword in n['judul'].lower() or keyword in n['isi'].lower()
        ]
        if note_matches:
            hasil += "CATATAN:\n" + "\n".join(note_matches) + "\n\n"

    if "TASK" not in hasil and "CATATAN" not in hasil:
        hasil += "[📭] Tidak ada hasil ditemukan."

    return hasil

def handle(cmd):
    print("[Mode Pencarian]")
    kata = input("Masukkan kata kunci: ").strip()
    print(search(kata))
