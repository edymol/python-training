names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Oliver", "Isabella", "William", "Sophia", "Elijah",
    "Charlotte", "James", "Amelia", "Benjamin", "Mia", "Lucas", "Harper", "Henry", "Evelyn", "Alexander",
    "Abigail", "Michael", "Emily", "Daniel", "Elizabeth", "Ethan", "Sofia", "Jacob", "Avery", "Ella",
    "Logan", "Madison", "Jackson", "Scarlett", "Levi", "Grace", "Sebastian", "Chloe", "Mateo", "Victoria",
    "Jack", "Riley", "Carter", "Aria", "Owen", "Lily", "Wyatt", "Hannah", "Jayden", "Aubrey",
    "Luke", "Zoey", "Lincoln", "Penelope", "John", "Lillian", "Ryan", "Addison", "Isaac", "Layla",
    "Nathan", "Natalie", "Samuel", "Camila", "Adam", "Hazel", "Isaiah", "Brooklyn", "David", "Savannah",
    "Joseph", "Brooklyn", "Anthony", "Aaliyah", "Joshua", "Anna", "Hunter", "Leah", "Christian", "Zoe",
    "Gabriel", "Stella", "Julian", "Ellie", "Dylan", "Claire", "Caleb", "Violet", "Mason", "Audrey",
    "Eli", "Skylar", "Landon", "Maya", "Aaron", "Lucy", "Connor", "Paisley", "Isabella", "Caroline"
]


def clean_elements(elements):
    name_counts = {}
    if not elements:
        return None
    for name in elements:
        name = name.lower()  # Convert name to lowercase
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

    for name, count in name_counts.items():
        print(f"{name.capitalize()}: {count}")


clean_elements(names)
