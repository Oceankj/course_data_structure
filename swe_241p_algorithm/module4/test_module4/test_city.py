from swe_241p_algorithm.module4.city import City


# Task1
class TestCity:
    def test_city_creation(self):
        city = City(name="Taipei", population=50000)
        assert city.name == "Taipei"
        assert city.population == 50000
        assert len(city.neighbors) == 0

    def test_city_with_neighbors(self):
        neighbor1 = City(name="Keelong", population=30000)
        neighbor2 = City(name="New Taipei", population=20000)
        city = City(
            name="Taipei",
            population=50000,
            neighbors=[neighbor1, neighbor2],
        )

        assert city.name == "Taipei"
        assert city.population == 50000
        assert city.neighbors == [neighbor1, neighbor2]
        assert city.neighbors[0].name == "Keelong"
        assert city.neighbors[0].population == 30000
        assert city.neighbors[1].name == "New Taipei"
        assert city.neighbors[1].population == 20000

    def test_city_creation_without_population(self):
        city = City(name="Taipei")
        assert city.name == "Taipei"
        assert city.population is None
        assert len(city.neighbors) == 0

    def test_city_creation_without_name(self):
        # name is a required positional argument, so this should raise a TypeError
        try:
            City()
            assert False, "Expected TypeError for missing 'name' argument"
        except TypeError:
            pass  # expected

    def test_edit_city_properties_after_creation(self):
        city = City(name="Taipei", population=1000)
        # Change name
        city.name = "Keelong"
        assert city.name == "Keelong"
        # Change population
        city.population = 2000
        assert city.population == 2000
        # Add neighbors
        neighbor = City("New Taipei", 700)
        city.neighbors = [neighbor]
        assert city.neighbors == [neighbor]
        # Edit neighbor in list
        city.neighbors[0].name = "Keelong"
        assert city.neighbors[0].name == "Keelong"
