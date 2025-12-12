import sys
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, log, square, sin, cos, sqrt, pct

# add test
def test_add_1():
    assert add(5, 6) == 11

def test_add_2():
    assert add(5, 6) != 1

def test_sub1():
    assert sub(1,1) == 0

def test_sub2():
    assert sub(1,1) != 10

def test_mult1():
    assert mult(8,1) == 8

def test_mult2():
    assert mult(8,1) != 0

def test_div1():
    assert div(8,1) == 8

def test_div2():
    assert div(8,0) is None

def test_div3():
    assert div(8,1) != 1

def test_log1():
    assert log(8,2) == 3

def test_log2():
    assert log(8,2) != 1

def test_log3():
    assert log(100) == 2

def test_log4():
    assert log(50) == math.log(50, 10)

def test_square1():
    assert square(2) == 4

def test_square2():
    assert square(2) != 5

def test_sin1():
    assert sin(0) == 0

def test_sin2():
    assert sin(math.pi) != 10

def test_cos1():
    assert cos(0) == 1

def test_cos2():
    assert cos(math.pi) != 0

def test_sqrt1():
    assert sqrt(4) == 2

def test_sqrt2():
    assert sqrt(2) != 4

def test_sqrt3():
    assert sqrt(-3) is None

def test_pct1():
    assert pct(1) == 100

def test_pct2():
    assert pct(1) != 1
