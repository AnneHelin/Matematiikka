# Tässä tiedostossa lasketaan painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määritys

# Painoindeksi
def bmi(paino, pituus):
    """Laskee painoindeksin kaavalla paino jaettuna pituuden sadasosa neliöllä
    
    Args:
        paino (float): paino kiloina
        pituus (float): pituus senttimetreinä (cm)
        
    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / (pituus/100) ** 2
    return painoindeksi

 # Rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee henkilön kehon rasvaprosentin
    
    Args:
        bmi (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli (int): 1 - Miehet, 0 - Naiset
        
    Returns:
        float: kehon rasvaprosentti 
   """   
    # Aikuisen rasvaprosentti
    if ika >= 18:
        rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    else:
        # Lapsen rarvaprosentti
        rprosentti = 1.5 * bmi - 0.70 * ika - 3.6 * sukupuoli + 1.4

    return rprosentti

    # Testit
    if __name__=='__main__':

        # 1. Testi painoindeksi
        pituus = 165
        paino = 59
        omabmi = bmi(paino, pituus)
        print('Pituus:', pituus, 'Paino', paino, 'Painoineksi', bmi)

        # 2. Rasvaprosentti
        ika = 46
        sukupuoli = 0
        print('Rasvaprosentti:', rasvaprosentti(omabmi, ika, sukupuoli))

            