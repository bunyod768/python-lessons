def case_variants(word):
    return {word.lower(), word.upper(), word.capitalize()}

# Bitta odam haqida ma'lumot
ism = "Zokir"
familya = "Bahodirov"
yil = "2006"
oy = "07"
kun = "16"
yosh = "19"
raqam = "947551007"

belgilar = ["", "@", "_", "!", ".", "-"]

kombinatsiyalar = set()

# Ism + yil + belgilar
for ism_var in case_variants(ism):
    for belgi in belgilar:
        kombinatsiyalar.add(f"{ism_var}{belgi}{yil}")
        kombinatsiyalar.add(f"{yil}{belgi}{ism_var}")
        kombinatsiyalar.add(f"{ism_var}{belgi}{kun}{belgi}{oy}")
        kombinatsiyalar.add(f"{ism_var}{belgi}{oy}{belgi}{kun}")
        kombinatsiyalar.add(f"{ism_var}{belgi}{yil}{belgi}{oy}{belgi}{kun}")

# Ism + familya + yil + belgilar
for ism_var in case_variants(ism):
    for fam_var in case_variants(familya):
        for belgi in belgilar:
            kombinatsiyalar.add(f"{ism_var}{fam_var}")
            kombinatsiyalar.add(f"{ism_var}{belgi}{fam_var}")
            kombinatsiyalar.add(f"{ism_var}{belgi}{fam_var}{belgi}{yil}")
            kombinatsiyalar.add(f"{fam_var}{belgi}{ism_var}{belgi}{yil}")
            kombinatsiyalar.add(f"{ism_var}{belgi}{fam_var}{belgi}{oy}{belgi}{kun}")

# Ism + raqam + belgi
for ism_var in case_variants(ism):
    for belgi in belgilar:
        kombinatsiyalar.add(f"{ism_var}{belgi}{raqam}")
        kombinatsiyalar.add(f"{raqam}{belgi}{ism_var}")

# Tozalash: faqat 8 yoki undan uzun kombinatsiyalar
filtered = [k for k in kombinatsiyalar if len(k) >= 8]

# Faylga yozish
with open("wordlist1.txt", "w", encoding="utf-8") as f:
    for password in sorted(filtered):
        f.write(password + "\n")

print(f"✅ {len(filtered)} ta kuchli kombinatsiya yozildi.")
