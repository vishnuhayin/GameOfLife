import numpy as np
from GameOfLife_lifeStatus import LifeStatus
from GameOfLife_printGameStatus import PrintStatus

def GamePlay(initial_state):
    basic_matrix = np.array([
                             [-1, 1], [0, 1], [1, 1],
                             [-1, 0], [0, 0], [1, 0],
                             [-1, -1], [0, -1], [1, -1]
                            ])
    try:
        while True:
            final_state = []

            for state in initial_state:
                dummy_state = (basic_matrix + state).tolist()
                dummy_state.remove(state.tolist())
                dummy_state = np.array(dummy_state)
                life_status = LifeStatus(state, initial_state, dummy_state)

                if life_status and state.tolist() not in final_state:

                    final_state.append(state.tolist())

                    for element in dummy_state:

                        small_dummy = (basic_matrix + element).tolist()
                        small_dummy.remove(element.tolist())
                        small_dummy = np.array(small_dummy)

                        life_status = LifeStatus(element, initial_state, small_dummy)

                        if life_status and element.tolist() not in final_state:
                            final_state.append(element.tolist())

            PrintStatus(final_state)

            initial_state = np.array(final_state)


            stop = input("Press Enter to proceed this game.(enter q to quit) >>>")
            if stop.strip().lower() == 'q' or final_state == []:
                break

    except Exception as e:
        print("Sorry some error occurred !!!")
