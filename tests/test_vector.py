from __future__ import annotations

import unittest

from particle_attraction_lib.vector import Vector


class TestVector(unittest.TestCase):
    def test_vector_can_be_added(self):
        v1 = Vector(dx=1, dy=0)
        v2 = Vector(dx=0, dy=1)

        sut = v1 + v2
        self.assertEqual(Vector(1, 1), sut)

    def test_vectory_can_be_multiply_per_a_factor(self):
        v1 = Vector(dx=1, dy=1)
        sut = v1 * 2

        self.assertEqual(Vector(2, 2), sut)
