# Piirin laskeminen

# Neliön sivujen pituus:

a = 8 
b = 8 
c = 8
d = 8 

def piiri(sivut, yksikko):
    piiri = 0
    for sivu in sivut:
        piiri += sivu
    return ('p=' +str(piiri) + ' ' + yksikko)

print(piiri((8, 8, 8, 8), 'cm'))        

# Pinta-alan laskwminen

a = 8 
b = 8 
c = 8
d = 8 

