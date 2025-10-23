import subprocess

def handle(cmd):
    parts = cmd.split()
    if len(parts) < 2:
        print("Usage: run filename")
        return

    filename = parts[1]
    try:
        if filename.endswith(".py"):
            subprocess.run(["python3", filename])
        elif filename.endswith(".js"):
            subprocess.run(["node", filename])
        elif filename.endswith(".sh"):
            subprocess.run(["bash", filename])
        else:
            print("[!] File tidak dikenali.")
    except Exception as e:
        print("[!] Error:", e)
