import subprocess

# Ping qilinadigan manzil
target = "google.com"

# Natijani yozib olinadigan fayl nomi
output_file = "ping_natijasi.txt"

# Ping buyrug'ini bajarish
try:
    result = subprocess.run(
        ["ping", "-n", "4", target],  # Agar siz Linuxda ishlatsangiz, "-n" o'rniga "-c" yozing
        capture_output=True,
        text=True
    )

    # Natijani faylga yozish
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.stdout)

    print(f"Ping natijasi '{output_file}' fayliga saqlandi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
