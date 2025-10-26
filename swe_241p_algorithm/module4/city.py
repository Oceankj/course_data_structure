from __future__ import annotations
from typing import Optional


class City:
    def __init__(
        self,
        name: str,
        population: Optional[int] = None,
        neighbors: list[City] = [],
    ) -> None:
        self.name = name
        self.population = population
        self.neighbors = neighbors
