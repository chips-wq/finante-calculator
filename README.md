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
A(P, R, n) = P \frac{R(1+R)^{n}}{(1+R)^{n} - 1}
$$

_Nota: Exista credit cu [dobanda variabila [3]](https://www.investopedia.com/terms/v/variableinterestrate.asp), aceasta depinzand de un anumit indice, iar rata lunara se poate schimba._

$A$ = **anuitatea lunara** (rata lunara, banii pe care debitorul ii datoreaza bancii la scadenta)

De aici e evident, **costul total** = $n * A(P,R,n)$ (rata lunara \* numarul de luni)

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

In continuare, vom nota sirul $P_{i}$ sirul soldului creditului (cati bani mai ai de platit din principal).

Asadar, $P = P_{0} = 10.000$, valoarea initiala.

$P_{1} = 9025.05$, dupa prima plata si asa mai departe.

### Intuitie calculare rata lunara

1.  Observam ca **plata dobanzii** in prima luna este egala cu $R \cdot P_{0} = 56.25$.

Observam ca **plata principalului** in prima luna este restul din rata lunara $1031.2 - 56.25 = 974.95$

2. Observam ca **plata dobanzii** in a doua luna este egala cu $R \cdot P_{1} = 50.77$

Observam ca **plata principalului** in a doua luna este restul din rata lunara $1031.2 - 50.77 = 980.43$

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

_Observatie: Fiecare luna poate fi vazuta ca un credit nou, si din ea se poate calcula anuitatea lunara:_

$$
A(P_i, R, n-i) = A(P, R, n), \forall i
$$

**Rambursarea anticipata** [[2]](https://panorama.ro/rambursare-anticipata-credit-ipotecar-banca/) inseamna sa dai bani in plus, peste rata lunara.

In momentul cand dai bani, acestia se vor scade din **soldul creditului:** $P_i$, corespunzator lunii.

Evident, asta inseamna ca **dobanzile urmatoare vor fi mai mici**.

Sa presupunem ca dorim sa facem o **rambursare anticipata**, sa **scadem perioada** si sa mentinem **aceeasi anuitate lunara**. (exista mai multe optiuni).

Pentru simplitate, ne putem imagina alt credit, in momentul cand platim, acesta fiind: $A(P-q, R, n_2)$, unde

1. $q$ = reprezinta suma cat o inapoiem in momentul de fata
2. $R$ = reprezinta rata dobanzii anuale / 12 / 100
3. $n_2$ = numarul de luni care ramane dupa ce inapoiem q

Anuitatea lunara ramane la fel, deci ajungem la ecuatia:

$$
A(P-q, R, n_2) = A(P, R, n)
$$

Se observa ca daca $q \gt 0$, trebuie sa avem $n_2 \lt n$: perioada pe care platim **se reduce** (deci nu vom mai plati dobanda in acele luni).

In ecuatia de mai sus, singura necunoscuta este $n_2$ (numarul de luni nou). Ecuatia o vom rezolva prin metode numerice, iar rezultatul il vom rotunji in sus: _(vezi fsolve din scipy)_.

### Exemplu

Vom lua exemplul original, incepand cu `luna2`, vom pretinde ca e un credit nou si il vom rambursa anticipat cu `3000` de lei.

1. soldul_creditului = `8044.62`
2. rata_dobanzii = `6.75`
3. numarul_de_luni = `8`

```bash
[4.9745078] # valoarea exacta a lui n2
Principalul: 8044.62
Numarul de luni: 8
Rata dobanzii (pe an): 6.75
Costul total al creditului 8249.58
Costul total al dobanzii 204.96
Procent principal / credit: 97.52
   Luna  Rata lunară  Plata principalului  Plata dobânzii  Soldul creditului
0     1       1031.2               985.95           45.25            7058.67
1     2       1031.2               991.49           39.71            6067.18
2     3       1031.2               997.07           34.13            5070.11
3     4       1031.2              1002.68           28.52            4067.43
4     5       1031.2              1008.32           22.88            3059.11
5     6       1031.2              1013.99           17.21            2045.12
6     7       1031.2              1019.69           11.50            1025.43
7     8       1031.2              1025.43            5.77              -0.00


Noul numar de luni dupa rambursarea anticipata este: 5
Principalul: 5044.62
Numarul de luni: 5
Rata dobanzii (pe an): 6.75
Costul total al creditului 5130.07
Costul total al dobanzii 85.45
Procent principal / credit: 98.33
   Luna  Rata lunară  Plata principalului  Plata dobânzii  Soldul creditului
0     1      1026.01               997.64           28.38            4046.98
1     2      1026.01              1003.25           22.76            3043.73
2     3      1026.01              1008.89           17.12            2034.84
3     4      1026.01              1014.57           11.45            1020.27
4     5      1026.01              1020.27            5.74              -0.00
In total ai salvat ca dobanda 119.52
```

# Ce este DAE ?

[TODO: ...]

### Referinte

[[1]: https://www.jessym.com/articles/deriving-the-mortgage-payment-formula](https://www.jessym.com/articles/deriving-the-mortgage-payment-formula)

[[2]: https://panorama.ro/rambursare-anticipata-credit-ipotecar-banca/](https://panorama.ro/rambursare-anticipata-credit-ipotecar-banca/)

[[3]: https://www.investopedia.com/terms/v/variableinterestrate.asp](https://www.investopedia.com/terms/v/variableinterestrate.asp)

_Simulatorul si indicatiile sunt doar pentru credite cu dobanda fixa, insa cititorul poate deriva formule in cazul in care dobanda se schimba._

_Indicatie: din sirul $P_i$, vom calcula dobanda respectiva acelei luni: $R_i * P_i$ = dobanda in aceasta luna (rata lunara se schimba si ea)_
