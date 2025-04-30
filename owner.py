class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Returns a full list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner. Checks that the pet is a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of the Pet class.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)
