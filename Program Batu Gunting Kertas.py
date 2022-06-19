dfNopal = 0

Udin = 0

babak = int(input("Banyak ronde? "))

for x in range(babak):

    tamy = input("Nopal pilih apa? (B/G/K) ").upper()

    grah = input("Udin pilih apa? (B/G/K) ").upper()

    print("")

    if (tamy == "B" and grah == "G") or (tamy == "G" and grah == "K") or (tamy == "K" and grah == "B"):

        Nopal+=1

    elif (grah == "B" and tamy == "G") or (grah == "G" and tamy == "K") or (grah == "K" and tamy == "B"):

        Udin+=1

    else:

        continue

if Nopal>Udin:

    print("Selamat Nopal menang sebanyak", Nopal, "Ronde")

elif Nopal<Udin:

    print("Selamat Udin menang sebanyak", Udin, "Ronde")

else:

   print("Seri")