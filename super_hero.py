def create_superhero(filename):
    super_heroes = {}
    with open(filename) as f:
        for line in f:
            number = line.split(",")[0].lower()
            hero = line.split(",")[1].strip().lower()
            super_heroes[number] = hero
    return super_heroes


def main():
    super_d = create_superhero('super_hero.csv')
    #print(super_d)
    f_name = input("Enter any number between 1 to 63 : ")
    first = input("enter first name: ")
    last = input("enter last name: ")
    first_name = f_name[0].lower()
    first_letter = first_name[0]
    print("Your Super Hero name is : {} {} {}".format(first, super_d[first_letter], last))


main()


