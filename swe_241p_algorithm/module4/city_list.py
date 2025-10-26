import os
from typing import TypeAlias
from swe_241p_algorithm.module4.city import City

INPUT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/input"

DataType: TypeAlias = list[tuple[str, str]]

Cities: TypeAlias = dict[str, City]


class CityList:

    _cities: Cities

    def __init__(
        self,
        population_file: str = "city_population.txt",
        network_file: str = "road_network.txt",
    ) -> None:
        self._cities = {}
        self._build_city_list(self._read_file(population_file))
        self._connect_city(self._read_file(network_file))

    def _read_file(self, file_name: str) -> DataType:
        data: DataType = []
        file_path = os.path.join(INPUT_PATH, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                [city_name, value] = line.split(" : ")
                city_name = city_name.strip()
                value = value.strip()
                if not value:
                    continue
                data.append((city_name, value))
        return data

    def _build_city_list(self, data: DataType) -> None:
        for [city_name, population] in data:
            if city_name in self._cities:
                continue
            try:
                self._cities.setdefault(
                    city_name, City(city_name, population=int(population))
                )
            except ValueError:
                continue

    def _connect_city(self, data: DataType) -> None:
        for [city_name, connected_city_name] in data:
            if city_name not in self._cities:
                self._cities.setdefault(city_name, City(city_name))
            if connected_city_name not in self._cities:
                self._cities.setdefault(
                    connected_city_name, City(connected_city_name)
                )

            city = self._cities[city_name]
            connected_city = self._cities[connected_city_name]

            if city not in connected_city.neighbors:
                connected_city.neighbors.append(city)
            if connected_city not in city.neighbors:
                city.neighbors.append(connected_city)

    def get(self):
        return self._cities
