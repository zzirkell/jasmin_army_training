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
    counts = {}
    for dog in dogs:
        if dog["breed"] not in counts:
            counts[dog["breed"]] = 1
        else:
            counts[dog["breed"]] += 1
    return counts

    # TODO:
    # Create an empty dictionary called counts.
    # Loop through dogs.
    # Get the breed from each dog.
    # Count how often each breed appears.
    # Return counts.

def find_dogs_by_size(dogs, wanted_size):
    dogs_by_size = []
    for dog in dogs:
        if dog["size"] == wanted_size:
            dogs_by_size.append(dog["name"])
    return dogs_by_size

def collect_unique_temperaments(dogs):
    unique_temperaments = set()
    for dog in dogs:
        for temperament in dog["temperaments"]:
            unique_temperaments.add(temperament)
    return unique_temperaments

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