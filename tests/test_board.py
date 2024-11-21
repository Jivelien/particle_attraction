import unittest

from particle_attraction_lib.board import Board


class TestBoard(unittest.TestCase):
    def test_tuple_conversion(self):
        b = Board(100, 200)

        sut = tuple(b)

        self.assertEqual((100, 200), sut)
