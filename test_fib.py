import fibonacci

class TestClass:
    def test1(slef):
        assert fibonacci.fib(0) == 0

    def test2(slef):
        assert fibonacci.fib(1) == 1
    
    def test3(slef):
        assert fibonacci.fib(2) == 1

    def test4(slef):
        assert fibonacci.fib(3) == 2

    def test5(slef):
        assert fibonacci.fib(-1) == 0

    def test6(slef):
        assert fibonacci.fib(-3) == 0

    def test7(slef):
        assert fibonacci.fib(10) == 55
    
    def test8(slef):
        assert fibonacci.fac(0) == 1

    def test9(slef):
        assert fibonacci.fac(1) == 1
    
    def test10(slef):
        assert fibonacci.fac(2) == 2

    def test11(slef):
        assert fibonacci.fac(3) == 6

    def test12(slef):
        assert fibonacci.fac(-1) == 0

    def test13(slef):
        assert fibonacci.fac(-3) == 0

    def test14(slef):
        assert fibonacci.fac(10) == 3628800