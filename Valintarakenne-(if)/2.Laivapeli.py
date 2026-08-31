hytti = input("Anna hyttiluokka (LUX, A, B, C): ")

#Jos hytti on LUX
if hytti == "LUX":
    print("LUX-hytti on parvekkellinen hytti yläpuolella")

#Jos hytti on A
elif hytti == "A":
    print("A-hytti on ikkunallinen hytti autokannen yläpuolella")

#Jos hytti on B
elif hytti == "B":
    print("B-hytti on ikkunaton hytti autokannen yläpuolella")

#Jos hytti on C
elif hytti == "C":
    print("C-hytti on ikkunaton hytti autokannen alapuolella")

#Jos vastettiin muu kuin annetettu hyttiluokat
else:
    print("Virheellinen hyttiluokka. Anna hyttiluokka uudelleen (LUX, A, B, C).")
    