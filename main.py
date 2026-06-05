class Fan:
    def __init__(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

f = Fan("Matematika")
print(f.get_nom())

f.set_nom("Informatika")
print(f.get_nom())
