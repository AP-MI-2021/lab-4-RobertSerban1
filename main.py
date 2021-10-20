def printMenu():
    print("1.Citire")
    print("2.Afisarea tuturor numerelor negative nenule din lista")
    print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
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
def ultima_cif_egal_nr(l, x):
    """
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param l: lista de nr intregi
    :param x: un numar intreg
    :return: numarul care are ultima cifră egală cu o cifră citită
    """
    min = 999999
    for i in l:
        if i % 10 == x:
            if i < min:
                min = i
    return min
def test_ultima_cif_egal_nr():
    assert ultima_cif_egal_nr([1, 6, 34, 68, 40, 48, 20], 8) == 48

def main():
    test_afis_nr_negative()
    test_ultima_cif_egal_nr()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(test_afis_nr_negative(l))
        elif optiune == "3":
            x = int(input("Dati un numar"))
            print(test_ultima_cif_egal_nr(l, x))
        elif optiune == "x":
            break

main()
