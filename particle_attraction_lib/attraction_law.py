from abc import ABC, abstractmethod

from particle_attraction_lib.particle import Particle


class AttractionLawInterface(ABC):
    @abstractmethod
    def between(self, a_species: int, another_species: int):
        raise NotImplementedError
