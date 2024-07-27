from scipy.optimize import fsolve
from math import ceil

def rambursare_anticipata_scade_perioada(principal, mothly_interest_rate, number_of_payments, valoare_rambursata):
  """
    Avem functia A(p, r, n). Cand rambursam anticipat, scadem din principal instant, asadar
    vom rezolva numeric ecuatia A(p-q, r, n2) = A(p, q, n), deoarece dorim ca anuitatea sa ramana constanta
    iar perioada sa scada: `n2 < n`
  """
  def equation(n2, P, q, r, n):
      # Formula pentru A initial
      A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
      # Formula pentru A cu noul principal si noul numar de luni
      A_new = (P - q) * r * (1 + r) ** n2 / ((1 + r) ** n2 - 1)
      # Echivalarea celor doua
      return A - A_new

  # Estimare initiala pentru n2 (putem folosi n ca o estimare initiala)
  n2_initial_guess = number_of_payments

  # Rezolvarea ecuatiei
  n2_solution = fsolve(equation, n2_initial_guess, args=(principal, valoare_rambursata, mothly_interest_rate, number_of_payments))

  print(n2_solution)
  n2 = ceil(n2_solution[0]) # Mereu platim o luna in plus

  return n2

# Creditul nostru echivalent, insa pornind din luna2
# A(8044.62, 6.75 / 12 / 100, 8) = A(10000, 6.75 / 12 / 100, 10), conform observatiei de la rambursare anticipata
credit_principal = 8044.62
rata = 6.75
numar_luni = 8

# Cati bani rambursam in acest moment
rambursat = 3000

# Noul numar de luni
new_num_of_months = rambursare_anticipata_scade_perioada(credit_principal, rata / 12 / 100, numar_luni, rambursat)

from calcul_anuitate import Credit

# Generam si creditul_dupa_rambursare, scazand direct din principal (soldul creditului)
credit_original = Credit(credit_principal, numar_luni, monthly_interest_rate=rata/12/100)
credit_dupa_rambursare = Credit(credit_principal-rambursat, new_num_of_months, monthly_interest_rate=rata/12/100)

print(credit_original)
print()
print()
print(f"Noul numar de luni dupa rambursarea anticipata este: {new_num_of_months}")
print(credit_dupa_rambursare)


print(f"In total ai salvat ca dobanda {round(credit_original.dobanda_totala - credit_dupa_rambursare.dobanda_totala, 2)}")
