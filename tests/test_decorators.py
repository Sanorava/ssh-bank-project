import pytest
from src.decorators import log

def test_log(capsys):
    @log()
    def example_func(a, b):
        return a / b
    example_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_func ok\n\n"


def test_log2(capsys):
    @log()
    def example_func(a, b):
        return a / b
    example_func(1, '2')
    captured = capsys.readouterr()
    assert captured.out == "example_func ERROR : TypeError. Inputs: (1, '2'), {}\n\n"
