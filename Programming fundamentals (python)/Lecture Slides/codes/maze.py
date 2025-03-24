class Location:  # a pair of coordinates
    pass
    
def setLocation(x, y):
    point = Location()
    point.x_index = x
    point.y_index = y
    return point

def isValidLocation(point):
    if (
        point.x_index > -1
        and point.x_index < 23
        and point.y_index > -1
        and point.y_index < 50
    ):
        return True
    return False


def solveMaze(mz, starting_location):

    moves = [0] * 10000
    moves_count = 0
    
    moves[moves_count] = starting_location
    moves_count = moves_count + 1

    while moves_count > 0:
        moves_count = moves_count - 1
        lc = moves[moves_count]

        if mz[lc.x_index][lc.y_index] == "E":
            break

        if mz[lc.x_index][lc.y_index] != "S":
            mz[lc.x_index][lc.y_index] = "@"

        up = setLocation(lc.x_index - 1, lc.y_index)
        right = setLocation(lc.x_index, lc.y_index + 1)
        down = setLocation(lc.x_index + 1, lc.y_index)
        left = setLocation(lc.x_index, lc.y_index - 1)

        if isValidLocation(up) and (
            mz[up.x_index][up.y_index] == " " 
            or mz[up.x_index][up.y_index] == "E"
        ):
            moves[moves_count] = up
            moves_count = moves_count + 1
        
        if isValidLocation(right) and (
            mz[right.x_index][right.y_index] == " "
            or mz[right.x_index][right.y_index] == "E"
        ):
            moves[moves_count] = right
            moves_count = moves_count + 1

        if isValidLocation(down) and (
            mz[down.x_index][down.y_index] == " "
            or mz[down.x_index][down.y_index] == "E"
        ):
            moves[moves_count] = down
            moves_count = moves_count + 1
        
        if isValidLocation(left) and (
            mz[left.x_index][left.y_index] == " "
            or mz[left.x_index][left.y_index] == "E"
        ):
            moves[moves_count] = left
            moves_count = moves_count + 1

def printMaze(mz, height, width):
    for i in range(height):
        for j in range(width):
            print(mz[i][j], end="")
        print()

def searchMaze(ch, mz, height, width):
    loc = Location()
    for i in range(height):
        for j in range(width):
            if mz[i][j] == ch:
                loc = setLocation(i, j)
    return loc

def main():
    # maze is not a 2D list of 23 rows and 50 columns but list of 23 strings with each of len 50
    maze = [
        list("**************************************************"),
        list("*******                              ******** ****"),
        list("******* ************* ************** ******** ****"),
        list("******* ************* ***          * ***      ****"),
        list("        ************* **  *******  * *** **** ****"),
        list("******* *** ***    ** *  ********        **** ****"),
        list("******* *** ****** ** *  ******************** ****"),
        list("******* *** ****** **    ******************** ****"),
        list("******* *** ****** ************************** ****"),
        list("******* *** **                      ********* ****"),
        list("***     *** ** **** **** ******************** ****"),
        list("*** ********** **** ****                ***** ****"),
        list("*** ********** **** ************************* ****"),
        list("*** ********** **** ************************* ****"),
        list("***            **** ************ ************S****"),
        list("******** ********** ************ ************ ****"),
        list("******** ********** ************      ******* ****"),
        list("********     ****** ************ **** ******* ****"),
        list("*******************              **** ******* ****"),
        list("************************************* ******* ****"),
        list("************************************* ************"),
        list("*************************************        E    "),
        list("**************************************************"),
    ]

    stLoc = searchMaze("S", maze, 23, 50)

    printMaze(maze, 23, 50)
    solveMaze(maze, stLoc)

    print("\n==================================================\n")
    print("Solution\n")
    printMaze(maze, 23, 50)

main()
