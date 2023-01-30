def main():
    print("Anna 8 kokonaislukua, laske niiden keskiarvo")
    i = 0
    summa = 0
    while i < 8:
        rivi = input("Anna seuraava luku:")
        luku = int(rivi)
        summa = summa + luku
        i = i + 1
        keskiarvo = summa / 8
        print('Niiden keskiarvo on', keskiarvo)

        main()