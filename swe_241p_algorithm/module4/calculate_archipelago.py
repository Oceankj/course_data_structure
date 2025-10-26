from itertools import count
from queue import Queue
from typing import Optional
from swe_241p_algorithm.module4.city import City
from swe_241p_algorithm.module4.city_list import Cities


class CalculateArchipelago:
    def count_archipelago(self, cities: Cities) -> int:
        visited: set[City] = set()
        count = 0

        for city in cities.values():
            if city not in visited:
                self._dfs(city, visited)
                count += 1
        return count

    def _dfs(self, city: City, visited: set[City]):
        if city in visited:
            return
        visited.add(city)
        for neighbor in city.neighbors:
            self._dfs(neighbor, visited)

    def calculate_population(self, cities: Cities) -> list[int]:
        visited: set[City] = set()
        populations: list[int] = []

        for city in cities.values():
            if city not in visited:
                populations.append(self._dfs_population(city, visited))
        return populations

    def _dfs_population(self, city: City, visited: set[City]) -> int:
        if city in visited:
            return 0

        if city.population is None:
            raise ValueError(f"City {city.name} has no population")

        visited.add(city)
        population: int = city.population
        for neighbor in city.neighbors:
            if neighbor.population is None:
                raise ValueError(f"neighbor {neighbor.name} has no population")
            population += self._dfs_population(neighbor, visited)
        return population

    @staticmethod
    def get_distance(city1: City, city2: City) -> int:
        visited: set[City] = set()
        queue: Queue[tuple[City, int]] = Queue()
        queue.put((city1, 0))
        visited.add(city1)

        while not queue.empty():
            curr_city, dist = queue.get()
            visited.add(curr_city)

            for neighbor in curr_city.neighbors:
                if neighbor is city2:
                    return dist + 1
                if neighbor not in visited:
                    queue.put((neighbor, dist + 1))

        return 0
