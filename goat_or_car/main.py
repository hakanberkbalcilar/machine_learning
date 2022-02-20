from asyncio import run
import random;

options = ['Goat', 'Goat', 'Car']

def start():
    printTitle('')

    print('Exit => 0')
    print('Single Selection => 1')
    print('Double Selection => 2')
    result = input('Choose one of the options: ')
    if(result == '1'):
        runSingleSelectionGame()
    elif(result == '2'):
        runDoubleSelectionGame()
    elif(result == 'q'): return
    else:
        print('\nInvalid value!')
        start()

def printTitle(gameType):
    print('\n\n\n------------------------------------------')
    print(f'Goat Or Car Game {gameType}')
    print('------------------------------------------\n')

def printProbability(carCount):
    probability = carCount * .1
    print(f'\nProbability of choosing car is %{probability}')


def getSelection(gameType):
    printTitle(gameType)
    result = input('[1, 2, 3] Choose one of the options: ')
    if(len(result) == 1 and '4' > result > '0'): return int(result)
    print('\nInvalid value!')
    return getSelection(gameType)

def runSingleSelectionGame():
    result = getSelection('Single Selection')
    selections = []
    for i in range(1000):
        random.shuffle(options)
        selections.append(options[result])
    printProbability(selections.count('Car'))
    start()

def runDoubleSelectionGame():
    selections = []

    result = getSelection('Double Selection')

    for i in range(1000):
        random.shuffle(options)
        indexes = [0, 1, 2]
        indexes.pop(result-1)
        if(options[indexes[0]] == 'Car'):
            indexes.pop(1)
        else:
            indexes.pop(0)
        index = indexes[0]
        selections.append(options[index])
    printProbability(selections.count('Car'))
    start()

start()
    