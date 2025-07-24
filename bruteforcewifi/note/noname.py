import subprocess

# Buyruqni ishga tushirish va natijani olish
result = subprocess.run(
    ["ipconfig", "/all"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8"
)

# Natijani faylga yozish
with open("info.txt", "w", encoding="utf-8") as f:
    f.write(result.stdout)
