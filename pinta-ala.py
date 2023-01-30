def main():
    rivi = input("Anna nelion sivun pituus (cm): ")
    sivu = float(rivi)
    while sivu < 0:
        print("Sivun pituus ei saa olla negatiivinen!")
        rivi = input("Anna sivun pituus (cm): ")
        rivi = input("Anna sivun pituus (cm): ")
        sivu = float(rivi)
        sivu = float(rivi)
    ala = sivu * sivu
    print("Nelion pinta-ala on", ala, "cm2.")

main()
