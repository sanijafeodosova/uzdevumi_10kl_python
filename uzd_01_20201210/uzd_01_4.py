# Izveidot kalkulatoru. Programma prasa lietotājam ievadīt divus skaitļus. Ar šiem skaitļiem tiek veiktas operācijas (saskaitīšana, atņemšana, reizināšana, dalīšana). Rezultāts tiek parādīts konsolē.

from ctypes import resize


num1 = int(input("Ievadiet pirmo skaitli : "))
num2 = int(input("Ievadiet otro skaitli : "))

summ = num1 + num2
atnem = num1 - num2
reiz = num1 * num2
dal = num1 / num2

print ("Šo skaitļu summa ir",summ,"starpība ir",atnem,"reizinājums ir",reiz,"un dalījums ir",dal)