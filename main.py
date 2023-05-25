# modulul(fisierul) get_data.py contine codul care preia date online despre valute si le returneaza intr-un dictionar:
import get_data

# dictionar predefinit cu valute raportate la 1 euro (2023) (il putem folosi daca sunt probleme cu functionarea API)
# curs_valutar = {'EUR': 1, 'USD': 1.0876, 'RON': 4.9375, 'PLN': 4.5078, 'SEK': 11.2905, 'CHF': 0.9747, 'CAD': 1.4684}

curs_valutar = get_data.main()

# cream string cu valute acceptate pe care il afisam in consola. string-ul este format din dictionar
valute_acceptate = ""
for valuta in curs_valutar.keys():
    valute_acceptate += valuta + ", "


# verificare daca datele introduse sunt acceptate
def wrong_input(user_input):
    if user_input not in valute_acceptate:
        print("Valuta neacceptata.")
        return 1
    return 0


print(f"Valute acceptate: {valute_acceptate[:-2]}\n")

while True:  # programul de conversie se repeta pana il inchidem noi
    while True:  # secventa se repeta pana introducem o valoare acceptata
        din_valuta = input("Convertiti din valuta: ").upper()
        if wrong_input(din_valuta) == 1:
            continue
        else:
            break

    while True:
        in_valuta = input("In valuta: ").upper()
        if wrong_input(in_valuta):
            continue
        else:
            break

    cantitate = float(input("Cantitate: "))

    # se face conversia, si apoi se afiseaza rezultatul:
    cantitate_referinta = cantitate / curs_valutar[din_valuta]
    cantitate_convertita = (cantitate_referinta * curs_valutar[in_valuta]).__round__(2)

    print(f"\n{cantitate} {din_valuta} = {cantitate_convertita} {in_valuta}\n")
