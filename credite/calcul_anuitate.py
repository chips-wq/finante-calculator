"""
principal = valoarea imprumutata initial
monthly_interest_rate = rata lunara (de obicei rata dobanzii / 12)
number_of_payments = numarul de luni pe care este luat creditul
APR = dobanda_anuala_efectiva
"""

import pandas as pd

class Credit:
  def __init__(self, principal, number_of_payments, monthly_interest_rate=None, APR = None):
    self.principal = principal
    self.monthly_interest_rate = monthly_interest_rate # ex: rata dobanzii (din contract) / 12 / 100
    self.number_of_payments = number_of_payments
    self.APR = APR

    if APR is not None:
      # We will calculate the monthly_interest_rate from DAE and then have a more real representation of the cost of this credit
      self.monthly_interest_rate = (1 + APR / 100) ** (1 / 12) - 1
      # This is the effective monthly interest rate
      # P_k * self.monthly_interest_rate = dobanda din luna k
    else:
      assert(monthly_interest_rate is not None)
      self.monthly_interest_rate = monthly_interest_rate

    # Calculul ratei lunare folosind formula (se mai numeste anuitate)
    self.monthly_payment = self.principal * (self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.number_of_payments) / ((1 + self.monthly_interest_rate) ** self.number_of_payments - 1)
    # A(p, r, n) => anuitatea (monthly_payment) e o functie care depinde de 
    # `principal`, `rata la fiecare plata` si `numarul de plati`

    # Calculeaza scadentarul pentru acest credit
    self.scadentar()

  def scadentar(self):
      # Inițializare variabile
    remaining_balance = self.principal
    schedule = []

    self.dobanda_totala = 0

    # Generarea scadentarului
    for i in range(1, self.number_of_payments + 1):
        interest_payment = remaining_balance * self.monthly_interest_rate
        principal_payment = self.monthly_payment - interest_payment
        remaining_balance -= principal_payment
        self.dobanda_totala += interest_payment
        schedule.append({
            "Luna": i,
            "Rata lunară": round(self.monthly_payment, 2),
            "Plata principalului": round(principal_payment, 2),
            "Plata dobânzii": round(interest_payment, 2),
            "Soldul creditului": round(remaining_balance, 2)
        })

    # Crearea unui DataFrame pentru scadentar
    self.schedule_df = pd.DataFrame(schedule)



    # print(f"In total platesti: {self.monthly_payment * self.number_of_payments}")
    # print(f"In total platesti dobanda: {self.dobanda_totala}")
  def save_scadentar(self, nume):
    # Salvarea scadentarului într-un fișier Excel
    self.schedule_df.to_excel(f"{nume}.xlsx", index=False)

  def __str__(self):
    res = ""
    if self.APR:
      res += "Rata lunara a fost calculata din DAE, deci anuitatea poate sa difere (din cauza comisioanelor), insa costul total al creditului e corect.\n"
      res += f"DAE: {self.APR}\n"
    
    cost_total = round(self.monthly_payment * self.number_of_payments, 2)
    res += f"Principalul: {self.principal}\n"
    res += f"Numarul de luni: {self.number_of_payments}\n"
    res += f"Rata dobanzii (pe an): {round(self.monthly_interest_rate * 12 * 100, 3)}\n"
    res += f"Costul total al creditului {cost_total}\n"
    res += f"Costul total al dobanzii {round(self.dobanda_totala, 2)}\n"
    res += f"Procent principal / credit: {round(self.principal / cost_total * 100, 2)}"

    res += "\n"
    # Afișarea primelor 12 luni din scadentar
    # res += repr(self.schedule_df.head(12))
    res += repr(self.schedule_df)

    return res
    
def read_credit_from_stdin():
  print("Introdu principalul: ")
  principal = float(input())  # valoarea creditului
  print("Introdu Dobanda Anuala (nu efectiva) in procente: ")
  annual_interest_rate = float(input())  # rata dobanzii
  print("Introdu durata creditului in luni:")
  months = int(input())  # durata creditului

  return principal, annual_interest_rate, months

if __name__ == "__main__":
  principal, annual_interest_rate, months = read_credit_from_stdin()

  credit_random = Credit(principal, months, monthly_interest_rate=annual_interest_rate/12/100)
  print(credit_random);
