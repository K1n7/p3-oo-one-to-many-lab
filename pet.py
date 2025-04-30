class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Valid types are {', '.join(Pet.PET_TYPES)}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add pet to the owner's list of pets if owner is provided
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)

        # Store all pets in the class-level all variable
        Pet.all.append(self)

    # Class variable to store all pets
    all = []
