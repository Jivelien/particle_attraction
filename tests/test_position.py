from __future__ import annotations

import unittest

from particle_attraction_lib.particle import Position


class TestPosition(unittest.TestCase):
    def test_distance_when_position_are_spaced(self):
        p1 = Position(0, 0)
        p2 = Position(3, 4)

        sut = p1.distance_from(p2)
        self.assertAlmostEqual(5., sut)
