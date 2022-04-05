# Kâda valsts nolçma pâriet uz jaunu naudas sistçmu. Vecajâ sistçmâ bija trîs naudas vienîbas: dâlderis, grasis, santîms. Naudas vçrtîbas norâdîtas zemâk.
# 1 dâlderis = 37 graði
# 1 grasis = 162 santîmi
# Jaunajâ naudas sistçmâ paliek tikai santîmi un dâlderi. Santîms saglabâ savu vçrtîbu, bet 1 dâlderis bûs vienâds ar 100 santîmiem. Izveidot programmu, kas pârveidotu vecâs sistçmas naudu uz jaunu. Lietotâjam prasa ievadît vecâs sistçmas dâlderus, graðus un santîmus. Tiek aprçíinâts jaunâs sistçmas dâlderu un graðu daudzums. Rezultâts tiek parâdîts konsolç.

Vdalderis = float(input("Ievadiet dālderu daudzumu: "))
Vgrasis = float(input("Ievadiet grašu daudzumu: "))
Vsantims = float(input("Ievadiet santīmu daudzumu: "))

dalderis_sant = Vdalderis * 37 * 162
grasis_sant = Vgrasis * 162
santims = Vsantims
jauna = dalderis_sant + grasis_sant + santims

dalderis = jauna // 100
jauna = jauna % 100
santims = jauna

print("Pēc jaunās naudas sistēmas, Jums ir" ,dalderis,"dālderi un ",santims,"santīmi!")