people = [
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Cho", "house":"Ravenclaw"}
]

def f(person):
    return person["name"]

people.sort(key = f)

# OR we use Lambda the same way

people.sort(key = lambda person: person["name"])
print(people)