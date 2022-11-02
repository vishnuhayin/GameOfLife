import numpy as np

def LifeStatus(square, initial_state, dummy_state):

    counter, deadOrAlive = 0, False

    try:
        if any(np.array_equal(state, square) for state in initial_state):
            deadOrAlive = True

        for state in initial_state:
            if any(np.array_equal(cell, state) for cell in dummy_state):
                counter += 1
                if counter == 4:
                    return False

        if counter < 2 : return False

        elif deadOrAlive and counter > 1 : return True

        else:
            if counter == 3 : return True

    except Exception as e:
        print("Sorry some error occured !!!")