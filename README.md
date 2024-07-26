# Librarie pentru calcule financiare

Aceasta librarie te ajuta sa iti estimezi **rata lunara, dobanda pe credit, dobanda pe depozit,** precum si
avantajele **rambursarii anticipate.**

## Ce este un credit de la banca si cum se plateste el ?

Atunci cand oamenii au nevoie de **o finantare** (de bani) pentru a-si cumpara **ceva acum** (o casa, a face o investitie) si nu au bani, apeleaza la o **institutie de credit** (banca) pentru a face un credit.

Institutia de credit le ofera bani in momentul de fata, iar ei profita intrucat persoana este obligata sa plateasca **bani in plus care se numesc dobanda**.

## Rata lunara

In cazul simplu, cand nu sunt alte comisioane, **rata lunara** depinde doar de

1. principal (cati bani imprumuti acum) = $P$
2. rata dobanzii anuale / 12 / 100 = $R$
3. numarul de luni pe care faci creditul = $n$

$$
A(P, r, n) = P \frac{R(1+R)^{n}}{(1+R)^{n} - 1}
$$

_Nota: Exista credit cu [dobanda variabila](https://www.investopedia.com/terms/v/variableinterestrate.asp), aceasta depinzand de un anumit indice_

$A$ = **anuitatea lunara** (rata lunara, banii pe care debitorul ii datoreaza bancii la scadenta)

De aici e evident, **costul total** = $n * A(p,r,n)$ (rata lunara \* numarul de luni)

### Cum se plateste creditul

Fiecare plata lunara este compusa din **principal** si **dobanda**.

**Soldul creditului** scade in fiecare luna cu partea platita din **principal**.

### Exemplu

Pentru a fi mai clar, vom face un exemplu, cu $A(10.000, 6.75/12/100, 10)$. [[1]](https://www.jessym.com/articles/deriving-the-mortgage-payment-formula)

1. Principal = 10.000 = $P$
2. Rata dobanzii anuale = 6.75. Notam $R = 6.75 / 12 / 100$ (rata dobanzii lunare)
3. Durata creditului = 10 luni = $n$

| Luna | Rata lunară | Plata principalului | Plata dobânzii | Soldul creditului |
| ---- | ----------- | ------------------- | -------------- | ----------------- |
| 1    | 1031.2      | 974.95              | 56.25          | 9025.05           |
| 2    | 1031.2      | 980.43              | 50.77          | 8044.62           |
| 3    | 1031.2      | 985.95              | 45.25          | 7058.67           |
| 4    | 1031.2      | 991.49              | 39.71          | 6067.18           |
| 5    | 1031.2      | 997.07              | 34.13          | 5070.11           |
| 6    | 1031.2      | 1002.68             | 28.52          | 4067.43           |
| 7    | 1031.2      | 1008.32             | 22.88          | 3059.11           |
| 8    | 1031.2      | 1013.99             | 17.21          | 2045.12           |
| 9    | 1031.2      | 1019.69             | 11.50          | 1025.43           |
| 10   | 1031.2      | 1025.43             | 5.77           | -0.00             |

In continuare, vom nota sirul $P_{i}$ sirul soldului creditului.

Asadar, $P = P_{0} = 10.000$, valoarea initiala.

$P_{1} = 9025.05$, dupa prima plata si asa mai departe.

1.  Observam ca **plata dobanzii** in prima luna este egala cu $R \cdot P_{0} = 56.25$.

Observam ca **plata principalului** in prima luna este restul din rata lunara $1031.2 - 56.25 = 974.95$

2. Observam ca **plata dobanzii** in a doua luna este egala cu $R \cdot P_{1} = 50.77$

**[... se poate continua pana la final]**

```bash
$ python3 calcul_anuitate.py
Principalul: 10000
Numarul de luni: 10
Rata dobanzii (pe an): 6.75
Costul total al creditului 10311.98
Costul total al dobanzii 311.98
Procent principal / credit: 96.97
   Luna  Rata lunară  Plata principalului  Plata dobânzii  Soldul creditului
0     1       1031.2               974.95           56.25            9025.05
1     2       1031.2               980.43           50.77            8044.62
```

# Ce este rambursarea anticipata ?

### Referinte

[[1]: https://www.jessym.com/articles/deriving-the-mortgage-payment-formula](https://www.jessym.com/articles/deriving-the-mortgage-payment-formula)
