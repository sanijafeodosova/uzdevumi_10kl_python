# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)

radiuss = int(input("Ievadiet cilindra radiusu: "))
augstums = int(input("Ievadiet cilindra augstumu: "))

tilpums = 3.14 * radiuss * radiuss * augstums
laukums = 2 * (3.14 * radiuss * radiuss) + augstums * (2 * 3.14 * radiuss)

print("Cilindra laukums ir  ",laukums," ,bet tilpums", tilpums)

