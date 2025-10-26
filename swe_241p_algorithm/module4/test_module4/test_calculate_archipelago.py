import pytest
from swe_241p_algorithm.module4.calculate_archipelago import (
    CalculateArchipelago,
)
from swe_241p_algorithm.module4.city import City
from swe_241p_algorithm.module4.city_list import Cities


class TestCalculateArchipelago:
    def make_cities(self, city_defs, roads) -> Cities:
        # city_defs = ["A", "B", "C"]
        # roads = [("A", "B"), ("B", "C")]
        # Use a *new* neighbors list for each City, don't use mutable default to avoid pollution
        cities: Cities = {}
        for name in city_defs:
            pop = 10 + ord(name[0])
            # Each City instantiates with its own neighbors list
            cities[name] = City(name=name, population=pop, neighbors=[])
        for a, b in roads:
            if b not in [n.name for n in cities[a].neighbors]:
                cities[a].neighbors.append(cities[b])
            if a not in [n.name for n in cities[b].neighbors]:
                cities[b].neighbors.append(cities[a])

        return cities

    # Task 3
    def test_archipelago_count_simple(self):
        ca = CalculateArchipelago()
        # 2 isolated cities, 1 group of 2 cities
        cities = self.make_cities(["A", "B", "C", "D"], [("A", "B")])
        count = ca.count_archipelago(cities)
        assert count == 3  # ("A","B") + "C" + "D"

    def test_archipelago_count_one_big(self):
        ca = CalculateArchipelago()
        # All connected
        cities = self.make_cities(
            ["A", "B", "C", "D"], [("A", "B"), ("B", "C"), ("C", "D")]
        )
        assert ca.count_archipelago(cities) == 1

    def test_archipelago_count_all_isolated(self):
        ca = CalculateArchipelago()
        # None connected
        cities = self.make_cities(["A", "B", "C"], [])
        assert ca.count_archipelago(cities) == 3

    # Task 4
    def test_calculate_population_multiple(self):
        ca = CalculateArchipelago()
        # ("A","B") with pops, isolated "C"
        cities = self.make_cities(["A", "B", "C"], [("A", "B")])
        pops = sorted(ca.calculate_population(cities))
        assert sorted(pops) == sorted(
            [
                cities["A"].population + cities["B"].population,
                cities["C"].population,
            ]
        )

    def test_calculate_population_big_group(self):
        ca = CalculateArchipelago()
        # Full chain: A-B-C. One archipelago
        cities = self.make_cities(["A", "B", "C"], [("A", "B"), ("B", "C")])
        assert ca.calculate_population(cities) == [
            cities["A"].population
            + cities["B"].population
            + cities["C"].population
        ]

    def test_calculate_population_missing_population(self):
        ca = CalculateArchipelago()
        # A-B, but B missing population
        cities = self.make_cities(["A", "B"], [("A", "B")])
        cities["B"].population = None
        with pytest.raises(ValueError):
            ca.calculate_population(cities)

    def test_calculate_population_empty(self):
        ca = CalculateArchipelago()
        # No cities
        cities = {}
        assert ca.calculate_population(cities) == []

    def test_count_archipelago_empty(self):
        ca = CalculateArchipelago()
        assert ca.count_archipelago({}) == 0

    # Task 5
    def test_get_distance_direct_neighbor(self):
        ca = CalculateArchipelago()
        # Simple direct connection: A-B
        cities = self.make_cities(["A", "B"], [("A", "B")])
        dist = ca.get_distance(cities["A"], cities["B"])
        assert dist == 1
        dist2 = ca.get_distance(cities["B"], cities["A"])
        assert dist2 == 1

    def test_get_distance_chain(self):
        ca = CalculateArchipelago()
        cities = self.make_cities(
            ["A", "B", "C", "D"], [("A", "B"), ("B", "C"), ("C", "D")]
        )

        assert ca.get_distance(cities["A"], cities["D"]) == 3
        assert ca.get_distance(cities["C"], cities["A"]) == 2

    def test_get_distance_same_city(self):
        ca = CalculateArchipelago()
        cities = self.make_cities(["A"], [])

        assert ca.get_distance(cities["A"], cities["A"]) == 0

    def test_get_distance_unreachable(self):
        ca = CalculateArchipelago()
        # A and B connected, C isolated
        cities = self.make_cities(["A", "B", "C"], [("A", "B")])

        assert ca.get_distance(cities["A"], cities["C"]) == 0
        assert ca.get_distance(cities["C"], cities["B"]) == 0

    def test_get_distance_empty_cities(self):
        ca = CalculateArchipelago()

        class DummyCity:
            neighbors = []

        city1 = DummyCity()
        city2 = DummyCity()
        assert ca.get_distance(city1, city2) == 0
