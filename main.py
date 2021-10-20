def printMenu():
    print("1.Citire")
    print("2.Afisarea tuturor numerelor negative nenule din lista")
    print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
    print("4.Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu")
    print("CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
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

"""
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True
def oglindit(n):
    m = n
    inv = 1
    while m:
        u = m % 10
        inv = inv * 10 + u
        m = m // 10
    return inv
def superprim(y):
    x = oglindit(y)
    while x != 0:
        if is_prime(x) == 0:
            return False
        x = x // 10
    return True
def afis_superprim(l):
    rez = []
    for x in l:
        if superprim(x) == 1:
            rez.append(x)
    return rez
def test_afis_superprim():
    assert (afis_superprim([173, 239]) == 239) is True
def cmmdc(l):
    cmmdc1 = l[1]
    for i in range(len(l)):
        x = l[i]
        while(x != cmmdc1):
            if x > cmmdc1:
                x = x - cmmdc1
            else:
                if x < cmmdc1:
                    cmmdc1 = cmmdc1 - x
    return cmmdc1
def afis_cmmdc(l):
    x = cmmdc(l)
    rez = []
    for i in range(len(l)):
        if l[i] > 0:
            rez.append(x)
        else:
            rez.append(str(x)[::-1])
def test_afis_cmmdc():
    assert (afis_cmmdc([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]) is True
"""
def main():
    test_afis_nr_negative()
    test_ultima_cif_egal_nr()
    #test_afis_superprim()
    #test_afis_cmmdc()

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
        elif optiune == "4":
            print(afis_superprim(l))
        elif optiune == "5":
            print(afis_cmmdc(l))
        elif optiune == "x":
            break

main()