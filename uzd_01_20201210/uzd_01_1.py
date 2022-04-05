# Uzdevums: 01-1: Izveidot programmu, kas prasa lietotâjam ievadît skaitli n, tad programma aprçíina n+nn+nnn. Rezultâts tiek parâdîts konsolç.

n=int(input("Ievadiet skaitli n: "))
skatit=str(n)
t1=skatit+skatit
t2=skatit+skatit+skatit
iznak=n+int(t1)+int(t2)
print("Iznākums ir : ",iznak)