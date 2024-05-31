from typing import Union
from typing import Optional

"""
    list-compreesition para melhorar a legibilidade e eficiencia do código.
"""


def numeros_paire(items: list) -> Optional[list[Union[int | float]]]:
    if not isinstance(items, list):
        return False
    return [item for item in items if isinstance(item, Union[int|float]) and item % 2 == 0]


def test_numeros_paire_1_success():
    items = [1, 2, 3, 4, 5, 6, 7]
    resultats = numeros_paire(items)
    assert [2, 4, 6] == resultats


def test_numeros_paire_liste_mixte():
    items = ['a', 2, 'b', 4, 'c', 6, 'd', 8.0]
    resultats = numeros_paire(items)
    assert [2, 4, 6, 8.0] == resultats


def test_numeros_paire_liste_vide():
    items = []
    resultats = numeros_paire(items)
    assert [] == resultats


def test_numeros_paire_chose_invalide():
    chose = False
    resultats = numeros_paire(chose)
    assert False == resultats
