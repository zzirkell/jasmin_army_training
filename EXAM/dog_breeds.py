"""
Mini Exam 05: Dog Breed Helper

Theme:
A small helper for dog breed information.

Goal:
Use a list of dictionaries, loops, conditions, sets, counting, and functions.

No classes yet.
"""


def count_dogs_by_breed(dogs):
    """
    dogs is a list of dictionaries.

    Example:
    [
        {"name": "Milo", "breed": "beagle"},
        {"name": "Luna", "breed": "poodle"}
    ]

    Return a dictionary that counts how many dogs there are per breed.
    """

    # TODO:
    # Create an empty dictionary called counts.
    # Loop through dogs.
    # Get the breed from each dog.
    # Count how often each breed appears.
    # Return counts.

    pass


def find_dogs_by_size(dogs, wanted_size):
    """
    Return a list with dog names where dog["size"] equals wanted_size.
    """

    # TODO:
    # Create an empty list.
    # Loop through dogs.
    # If the dog's size matches wanted_size, append the dog's name.
    # Return the list.

    pass


def collect_unique_temperaments(dogs):
    """
    Each dog has a list of temperaments.

    Example:
    {
        "name": "Milo",
        "temperaments": ["friendly", "curious"]
    }

    Return a set of all unique temperaments.
    """

    # TODO:
    # Create an empty set.
    # Loop through dogs.
    # For each dog, loop through dog["temperaments"].
    # Add each temperament to the set.
    # Return the set.

    pass


def main():
    print("Mini Exam 05: Dog Breed Helper")
    print("------------------------------")

    dogs = [
        {
            "name": "Milo",
            "breed": "beagle",
            "size": "medium",
            "temperaments": ["friendly", "curious"]
        },
        {
            "name": "Luna",
            "breed": "poodle",
            "size": "small",
            "temperaments": ["smart", "friendly"]
        },
        {
            "name": "Rex",
            "breed": "german shepherd",
            "size": "large",
            "temperaments": ["loyal", "smart"]
        },
        {
            "name": "Bella",
            "breed": "beagle",
            "size": "medium",
            "temperaments": ["curious", "playful"]
        },
        {
            "name": "Nori",
            "breed": "shiba inu",
            "size": "small",
            "temperaments": ["independent", "loyal"]
        }
    ]

    breed_counts = count_dogs_by_breed(dogs)
    small_dogs = find_dogs_by_size(dogs, "small")
    unique_temperaments = collect_unique_temperaments(dogs)

    print(f"Breed counts: {breed_counts}")
    print(f"Small dogs: {small_dogs}")
    print(f"Unique temperaments: {unique_temperaments}")

    number_of_dogs = len(dogs)
    number_of_temperaments = len(unique_temperaments)

    print(f"Number of dogs: {number_of_dogs}")
    print(f"Number of unique temperaments: {number_of_temperaments}")

    if "friendly" in unique_temperaments:
        print("At least one dog is friendly.")

    if number_of_dogs >= 5:
        print("This is a nice dog dataset.")


if __name__ == "__main__":
    main()