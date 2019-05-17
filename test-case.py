import unittest
from unittest.mock import patch
from math import pi
from hypothesis import given
import hypothesis.strategies as st
import Exercices_tests_unitaires as ex

class Exercice_1_test_case(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_positif(self, x, y):
        self.assertEqual(ex.exercice_1(x,y),x*y)

    @given(st.integers(), st.integers())
    def test_negatif(self, x, y):
        # print()
        self.assertEqual(ex.exercice_1(-x, y), -x * y)

    def test_null(self):
        self.assertEqual(ex.exercice_1(0, 200), 0)
        self.assertEqual(ex.exercice_1(0, 0), 0)
        self.assertEqual(ex.exercice_1(0, -500), 0)

    def test_str(self):
        self.assertRaises(TypeError, ex.exercice_1, "abc","def")
        self.assertRaises(TypeError, ex.exercice_1, "abc", 0)
        self.assertRaises(TypeError, ex.exercice_1, 10, "")

class Exercice_2_test_case(unittest.TestCase):

    def test_inf(self):
        self.assertEqual(ex.exercice_2(-2, 5, 5), -255)
        self.assertEqual(ex.exercice_2(-10, 0, 5), -255)
        self.assertEqual(ex.exercice_2(-1, 0, 5), -255)

    def test_up(self):
        self.assertEqual(ex.exercice_2(8, -2, 5), 255)
        self.assertEqual(ex.exercice_2(10, -6, 5), 255)
        self.assertEqual(ex.exercice_2(-1, -10, -5), 255)

    def test_inter(self):
        self.assertEqual(ex.exercice_2(2, -2, 5), 2)
        self.assertEqual(ex.exercice_2(-3, -6, 0), -3)
        self.assertEqual(ex.exercice_2(0, 0, 0), 0)
        self.assertEqual(ex.exercice_2(1, 1, 5), 1)

    def test_str(self):
        self.assertRaises(TypeError, ex.exercice_2, "abc", "def", "ghi")
        self.assertRaises(TypeError, ex.exercice_2, "abc", 0, 2)
        self.assertRaises(TypeError, ex.exercice_2, 10, "", "abc")


class Exercice_3_test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Debut")

    @classmethod
    def tearDownClass(cls):
        print("Fin")

    def setUp(self):
        self.exo = ex.Exercice_3()

    def tearDown(self):
        print("Fin du test")

    def test_r_num(self):
        self.assertEqual(self.exo.r_num(10),None)
        self.assertEqual(self.exo.r,10)
        self.assertRaises(TypeError,self.exo.r_num, "abc")
        self.assertRaises(ValueError, self.exo.r_num, -5)

    def test_r_num(self):
        self.assertEqual(self.exo.r_num(10),None)
        self.assertEqual(self.exo.r,10)
        self.assertRaises(TypeError,self.exo.r_num, "abc")
        self.assertRaises(ValueError, self.exo.r_num, -5)

    def test_aire(self):
        self.assertAlmostEqual(self.exo.aire(10), pi*10**2)
        self.assertEqual(self.exo.aire(0), 0)
        self.assertRaises(TypeError, self.exo.aire, "abc")
        self.assertRaises(ValueError, self.exo.aire, -8)

    def test_dans_cercle(self):
        self.assertTrue(self.exo.dans_cercle(2, 0, 1))
        self.assertTrue(self.exo.dans_cercle(2, 1, 0))
        self.assertTrue(self.exo.dans_cercle(2, 1, 1))
        self.assertTrue(self.exo.dans_cercle(2, -1, -1))
        self.assertFalse(self.exo.dans_cercle(2, 2, 2))
        self.assertFalse(self.exo.dans_cercle(2, -3, 2))
        self.assertRaises(TypeError, self.exo.dans_cercle, "abc", 3, 4)
        self.assertRaises(TypeError, self.exo.dans_cercle, 8, "abc", 4)
        self.assertRaises(TypeError, self.exo.dans_cercle, 8, 56, "abc")
        self.assertRaises(ValueError, self.exo.dans_cercle, -8, 2, 3)


class Exercice_4_test_case(unittest.TestCase):
    def test_init(self):
        with patch("Excercices.requests.get") as mocked_get:
            exo = ex.Exercice_4("Paris")
            mocked_get.assert_called_with("https://fr.wikipedia.org/w/api.php",
        par = {
            "search" : lieu,
            "format" : "json",
            "action" : "opensearch",
        })

    def test_loc(self):
        fake_answer = ["Paris",["Paris Saint-Germain Football Clucb"],]
        with patch("Excercices.requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = fake_answer
            exo = ex.Exercice_4("Paris")
            self.assertEqual(exo.localisation(),"voici ce que je connais de Paris: ")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignor'], exit=False)