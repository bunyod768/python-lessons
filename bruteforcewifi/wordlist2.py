def case_variants(word):
    return {word.lower(), word.upper(), word.capitalize()}

ismlar = ["Zokir", "Sevinch"]
familiyalar = ["1", ""]
yillar = ["2006", "2009"]
kunlar = ["16", "16", "11", "20"]
oylar = ["06", "07", "08", "09"]
raqamlar = ["", "", "", ""]
belgilar = ["", "@", "_", "!", ".", "-"]

kombinatsiyalar = set()

for ism in ismlar:
    for ism_var in case_variants(ism):
        for yil in yillar:
            for belgi in belgilar:
                kombinatsiyalar.add(f"{ism_var}{belgi}{yil}")
                kombinatsiyalar.add(f"{yil}{belgi}{ism_var}")

        for fam in familiyalar:
            for fam_var in case_variants(fam):
                kombinatsiyalar.add(f"{ism_var}{fam_var}")
                for yil in yillar:
                    kombinatsiyalar.add(f"{ism_var}{fam_var}{yil}")
                    for belgi in belgilar:
                        kombinatsiyalar.add(f"{ism_var}{belgi}{fam_var}{belgi}{yil}")

# Ustiga qo‘shish: ism1 + ism2 + belgilar + yillar + raqamlar
for ism1 in ismlar:
    for ism2 in ismlar:
        if ism1 != ism2:
            for i1 in case_variants(ism1):
                for i2 in case_variants(ism2):
                    for belgi in belgilar:
                        kombinatsiyalar.add(f"{i1}{belgi}{i2}")
                        for yil in yillar:
                            kombinatsiyalar.add(f"{i1}{belgi}{i2}{belgi}{yil}")

# + Raqamlar bilan oxirgi kombinatsiyalar
for ism in ismlar:
    for ism_var in case_variants(ism):
        for raqam in raqamlar:
            for belgi in belgilar:
                kombinatsiyalar.add(f"{ism_var}{belgi}{raqam}")
                kombinatsiyalar.add(f"{raqam}{belgi}{ism_var}")

# Tozalash va yozish
filtered = [k for k in kombinatsiyalar if len(k) >= 8]

with open("wordlist2.txt", "w", encoding="utf-8") as f:
    for password in sorted(filtered):
        f.write(password + "\n")

print(f"✅ {len(filtered)} ta kuchli kombinatsiya yozildi (katta-kichik harflar bilan).")
