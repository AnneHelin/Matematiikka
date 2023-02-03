# hypotenuusan laskeminan

import math

A=float(input("Anna 1. kateetin pituus:"))
B=float(input("Anna 2. kateetin pituus:")) # Liukuluku

# Laketaan hypotenuusa
C= math.sqrt(A**2 + B**2) # Neliöjuuri

print("Hypotenuusan pituus on", round(C, 2))

