f = 1
nb = int(input("entrer un nombre entier positif : "))
for i in range (1 , nb + 1): # you dont need to declare i, if you're making a loop
    f = f * i                # ( l'affectation a chaque fois la boucle continue(f))1 = 1 * 1 , 1 = 1 * 2 , 2 = 2 * 3 , 3 = 3 * 4 ...
print("factorielle de",nb,"est :",f)
