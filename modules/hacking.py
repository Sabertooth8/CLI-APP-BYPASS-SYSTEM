def xss_test(cmd):
    parts = cmd.split()
    if len(parts) < 2:
        print("Usage: xss [url]")
        return

    url = parts[1]
    payload = "<script>alert(1)</script>"
    print(f"[XSS Test] Target: {url}")
    print(f"[Payload] Injected: {payload}")
    print("[Note] Ini simulasi. Untuk real exploit, hubungkan ke requests/curl.")
