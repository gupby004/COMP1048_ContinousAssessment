import math

class Planet:
    def __init__(self, name, mass, diameter, density, gravity, distance_from_sun, mean_temperature, moon_count, ring_system, global_magnetic_field):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun
        self.mean_temperature = mean_temperature
        self.moon_count = moon_count
        self.ring_system = ring_system
        self.global_magnetic_field = global_magnetic_field

    def radius(self):
        return self.diameter / 2

    def surface_area(self):
        r = self.radius()
        return round(4 * math.pi * (r ** 2), 2)

    def calculate_mass(self, weight):
        mass = weight * self.gravity
        return f"My mass is {mass} (Newtons) on {self.name}"

    def calculate_weight(self, weight):
        weight = weight * self.gravity / 9.8
        return f"I weigh {weight} (kg) on {self.name}"

    def __str__(self):
        info = f"---{self.name.upper()}---\n"
        info += f"{self.name} has a mass of {self.mass}.\n"
        info += f"It is {self.distance_from_sun} 10\u2076 km from the sun.\n"

        if self.moon_count == 0:
            info += f"There are no moons orbiting {self.name}.\n"
        elif self.moon_count == 1:
            info += f"There is a single moon which orbits {self.name}.\n"
        else:
            info += f"There are {self.moon_count} moons orbiting {self.name}.\n"

        if self.global_magnetic_field and self.ring_system:
            info += f"{self.name} has a global magnetic field. It has ring(s) surrounding it.\n"
        elif self.global_magnetic_field:
            info += f"{self.name} has a global magnetic field.\n"
        elif self.ring_system:
            info += f"It has ring(s) surrounding it.\n"

        return info





class SolarSystem:
    def __init__(self):
        self.planets = []
        self.valid_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    def add_planet(self, planet):
        if planet.name in self.valid_planets:
            self.planets.append(planet)
        else:
            print("----------")
            print(f"L {planet.name}. You are not a real planet. \n")

    def remove_planet(self, name):
        new_list = []
        for planet in self.planets:
            if planet != name:
                new_list.append(planet)
        self.planets = new_list

    def __str__(self):
        line = ["Planets in our Solar System:"]
        for planet in self.planets:
            line.append(str(planet))
        return "\n".join(line)







