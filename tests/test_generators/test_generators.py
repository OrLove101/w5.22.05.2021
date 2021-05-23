import pytest

from src.generators import ari_prog, geo_prog, fibonacci_prog, factorial_prog


def test_ari_prog():
    generator = ari_prog(0, 10, 2)
    expected_results = [0, 2, 4, 6, 8]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)


def test_geo_prog():
    generator = geo_prog(1, 10, 2)
    expepted_results = [1, 2, 4, 8]

    for result in expepted_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)


def test_fibonacci_prog():
    generator = fibonacci_prog(1, 10)
    expected_results = [1, 1, 2, 3, 5, 8, 13, 21, 34]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)


def test_factorial_prog():
    generator = factorial_prog(1, 10)
    expected_results = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    for result in expected_results:
        assert next(generator) == result

    with pytest.raises(StopIteration):
        next(generator)