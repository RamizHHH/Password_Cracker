
def apply_rule(word, rules):

    varations = set()

    word = word.strip()

    varations.add(word)

    if rules == "basic":


        varations.update(capitalizeVar(word))

        varations.update(numberSuffix(word))

        varations.update(symbolSuffix(word))

    elif rules == "aggresive":

        varations.update(capitalizeVar(word))

        varations.update(numberSuffix(word))

        varations.update(symbolSuffix(word))

        varations.update(addLeet(word))

        varations.update(addYears(word))

    else:
        raise ValueError("Type Not Real")


    return list(varations)


def capitalizeVar(word):
    capitalizedWords = [
        word.capitalize(),
        word.upper()
    ]

    return capitalizedWords

def numberSuffix(word):
    numberWords = [
        word + '1',
        word + '2',
        word + '12',
        word + '3',
        word + '13',
        word + '123',
        word + '4',
        word + '1234'
    ]

    return numberWords

def symbolSuffix(word):
    symbolWords = [
        word + '!',
        word + '@',
        word + '#'
    ]

    return symbolWords

def addLeet(word):
    leet = (
        word.replace('a', '@').replace('o', '0').replace('e', '3').replace('i', '1').replace('s', '$')
    )

    return leet

def addYears(word):
    years = [
        word + "2024",
        word + "2025",
        word + "2026"
    ]
    
    return years