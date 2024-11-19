import unittest
from typing import Tuple, Dict

from particle_attraction_lib.attraction_law import AttractionLawInterface


class AttractionLaw(AttractionLawInterface):
    def __init__(self):
        self.laws: Dict[Tuple[int, int], float] = {}

    def between(self, a_species: int, another_species: int):
        return self.laws.get((a_species, another_species), 0)

    def add(self, a_species: int, another_species: int, attraction: float):
        self.laws[a_species, another_species] = attraction


class TestAttractionLaw(unittest.TestCase):
    def test_return_zero_if_not_defined(self):
        a = AttractionLaw()

        sut = a.between(a_species=0, another_species=0)

        self.assertEqual(sut, 0)

    def test_can_add_law(self):
        a = AttractionLaw()
        a.add(a_species=0, another_species=0, attraction=1)

        sut = a.between(a_species=0, another_species=0)
        self.assertEqual(sut, 1)
