def Initialize():

    while True:
        try:
            squares = int(input("Enter the number of squares cells you want to make alive: "))
            column = 0
            square_cordinates = []
            for square in range(squares):
                cordinates = []
                column += 1
                for coordinate in ['x', 'y']:
                    cordinates.append(int(input(f"Enter the {coordinate} value of square {column}: ")))
                square_cordinates.append(cordinates)

            print("\nSquare Coordinates Entered:\n")
            for cordinates in square_cordinates:
                print(cordinates)

            return square_cordinates

        except Exception as e:
            print("Sorry. The values entered earlier contain some error !!!")
