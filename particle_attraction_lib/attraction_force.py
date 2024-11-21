from dataclasses import dataclass

from particle_attraction_lib.attraction_law import AttractionLawInterface
from particle_attraction_lib.vector import Vector


@dataclass
class AttractionParameters:
    size_of_attraction: int = 0
    absolute_repulsion: float = 0
    force_factor: int = 1


class AttractionForce:
    def __init__(self, attraction_parameters: AttractionParameters, attraction_law: AttractionLawInterface):
        self.attraction_parameters = attraction_parameters
        self.attraction_law = attraction_law

    def attraction_between(self, vector: Vector, a_species: int, another_species: int):
        distance_between_particles = vector.length

        if distance_between_particles > self.attraction_parameters.size_of_attraction:
            return 0

        if distance_between_particles <= self.attraction_parameters.absolute_repulsion:
            F = distance_between_particles / self.attraction_parameters.absolute_repulsion - 1
            return F * (1 / self.attraction_parameters.force_factor)

        relative_distance = distance_between_particles / self.attraction_parameters.size_of_attraction
        relative_repulsion = self.attraction_parameters.absolute_repulsion / self.attraction_parameters.size_of_attraction

        force_ratio = 1 - (abs(2 * relative_distance - 1 - relative_repulsion)) / (1 - relative_repulsion)

        return self.attraction_law.between(a_species=a_species, another_species=another_species) * force_ratio
