numbers=input(">>>")
translate = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
count = ""
for num in numbers:
    count += translate.get(num,"exception") + " "
print(count)    