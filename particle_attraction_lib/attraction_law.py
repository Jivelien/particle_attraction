from abc import ABC, abstractmethod
from typing import Dict, Tuple


class AttractionLawInterface(ABC):
    @abstractmethod
    def between(self, a_species: int, another_species: int) -> float:
        raise NotImplementedError


class AttractionLaw(AttractionLawInterface):
    def __init__(self) -> None:
        self.laws: Dict[Tuple[int, int], float] = {}

    def between(self, a_species: int, another_species: int) -> float:
        return self.laws.get((a_species, another_species), 0)

    def add(self, a_species: int, another_species: int, attraction: float) -> None:
        self.laws[a_species, another_species] = attraction
