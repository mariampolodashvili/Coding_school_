# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.

from abc import ABC, abstractmethod

class Country(ABC):
    @abstractmethod
    def enemy_of_country(self):
        pass
    @abstractmethod
    def population_of_country(self):
        pass
    @abstractmethod
    def official_language(self):
        pass


# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).

class Georgia(Country):
    def __init__(self,population, budget, capital, enemy, language):
        self.population=population
        self.enemy=enemy
        self.language=language
        self._capital=capital
        self.__budget=budget

    def enemy_of_country(self):
        print(f"Enemy of Georgia is {self.enemy}")

    def population_of_country(self):
        print(f"Population of Georgia is {self.population}")

    def official_language(self):
        print(f"Official language of Georgia is {self.language}")

# 3. შექმენი საქართველოს ობიექტი და გამოიყენე
# ზემოხსენებული მეთოდები.

georgia = Georgia(3713000, 1000000, "Tbilisi", "Russia", "Georgian")
georgia.population_of_country()
georgia.enemy_of_country()
georgia.official_language()
