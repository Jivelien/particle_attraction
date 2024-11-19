from dataclasses import dataclass

from particle_attraction_lib.distance import DistanceInterface
from particle_attraction_lib.particle import Particle
from particle_attraction_lib.attraction_law import AttractionLawInterface


@dataclass
class AttractionParameters:
    size_of_attraction: int = 0
    absolute_repulsion: float = 0
    force_factor: int = 1


class AttractionForce:
    def __init__(self, attraction_parameters: AttractionParameters, attraction_law: AttractionLawInterface,
                 distance: DistanceInterface):
        self.attraction_law = attraction_law
        self.distance = distance
        self.attraction_parameters = attraction_parameters

    def attraction_between(self, a_particle: Particle, another_particle: Particle):
        vector = self.distance.vector_between(a_particle.position, another_particle.position)
        distance_between_particles = self.distance.distance_of_vector(vector)

        if distance_between_particles > self.attraction_parameters.size_of_attraction:
            return 0

        if distance_between_particles <= self.attraction_parameters.absolute_repulsion:
            return (distance_between_particles / self.attraction_parameters.absolute_repulsion - 1) # * self.attraction_parameters.force_factor

        attraction = self.attraction_law.between(a_species=a_particle.species, another_species=another_particle.species)

        relative_distance = distance_between_particles / self.attraction_parameters.size_of_attraction
        relative_repulsion = self.attraction_parameters.absolute_repulsion / self.attraction_parameters.size_of_attraction

        force_ratio = 1 - (abs(2 * relative_distance - 1 - relative_repulsion)) / (1 - relative_repulsion)

        return attraction * force_ratio
