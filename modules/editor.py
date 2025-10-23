def write_file(filename):
    print(f"[📝 Write Mode] Sedang edit: {filename}")
    print("Ketik isi file lo di bawah. Ketik `:wq` di baris baru buat simpan.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == ":wq":
            break
        lines.append(line)

    try:
        with open(filename, "w") as f:
            f.write("\n".join(lines))
        print(f"[+] File {filename} berhasil disimpan.")
    except Exception as e:
        print(f"[!] Gagal nyimpan file: {e}")
