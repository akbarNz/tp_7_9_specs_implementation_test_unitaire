class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num, den : sont de type entier. den doit être strictement superieur à 0
        POST : None
        RAISES : ZeroDenominatorException si den = 0, TypeError si num et den pas entier
        """
        
        if not (isinstance(num, int) and isinstance(den, int)):
            raise TypeError(f"type de num : {type(num)}\n type de den : {type(den)}\n le numerateur et le denominateur doivent être de type int")    
        if den == 0:
            raise ZeroDenominatorException("Le dénominateur d'une fraction ne peut être egal à zéro.")
        # traitement de cas possible pour les valeurs de num et den
        if num < 0 and den < 0:
            self.__fract = self._simplifier(abs(num), abs(den))
        elif den < 0:
            # pour les opperations le moin de la fraction porte sur le numerateur
            self.__fract = self._simplifier(-num, abs(den))
        else:
            self.__fract = self._simplifier(num, den) # encapsulation
        
                 

    @property
    def numerator(self):
        return self.__fract[0]
    @property
    def denominator(self):
        return self.__fract[1]
    
# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : renvoie une chaine de caractère suivant le format : [-]num/den
        le signe moins est présent qu'en cas de fraction negative
        """
        return f'{self.numerator}/{self.denominator}'

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : la valeur absolue de num > la valeur absolue de den : fraction impropre
        POST : renvoie la chaine de caractères sous le format : i(j/den)
        où i est la partie entière, j est le reste de la division de num et den. 
        renvoie None si pas un nombre mixte.
        """
        if abs(self.numerator) <= abs(self.denominator):
            return None

        i = self.numerator // self.denominator
        j = self.numerator % self.denominator

        return f'{i}({j}/{self.denominator})'

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other peut être de type Fraction ou entier
         POST : renvoie un objet de type Fraction.
         RAISES : TypeError si other n'est pas de type entier ou Fraction
         """
        
        if not isinstance(other, (Fraction, int)):
            raise TypeError(f'type de other : {type(other)}. ne supporte pas l\'addition avec ce type. type doit être Fraction ou int')
        if isinstance(other, int):
            other = Fraction(other)
        #meme denominateur
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        #denominateur différent
        den_commun = self._ppcm(self.denominator, other.denominator)
        n = (den_commun // self.denominator) * self.numerator + (den_commun // other.denominator) * other.numerator
        return Fraction(n, den_commun)


    def _ppcm(self, nb1, nb2):
        return abs(nb1 * nb2) // self._gcd(nb1, nb2)

    def _gcd(self, a, b):
    
        while b != 0:
            r = a % b
            a = b
            b = r

        return a
    
    def _simplifier(self, num, den):
        """Simplifier une fraction
        PRE: -
        POST: Renvoie un tuple.
        """
        div = self._gcd(num, den)
        return (num//div, den//div)
    
    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other peut être de type Fraction ou entier
        POST : renvoie un objet de type Fraction.
        """

        if not isinstance(other, (Fraction, int)):
            raise TypeError(f'type de other : {type(other)}. ne supporte pas la soustraction avec ce type. type doit être Fraction ou int')
        if isinstance(other, int):
            other = Fraction(other)
        #meme denominateur
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        #denominateur différent
        den_commun = self._ppcm(self.denominator, other.denominator)
        n = (den_commun // self.denominator) * self.numerator - (den_commun // other.denominator) * other.numerator
        return Fraction(n, den_commun)

        
    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other peut être de type Fraction ou entier
        POST : renvoie un objet de type Fraction.
        """

        if not isinstance(other, (Fraction, int)):
            raise TypeError(f'la multiplication entre le type {type(self)} et \
                            le type {type(other)} n\'est pas defini. le type doit être Fraction ou int')
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

        
            

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other peut être de type Fraction ou entier
        POST : renvoie un objet de type Fraction.
        """

        if not isinstance(other, (Fraction, int)):
            raise TypeError(f'la multiplication entre le type {type(self)} et \
                            le type {type(other)} n\'est pas defini. le type doit être Fraction ou int')
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

        
            
    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : type de other doit être entier
        POST : renvoie un objet de type Fraction.
        """
        if not isinstance(other, int):
            raise TypeError(f'le type {type(other)} n\'est pas valide. type doit être int')
        
        return Fraction(self.numerator ** other, self.denominator ** other)

        
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : type de other doit être Fraction
        POST : renvoie un booléen. True si égalité, False sinon. 
        
        """

        if not isinstance(other, Fraction):
            raise TypeError(f'le type {type(other)} n\'est pas valide. type doit être Fraction')
        
        return self.numerator == other.numerator and self.denominator == other.denominator


            
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : -
        POST : Renvoie un float
        """
        return self.numerator / self.denominator
    
    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)
    def __gt__(self, other):
        """Overloading of > for fractions
        PRE: type de other Fraction
        POST: renvoie un booleen. True si plus grand, False sinon.
        RAISES: TypeError si type de other autre que Fraction
        """

        if not isinstance(other, Fraction):
            raise TypeError(f'le type {type(other)} n\'est pas valide. other doit être de type Fraction')
        
        return self.__float__() > other.__float__()

        

    def __lt__(self, other):
        """Overloading of < for fractions
        PRE: type de other Fraction
        POST: renvoie un booleen. True si plus grand, False sinon.
        RAISES: TypeError si type de other autre que Fraction
        """

        if not isinstance(other, Fraction):
            raise TypeError(f'le type {type(other)} n\'est pas valide. other doit être de type Fraction')
        
        return self.__float__() < other.__float__()




    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -
        POST : renvoie un booléen. True si num = 0, False sinon.
        """
        return self.numerator == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : renvoie un booléen. True si num est entièrement divisible par den, False sinon.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : renvoie un booléen. True si fraction propre, False sinon.
        """
        return self.numerator < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : renvoie un booléen. True si num = 1 lorsque simplifié, False sinon.
        """
        diviseur = self._gcd(self.numerator, self.denominator)
        # fraction déjà simplifié
        if diviseur == 1:
            # fraction peut etre positif ou negatif 
            return abs(self.numerator) == 1
        # simplification du num
        return abs(self.numerator) / diviseur == 1
    
    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference is a unit fraction

        PRE : type de other doit être Fraction
        POST : renvoie un booléen. True s'ils sont adjacent, False sinon.
        RIAISES : TypeError si other n'est pas de type Fraction.
        """

        if not isinstance(other, Fraction):
            raise TypeError(f'le type {type(other)} n\'est pas valide. other doit être de type Fraction')
        
        # travailler qu'avec les copy positives de deux fractions
        scpy = Fraction(abs(self.numerator), self.denominator)
        ocpy = Fraction(abs(other.numerator), other.denominator)
        # travailler qu'en positif pour se faciliter la tache
        if scpy > ocpy:
            unit = scpy - ocpy
            # unit doit être une fraction unitaire
            if not unit.is_unit():
                return False
            # ocpy + unit = scpy 
            return ocpy + unit == scpy
        else:
            unit = ocpy - scpy
            # unit doit être une fraction unitaire
            if not unit.is_unit():
                return False
            # scpy + unit = ocpy 
            return scpy + unit == ocpy
            

class ZeroDenominatorException(Exception):
    pass
