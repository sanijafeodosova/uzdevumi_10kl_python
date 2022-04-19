# Apgriezt pozitīva skaitļa ciparu secību. Piemērs: 12345 => 54321

skaitlis = int(input("Ievadiet skaitli: "))
 
sk = 0
while(skaitlis>0):
  rev = skaitlis % 10
  sk = (sk * 10) + rev
  skaitlis = skaitlis//10
 
print("Apgrieztais skaitlis ir : {}".format(sk))