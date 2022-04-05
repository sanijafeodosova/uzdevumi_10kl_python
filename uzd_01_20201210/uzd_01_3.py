# Izveidot programmu, kura prasa lietotâjam sekunþu skaitu. Sekundes tiek pârveidotas par “x hours y minutes z seconds” tipa tekstu. Rezultâts tiek parâdîts konsolç.

laiks = float(input("Ievadiet sekunžu skaitu: "))
dienas = laiks // (24 * 3600)
laiks = laiks % (24 * 3600)
stundas = laiks // 3600
laiks %= 3600
minutes = laiks // 60
laiks%=60
seconds = laiks
print("%d dienas %d stundas %d minūtes %d sekundes" % (dienas, stundas, minutes, seconds))