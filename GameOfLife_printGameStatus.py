def PrintStatus(current_state):
    print("\nThis Game's current state is:")
    try:
        for square_coordinate in current_state:
            print(square_coordinate)
    except Exception as e:
        print("Sorry some error occured.")
