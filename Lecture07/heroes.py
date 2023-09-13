hero = ['Ironman','Thor','Hulk','Superman','Spiderman']
loop = 'y'
def main():
    print('Select your actions! (1-6)')
    print('1. Display Heroes')
    print('2. Add Heroes')
    print('3. Insert Heroes')
    print('4. Remove Heroes')
    print('5. Display Sorted Heroes (Ascending / Descending)')
    print('6. Exit')

    while loop.lower()=='y':
        first = int(input('Type number here (1-6) : '))
        if first == 1:
            showhero(hero)
        if first == 2:
            add = str(input('Enter the name of Hero: '))
            addhero(add)
        if first == 3:
            insert = str(input('Select name of hero'
                                'of you want to insert: '))
            insert2 = str(input('Select a position on list: '))
            inserthero(insert,insert2)
        if first == 4:
            remove = str(input('Select hero you want to remove: '))
            removehero(remove)
        if first == 5:
            sort = str(input('AScending/Decending (A/D): '))
            if sort.upper == 'A':
                Sorted_HeroAscend(hero)
            if sort.upper == 'D':
                Sorted_HeroDecend(hero)
        if first == 6:
            break
        print(hero)

def showhero(hero):
    return hero

def addhero(name):
    return hero.append(name)

def removehero(name):
    return hero.remove(name)

def inserthero(index,name):
    return hero.insert(index, name)

def Sorted_HeroAscend(name):
    return hero.sort(name)

def Sorted_HeroDecend(name):
    return hero.sort(name, reverse=True)

main()