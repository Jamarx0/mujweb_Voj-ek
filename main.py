jmeno = input("Zadejte jméno: ")
presents = ["auto", "pc", "panenka", "vysavač", "jídlo", "auto", "vysavač"]
unique_presents = set(presents)
print(unique_presents)

names = ["Petr", "Marie", "Káta", "Maminka", "Ivan"]
for name, present in zip(names, presents):
    print(f"{name} dostane {present}")

def get_present(name):
    if name in names:
        return presents[names.index(name)]
    return "Neznám toto jméno."
print(get_present(jmeno))
