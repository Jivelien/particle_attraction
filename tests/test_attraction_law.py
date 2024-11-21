import unittest

from particle_attraction_lib.attraction_law import AttractionLaw


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
