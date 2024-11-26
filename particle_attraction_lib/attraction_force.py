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

        if self._are_particles_to_far_away(distance_between_particles):
            return 0

        if self._are_particles_too_close(distance_between_particles):
            return self._closed_repulsion_force(distance_between_particles)

        attraction_factor_between = self.attraction_law.between(a_species=a_species, another_species=another_species)
        return attraction_factor_between * self._interaction_force(distance_between_particles)

    # def _interaction_force(self, distance_between_particles):
    #     relative_distance = distance_between_particles / self.attraction_parameters.size_of_attraction
    #     relative_repulsion = self.attraction_parameters.absolute_repulsion / self.attraction_parameters.size_of_attraction
    #     force_ratio = 1 - (abs(2 * relative_distance - 1 - relative_repulsion)) / (1 - relative_repulsion)
    #
    #     return force_ratio * (1 / self.attraction_parameters.force_factor)

    def _interaction_force(self, distance_between_particles):
        post_repulsion_distance = distance_between_particles - self.attraction_parameters.absolute_repulsion
        size_of_interaction = self.attraction_parameters.size_of_attraction - self.attraction_parameters.absolute_repulsion
        half_interaction_zone= size_of_interaction / 2

        if post_repulsion_distance <= half_interaction_zone:
            force_ratio = post_repulsion_distance / half_interaction_zone
        else:
            force_ratio = 2 - post_repulsion_distance / half_interaction_zone

        return force_ratio * (1 / self.attraction_parameters.force_factor)

    def _closed_repulsion_force(self, distance_between_particles):
        return distance_between_particles / self.attraction_parameters.absolute_repulsion - 1

    def _are_particles_too_close(self, distance_between_particles):
        return distance_between_particles <= self.attraction_parameters.absolute_repulsion

    def _are_particles_to_far_away(self, distance_between_particles):
        return distance_between_particles > self.attraction_parameters.size_of_attraction
