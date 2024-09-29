class Depozit():
  """
  Calculatorul isi asuma cateva lucruri:

  1. Dobanda va fi platita anual astfel suma_depozit += suma_depozit * dobanda_an_procente
  (se observa ca dobanda e adaugata automat inapoi in depozit, astfel avem *compound interest*)

  2. Va fi platit un depozit pe venit la data scadentei (la final) de 10% din suma dobandei castigate.
  """
  def __init__(self, suma_initiala, dobanda_an_procente, numar_ani):
    self.suma_initiala = suma_initiala
    self.r = dobanda_an_procente / 100
    self.numar_ani = numar_ani
  
  def simulate(self):
    # Compound interest formula
    suma_finala = self.suma_initiala * (1 + self.r) ** self.numar_ani
    dobanda_fara_impozit = suma_finala - self.suma_initiala

    dobanda_cu_impozit_luat = 90/100 * dobanda_fara_impozit
    print(f"Dobanda dupa impozit: {round(dobanda_cu_impozit_luat, 2)}")
    print(f"Suma initiala: {self.suma_initiala}")
    print(f"Suma finala: {round(dobanda_cu_impozit_luat + self.suma_initiala, 2)}")



if __name__ == '__main__':
  print("Suma initiala: ")
  suma_initiala = float(input())

  print("Dobanda an procente: ")
  dobanda_an_procente = float(input())

  print("Numarul de ani: ")
  numar_ani = int(input())

  depozit = Depozit(suma_initiala, dobanda_an_procente, numar_ani)
  depozit.simulate()

