from fraction import Fraction, ZeroDenominatorException

def main():
    # Créer une fraction 3/4
    f1 = Fraction(3, 4)
    print('f1 : ',f1)  # Affiche : 3/4

    # Fraction par défaut (0/1)
    f2 = Fraction()
    print('f2 : ',f2)  # Affiche : 0/1

    # Fraction avec un numérateur et dénominateur négatifs
    f3 = Fraction(-6, -9)
    print('f3 : ',f3)  # Affiche : 6/9

    f4 = Fraction(-6, 9)
    print('f4 : ',f4)
    f = Fraction(7, 4)
    print('f : ', f)
    print('nombre mixte : ',f.as_mixed_number())  # Affiche : 1(3/4)

    result = f1 + f2
    print('addition : ',result) 
     
    result = f1 - f2
    print('soustraction : ',result)

    result = f1 * 3
    print('multiplication : ',result)  

    try:
        result = f1 / f2 # attention division par zero
        print('division reel : ',result)  
    except ZeroDenominatorException as e:
        print(e)

    result = f1 / f3
    print('division reel : ',result) 

    result = f ** 2
    print('puissance : ' ,result)  

    print('egalité : ',f1 == f2)  

    print('plus petit que : ',f1 < f2)

    print('plus grand que : ', f > f1 )


    print('est egal à zéro : ',f.is_zero())

    print('est un entier : ',f.is_integer())

    print('est propre : ',f.is_proper())

    print('est un fraction unitaire : ',f.is_unit())

    print('sont adjacent : ',f1.is_adjacent_to(f2))


if __name__ == "__main__":
    main()