from solutions.CHK import checkout_solution_two


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution_two.checkout('ABCD') == 115
        assert checkout_solution_two.checkout('x') == -1
        assert checkout_solution_two.checkout('AAA') == 130
        assert checkout_solution_two.checkout('AxA') == -1
        assert checkout_solution_two.checkout('AAAA') == 180
        assert checkout_solution_two.checkout('AAAAA') == 200
        assert checkout_solution_two.checkout('AAAAAA') == 260
        assert checkout_solution_two.checkout('EEB') == 80
        assert checkout_solution_two.checkout('BB') == 45




