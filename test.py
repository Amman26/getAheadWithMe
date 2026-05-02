import pytest
from src.calculations import Calculations

class TestCalculations:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.calc = Calculations()

    @pytest.mark.parametrize("n1,n2,exval",
                             [(5,5,10), (-5,-5,-10), (0,5,5)])
    def test_add(self, n1, n2, exval):
        assert self.calc.add(n1, n2) == exval

    @pytest.mark.parametrize("n1,n2,exval",
                             [(5,5,0), (-5,-5,0), (0,5,-5)])
    def test_sub(self, n1, n2, exval):
        assert self.calc.sub(n1, n2) == exval

    def test_mul(self):
        assert self.calc.mul(10,5) == 50

    def test_div(self):
        assert self.calc.div(10,5) == 2

    def test_ne(self):
        assert self.calc.ne(10,10) is False
        assert self.calc.ne(10,5) is True

    def test_diverr(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10, 0)
