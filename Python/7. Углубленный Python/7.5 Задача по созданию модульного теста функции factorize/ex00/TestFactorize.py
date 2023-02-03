class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        j = 1
        for value in ('string', 1.5):
            with self.subTest(i=j):
                self.assertRaises(TypeError, factorize, value)
            j += 1
    def test_negative(self):
        j = 1
        for value in (-1, -10, -100): 
            with self.subTest(i=j):
                self.assertRaises(ValueError, factorize, value)
            j += 1

    def test_zero_and_one_cases(self):
        j = 1
        for n, value in (0,(0, )), (1, (1, )):
            with self.subTest(i=j): 
                self.assertEqual(factorize(n), value)
            j += 1

    def test_simple_numbers(self):
        j = 1
        for n, value in (3,(3, )), (13, (13, )), (29, (29, )):
            with self.subTest(i=j): 
                self.assertEqual(factorize(n), value)
            j += 1

    def test_two_simple_multipliers(self):
        j = 1
        for n, value in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(i=j): 
                self.assertEqual(factorize(n), value)
            j += 1

    def test_many_multipliers(self):
        j = 1
        for n, value in (1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(i=j): 
                self.assertEqual(factorize(n), value)
            j += 1