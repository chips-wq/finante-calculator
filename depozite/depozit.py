print("Suma initiala: ")
suma_initiala = float(input())

print("Dobanda an procente: ")
dobanda_an_procente = float(input())

print("Numarul de ani: ")
numar_ani = int(input())

# suma_finala = suma_initiala
# for i in range(1, numar_ani + 1):
#   dobanda_bani = suma_finala * dobanda_an_procente / 100
#   print(dobanda_bani)
#   suma_finala += dobanda_bani

r = dobanda_an_procente / 100
suma_finala = suma_initiala * (1 + r) ** numar_ani
dobanda = suma_finala - suma_initiala

print(f"Dobanda este: {dobanda}")
dobanda = 90/100 * dobanda
print(f"Dobanda dupa impozit: {dobanda}")
print(f"Suma initiala: {suma_initiala}")
print(f"Suma finala: {round(suma_initiala + dobanda, 2)}")


