# Librarie pentru calcule financiare

Aceasta librarie te ajuta sa iti estimezi **rata lunara, dobanda pe credit, dobanda pe depozit,** precum si
avantajele **rambursarii anticipate.**

## Ce este un credit de la banca si cum se plateste el ?

Atunci cand oamenii au nevoie de **o finantare** (de bani) pentru a-si cumpara **ceva acum** (o casa, a face o investitie) si nu au bani, apeleaza la o **institutie de credit** (banca) pentru a face un credit.

Institutia de credit le ofera bani in momentul de fata, iar ei profita intrucat persoana este obligata sa plateasca **bani in plus care se numesc dobanda**.

## Rata lunara

In cazul simplu, cand nu sunt alte comisioane, **rata lunara** depinde doar de

1. principal (cati bani imprumuti acum) = $p$
2. rata dobanzii anuale / 12 = $r$
3. numarul de luni pe care faci creditul = $n$

$$
A(p, r, n) = P \frac{r(1+r)^{n}}{(1+r)^{n} - 1}
$$

$A$ = **anuitatea lunara** (rata lunara, banii pe care debitorul ii datoreaza bancii la scadenta)

De aici e evident, **costul total** = $n * A(p,r,n)$ (rata lunara \* numarul de luni)

### Cum se plateste creditul

Fie
