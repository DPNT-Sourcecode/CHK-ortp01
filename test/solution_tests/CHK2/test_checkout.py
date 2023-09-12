from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('x') == -1
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AxA') == -1
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 230
        assert checkout_solution.checkout('AAAAAA') == 260


