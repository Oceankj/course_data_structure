import os
import shutil
import tempfile
import pytest

from swe_241p_algorithm.module4.city import City
from swe_241p_algorithm.module4 import city_list as city_list_mod

CityList = city_list_mod.CityList


# === Global fixture: create temp test directory + mock INPUT_PATH ===
@pytest.fixture
def mock_inputs_path(monkeypatch):
    temp_dir = tempfile.mkdtemp()
    monkeypatch.setattr(city_list_mod, "INPUT_PATH", temp_dir)
    yield temp_dir
    shutil.rmtree(temp_dir)


# === fixture: create temporary city files ===
@pytest.fixture
def temp_city_files(mock_inputs_path):
    pop_path = os.path.join(mock_inputs_path, "city_population.txt")
    net_path = os.path.join(mock_inputs_path, "road_network.txt")
    with open(pop_path, "w", encoding="utf-8") as f:
        f.write("Taipei : 25000\n")
        f.write("Keelung : 12000\n")
        f.write("New Taipei : 40000\n")
    with open(net_path, "w", encoding="utf-8") as f:
        f.write("Taipei : Keelung\n")
        f.write("Keelung : New Taipei\n")
        f.write("New Taipei : Taipei\n")
    return pop_path, net_path


# Task 2
class TestCityList:
    def test_citylist_builds_and_connects(self, temp_city_files):
        clist = CityList("city_population.txt", "road_network.txt")
        cities = clist.get()

        assert isinstance(cities, dict)
        assert set(cities.keys()) == {"Taipei", "Keelung", "New Taipei"}

        taipei = cities["Taipei"]
        keelung = cities["Keelung"]
        newtaipei = cities["New Taipei"]

        # Check populations
        assert taipei.population == 25000
        assert keelung.population == 12000
        assert newtaipei.population == 40000

        # Check neighbors are bi-directional and correct
        assert keelung in taipei.neighbors
        assert taipei in keelung.neighbors
        assert newtaipei in keelung.neighbors
        assert keelung in newtaipei.neighbors
        assert taipei in newtaipei.neighbors
        assert newtaipei in taipei.neighbors

    def test_citylist_handles_valueerror_file(self, mock_inputs_path):
        pop_path = os.path.join(mock_inputs_path, "pop.txt")
        net_path = os.path.join(mock_inputs_path, "net.txt")
        with open(pop_path, "w", encoding="utf-8") as f:
            f.write("Taipei : N/A\nKeelung : 12000\n")
        with open(net_path, "w", encoding="utf-8") as f:
            f.write("Taipei : Keelung\nKeelung : Taipei\n")

        clist = CityList("pop.txt", "net.txt")
        cities = clist.get()

        assert "Taipei" in cities
        assert "Keelung" in cities
        assert cities["Keelung"].population == 12000
        assert isinstance(cities["Taipei"], City)

    def test_citylist_missing_value(self, mock_inputs_path):
        pop_path = os.path.join(mock_inputs_path, "pop.txt")
        net_path = os.path.join(mock_inputs_path, "net.txt")
        with open(pop_path, "w", encoding="utf-8") as f:
            f.write("Taipei : \nKeelung : 1000\n")
        with open(net_path, "w", encoding="utf-8") as f:
            f.write("Keelung : Taipei\n")

        clist = CityList("pop.txt", "net.txt")
        cities = clist.get()

        assert "Taipei" in cities
        assert "Keelung" in cities
        assert cities["Keelung"].population == 1000
        assert isinstance(cities["Taipei"], City)
