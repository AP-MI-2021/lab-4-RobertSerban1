def printMenu():
    print("1.Citire")
    print("2.Afisarea tuturor numerelor negative nenule din lista")
    print("x.Iesire")
def citireLista():
    l = []
    givenString = input("Dati lista de numere intregi, separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def afis_nr_negative(l):
    """
    afiseaza toate numerele negative nenule din lista
    :param l: lista de numere intregi
    :return: lista de numere doar cu numerele negative
    """
    rez = []
    for x in l:
        if x < 0:
            rez.append(x)
    l = rez
    return l
def test_afis_nr_negative():
    assert afis_nr_negative([-1, 2, 0, 3, -4]) == [-1, -4]

def main():
    test_afis_nr_negative()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(test_afis_nr_negative(l))
        elif optiune == "x":
            break

main()
