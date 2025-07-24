import subprocess
import time
# from wifitest import ssid
ssid = "Sevinch"
def get_wifi_names():
    result = subprocess.run(["netsh", "wlan", "show", "networks", "mode=bssid"],
                            capture_output=True, text=True, encoding="utf-8")
    lines = result.stdout.splitlines()
    ssids = set()

    for line in lines:
        if "SSID" in line and " : " in line:
            parts = line.split(" : ")
            if len(parts) > 1:
                ssid = parts[1].strip()
                if ssid and ssid.lower() != '':  # Bo‘sh SSIDlar chiqarilmaydi
                    ssids.add(ssid)
    return ssids

try:
    while True:
        print("\n📡 Yaqin atrofdagi Wi-Fi tarmoqlar:")
        wifi_names = get_wifi_names()
        print(wifi_names)
        if ssid not in wifi_names:
            print("\n❌ Dastur to‘xtatildi.")
            task_name = "wifitest.py"
            subprocess.run(["taskkill", "/F", "/IM", task_name, ">", "excaption.txt", "2>&1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            break
        else:
            for ssid in wifi_names:
                print(f"🔹 {ssid}")
            
            
  
        print("⏳ 5 daqiqa kutilyapti...\n")
        time.sleep(30)
except KeyboardInterrupt:
    print("\n❌ Dastur to‘xtatildi.")
