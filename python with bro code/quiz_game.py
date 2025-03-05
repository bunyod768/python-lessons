savollar = (("Inson tanasida necha litr qon mavjud?"),
            ("Ozbekistonda aholi soni(MLN) ?"),
            ("Alisher Navoiy qachon tavallud topgan?"),
            ("Amir Temur qachon tavallud topgan?"))

variantlar =  (("A.2" , "B.3" ,"C.4" ,"D.7"),
              ("A.37","B.40" ,"C.45" ,"D.43"),
              ("A.1447","B.1441","C.1443","D.1483"),
              ("A.1356","B.1336","C.1401","D.1354"))
savol_num = 0
corr_ans = 0

javoblar = ["C","A","B","B"]
all_ans = []
print("------------------------")
print("Welcome to the quiz game ")
print("------------------------")

for savol in savollar:
    print(savol)
    for variant in variantlar[savol_num]:
            print(variant)
    print("------------------------")
     
    sorov = input("Enter the answer: ").upper()
    all_ans.append(sorov)
    if sorov ==javoblar[savol_num]:
          print("CORRECT!")
          corr_ans += 1
    else:
          print("INCORRECT!")
          print(f"The current answer is  {javoblar[savol_num]} ")      
    savol_num += 1        
total = (corr_ans/len(savollar) *100)
print(f"Your answers:{all_ans}")
print(f"Current answers:{javoblar}")
print(f"Your result: {total}%")
