# Zemniekam ir govis, cûkas un vistas. Govîm un cûkâm ir pa 4 kâjâm, vistâm – 2. Izveidot programmu, kas prasa lietotâjam ievadît cûku, govju un vistu skaitu. Tiek aprçíinâts kopçjais kâju daudzums. Rezultâts tiek izvadîts konsolç.

govis = int(input("Ievadiet govju skaitu : "))
cukas = int(input("Ievadiet cūku skaitu : "))
vistas = int(input("Ievadiet vistu skaitu : "))

Gkajas = govis*4
Ckajas = cukas*4
Vkajas = vistas*2

skaits = Gkajas + Ckajas + Vkajas

print ("Kopējais kāju skaits ir ",skaits)