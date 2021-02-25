import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test1(self):
        result = fibonacci.fib(0)
        self.assertEqual(result, 0)

    def test2(self):
        result = fibonacci.fib(1)
        self.assertEqual(result, 1)

    def test3(self):
        result = fibonacci.fib(2)
        self.assertEqual(result, 1)

    def test4(self):
        result = fibonacci.fib(3)
        self.assertEqual(result, 2)

    def test5(self):
        result = fibonacci.fib(-1)
        self.assertEqual(result, 0)

    def test6(self):
        result = fibonacci.fib(-3)
        self.assertEqual(result, 0)

    def test7(self):
        result = fibonacci.fib(10)
        self.assertEqual(result, 55)

    def test8(self):
        result = fibonacci.fac(0)
        self.assertEqual(result, 1)

    def test9(self):
        result = fibonacci.fac(1)
        self.assertEqual(result, 1)

    def test10(self):
        result = fibonacci.fac(2)
        self.assertEqual(result, 2)

    def test11(self):
        result = fibonacci.fac(3)
        self.assertEqual(result, 6)

    def test12(self):
        result = fibonacci.fac(-1)
        self.assertEqual(result, 0)

    def test13(self):
        result = fibonacci.fac(-3)
        self.assertEqual(result, 0)

    def test14(self):
        result = fibonacci.fac(10)
        self.assertEqual(result, 3628800)

if __name__ == "__main__":
    unittest.main()   