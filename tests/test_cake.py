import pytest
from bakery.cake import Cake


@pytest.fixture()
def cake():
    return Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', 'free', 'loveYou')


def test_init(cake):
    assert cake.name == "Vanilla Cake"
    

def test_additives():
    cake1 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', 'free', 'loveYou')
    assert cake1.additives == ['chocolate', 'nuts']
