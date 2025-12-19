# Classes exercises

# favourite programming language counter
class ProgrammingLanguage:
    def __init__(self):
        self.__language = {}

    def favourite_language(self, language):
        self.__language[language.lower()] = self.__language.get(language.lower(), 0) + 1

    def __str__(self):
        return f"Popular Programming languages: {self.__language}"

    def __getitem__(self, key):
        return self.__language.get(key.lower(), 0)

    def get_language_map(self):
        return self.__language


pl = ProgrammingLanguage()
pl.favourite_language("Python")
pl.favourite_language("JavaScript")
pl.favourite_language("python")
pl.favourite_language("Java")
pl.favourite_language("java")
print("Favourite Languages Count:", pl.get_language_map())
print(pl)  # calls __str__ method

print("Number of people who like Python:", pl["Python"])  # calls __getitem__ method

print("Number of people who like Python:", pl.get_language_map().get("python"))

# access using key and update value
languages = pl.get_language_map()
languages["javascript"] = 10
print("Updated Favourite Languages Count:", pl.get_language_map())
