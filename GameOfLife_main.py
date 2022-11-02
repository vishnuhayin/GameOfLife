from GameOfLife_gameData import GameState
from GameofLife_initializeGameData import Initialize
from GameOfLife_gamePlay import GamePlay

def main():
    state = ''
    try:
        while True:
            print("------------------------------------------------\n"
                  "\t\t\t\tGAME OF LIFE\n"
                  "------------------------------------------------\n")
            while True:
                initial_state = Initialize()
                state = GameState(initial_state)
                check = input("\nPress Enter to start the game. (Enter N to re-entering the coordinates) >>> ")
                if check.strip().lower() != 'n' : break
            GamePlay(state.current_state)
            check = input("\nPress Enter to start another game. (Enter q to quit game of life app) >>> ")
            if check.strip().lower() == 'q': break
    except Exception as e:
        print("Sorry some error occured !!!")


if __name__ == '__main__':
    main()