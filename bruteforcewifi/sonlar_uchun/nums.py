total = 25_000_000
part_size = total // 4  # 25 million
part_num = 1

start = 25_000_000
end = 50_000_000
filename = "part2.txt"
with open(filename, "w", encoding="utf-8") as f:
     for i in range(start, end):
        f.write(f"{i:08}\n")

print(f"✅ {filename} yozildi: {start:08} dan {end - 1:08} gacha.")
