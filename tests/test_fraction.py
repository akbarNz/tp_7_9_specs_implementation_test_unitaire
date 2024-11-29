import unittest
from fraction import Fraction, ZeroDenominatorException

class FractionTest(unittest.TestCase):
    def test_init_default_params(self):
        """tester la creation de Fraction avec les parametres par defaut"""
        o = Fraction()
        self.assertEqual(o, Fraction(0, 1))

    def setUp(self):
        return Fraction(3,4)
    
    def test_init_positive_params(self):
        """tester la creation de Fraction avec les parametres positives"""
        o = self.setUp()
        self.assertEqual(o, Fraction(3,4))
    
    def test_init_negative_params(self):
        """tester la creation de Fraction avec les parametres negatives"""
        o = Fraction(-3,-4)
        ob = self.setUp()
        self.assertEqual(o, ob)
    
    def test_init_negative_frac(self):
        """tester la création d'une Fraction negative"""
        t = Fraction(-3, 4)
        self.assertEqual(Fraction(3,-4),t)
        self.assertEqual(Fraction(-3, 4), t)
    
    def test_init_zero_den_exc(self):
        """tester la lerver de l'exception denominateur nul"""
        self.assertRaises(ZeroDenominatorException, Fraction, 3, 0)

    def test_init_typeerr_exc(self):
        """tester la lerver de l'exception TypeError"""
        self.assertRaises(TypeError, Fraction, 'ab', 4.2)

    def test_str(self):
        """tester le format de la chaine de caractères"""
        o = self.setUp()
        self.assertEqual(str(o), '3/4')
        self.assertEqual(str(Fraction(-3,4)), '-3/4')
    
    def test_as_mixed_number(self):
        """tester si une Fraction est un nombre mixte"""
        o = Fraction(7, 4)
        self.assertEqual(o.as_mixed_number(), '1(3/4)')
        o = Fraction(-7, 4)
        self.assertEqual(o.as_mixed_number(),'-2(1/4)')
        o = self.setUp()
        self.assertIsNone(o.as_mixed_number())

    def test_add(self):
        """tester l'addition"""
        o = self.setUp()
        t = Fraction(1,4)
        self.assertEqual(o+t, Fraction(1,1), 'addition de deux fractions positfs')
        t = Fraction(-1,3)
        self.assertEqual(o+t, Fraction(5,12), 'addition des fractions positif et negatif')
        s = Fraction(-3,5)
        self.assertEqual(t+s, Fraction(-14, 15), 'addition de deux fractions negatives')
        with self.assertRaises(TypeError, msg='test TypeError pour l\'addition'):
            x = self.setUp() + 'abc'

    def test_truediv(self):
        """tester la division réel"""
        o = self.setUp()
        t = Fraction(1, 4)
        x = o / t
        self.assertEqual(x, Fraction(3,1), 'division de deux fractions positives')
        t = Fraction(-1, 4)
        x = o / t
        self.assertEqual(x, Fraction(-3,1), 'division par une fraction negative')
        o = Fraction(-3,4)
        x = o / t
        self.assertEqual(x, Fraction(3, 1), 'division de deux fractions negatives')
        with self.assertRaises(TypeError, msg='test la levé d\'exception TypeError'):
            x = o / 'abc'
        with self.assertRaises(ZeroDenominatorException, msg='test la levé d\'un denominateur nul lors de la division par une fraction dont le numerateur est nul'):
            x = o / Fraction()
    
    def test_eq(self):
        o = self.setUp()
        self.assertEqual(o, Fraction(3,4), 'egalité entre deux fraction')
        self.assertNotEqual(o, Fraction(1,2), 'inegalité entre deux fraction')
        with self.assertRaises(TypeError, msg='test TypeError pour l\'egalité'):
            self.assertEqual(o, 'abc')
        
    def test_is_integer(self):
        t = Fraction(4,2)
        self.assertTrue(t.is_integer(), 'test de si la fraction est un entier : True')
        self.assertFalse(self.setUp().is_integer(), 'test de si la fraction est un entier : False')
    
    def test_is_proper(self):
        o = self.setUp()
        t = Fraction(5, 4)
        self.assertTrue(o.is_proper(), 'test fraction propre : True')
        self.assertFalse(t.is_proper(), 'test fraction propre : False')

    def test_is_adjacent_to(self):
        o = self.setUp()
        t = Fraction(1,2)
        x = Fraction(1,3)
        self.assertTrue(o.is_adjacent_to(t), 'test si deux fractions sont adjacent : True')
        self.assertFalse(o.is_adjacent_to(x), 'test si deux fractions sont adjacent : False')
        with self.assertRaises(TypeError):
            o.is_adjacent_to('abc')

if __name__ == '__main__':
    unittest.main()