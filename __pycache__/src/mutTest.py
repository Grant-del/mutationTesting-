# tests/test_polynomial.py

from Polynomial import Polynomial
import pytest

def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [4, -1, 2]

def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])
    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [2, 1, 2]

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])
    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]

def test_evaluate():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    assert poly.evaluate(0) == -2
    assert poly.evaluate(2) == 2

def test_find_root_bisection():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(0, 2)
    assert abs(root - 2.0**0.5) < 1e-6
