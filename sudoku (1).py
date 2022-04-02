# import libraries here. Use the following ones only.
import time
import sys
import random

# add your implementation of the required functions here

#A class that hosts variables like attempts so they can be altered and used in different functions
class helper_variables:
    attempts = 0 #Will be used to count the number of moves user/computer has taken
    lives_left = 5 #Used in human_play(), when lives reach 0 it will be game over.

#Function that ends the running program
def game_kill():
    return

#Function that prints the sudoku board to the terminal
def print_board(sudoku):
    for i in range(9):
        print(sudoku[i][0:3], '|', sudoku[i][3:6], '|', sudoku[i][6:9])
        if i == 5 or i == 2:
            print('-'*51)
    print("\n")

# Function checks for number of blanks in sudoku puzzle at start
def blank_checker(sudoku):
    global blanks
    blanks = 0 # Blank counter set to 0
    for rows in sudoku:
        for i in range(9):
            if rows[i] == " ":  # Checks each element of each row to check if there are blanks
                blanks += 1  # Adds to the blank counter
            else:
                pass    
    return blanks #Returns the value of blanks to be used in the humanplay function

# Function checks if the value in the inputted location is blank or already has a value
def is_blank(select_space):
    if select_space == " ":  # If the slot is blank it is empty
        print("This slot is empty")

    else:
        print("This slot is filled")
        # The print board function is called again to print the updated sudoku board
        print_board(sudoku)
        human_play(sudoku, blanks)


def is_valid(input_num, input_col, input_row):
    num_here = 0 #Increment that will be added to if the inputted number is in row, column or 3x3 square 
    j = 0

    #Validates if the user input is an int or a number between 1-9, if not correct, the user is asked to input again
    while j == 0:
        if type(input_num) != int:
            print("That is not a valid input")
            input_num = int(input("Enter a number between 1-9  to put in the space:"))
        else:
            if (input_num < 1) or (input_num > 9):
                print("That is not a valid input")
                input_num = int(input("Enter a number between 1-9  to put in the space:"))
            elif input_num == " ":
                print("That is not a valid input")
                input_num = int(input("Enter a number between 1-9 to put in the space:"))
            else:
                print("Correct input")
                j = 1  # Allows for this branched while loop to be stopped

    # For loop going through each element in the row to see if the number has already been used
    i = 0  # For loop increment is set to 0
    num_used = 0  # Will be added to if the number has already been used in row
    table_row = sudoku[input_row]
    table_row_print = [] #Used to print out the numbers for table_row (testing)
    for i in range(0, len(table_row)):
        table_row_print.append(table_row[i])
        if str(input_num) == table_row[i]:
            print("This number has already been used in this row")
            num_used += 1
        else:
            continue
    if num_used > 0:
        print("The number cannot be used")

        # The print board function is called again to print the updated sudoku board
        print_board(sudoku)
        num_here += 1
    else:
        print("The number can be used")
    print(table_row_print)

    table_col = []  # The elements of the column will be added to a list
    for rows in sudoku:
        table_col.append(rows[input_col])  # Adds each item in column to list
    print(table_col)

    # Increments for the for loop
    i = 0  # For loop increment is set to 0
    num_used = 0  # Will be added to if the number has already been used in row

    # For loop going through each element in the column to see if the number has already been used
    for i in range(0, len(table_col)):
        if str(input_num) == table_col[i]:
            print("This number has already been used in this row")
            num_used += 1  # If number has been used it is added to the number used counter
        else:
            continue
    if num_used > 0:
        print("The number cannot be used")

        # The print board function is called again to print the updated sudoku board
        print_board(sudoku)
        num_here += 1
    else:
        print("The number can be used")

    # Check which 3x3 square the inputted location (inputrow,inputcol) is in
    square_num_list = []  # List where the numbers from 3x3 square will go into
    if (input_row >= 0) and (input_row < 3):
        if (input_col >= 0) and (input_col < 3):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[0][0], sudoku[0][1], sudoku[0][2], sudoku[1]
                                             [0], sudoku[1][1], sudoku[1][2], sudoku[2][0], sudoku[2][1], sudoku[2][2]]
        elif (input_col >= 3) and (input_col < 6):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[0][3], sudoku[0][4], sudoku[0][5], sudoku[1]
                                             [3], sudoku[1][4], sudoku[1][5], sudoku[2][3], sudoku[2][4], sudoku[2][5]]
        elif (input_col >= 6) and (input_col < 9):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[0][6], sudoku[0][7], sudoku[0][8], sudoku[1]
                                             [6], sudoku[1][7], sudoku[1][8], sudoku[2][6], sudoku[2][7], sudoku[2][8]]
    elif (input_row >= 3) and (input_row < 6):
        if (input_col >= 0) and (input_col < 3):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[3][0], sudoku[3][1], sudoku[3][2], sudoku[4]
                                             [0], sudoku[4][1], sudoku[4][2], sudoku[5][0], sudoku[5][1], sudoku[5][2]]
        elif (input_col >= 3) and (input_col < 6):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[3][3], sudoku[3][4], sudoku[3][5], sudoku[4]
                                             [3], sudoku[4][4], sudoku[4][5], sudoku[5][3], sudoku[5][4], sudoku[5][5]]
        elif (input_col >= 6) and (input_col < 9):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[3][6], sudoku[3][7], sudoku[3][8], sudoku[4]
                                             [6], sudoku[4][7], sudoku[4][8], sudoku[5][6], sudoku[5][7], sudoku[5][8]]
    elif (input_row >= 6) and (input_row < 9):
        if (input_col >= 0) and (input_col < 3):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[6][0], sudoku[6][1], sudoku[6][2], sudoku[7]
                                             [0], sudoku[7][1], sudoku[7][2], sudoku[8][0], sudoku[8][1], sudoku[8][2]]
        elif (input_col >= 3) and (input_col < 6):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[6][3], sudoku[6][4], sudoku[6][5], sudoku[7]
                                             [3], sudoku[7][4], sudoku[7][5], sudoku[8][3], sudoku[8][4], sudoku[8][5]]
        elif (input_col >= 6) and (input_col < 9):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[6][6], sudoku[6][7], sudoku[6][8], sudoku[7]
                                             [6], sudoku[7][7], sudoku[7][8], sudoku[8][6], sudoku[8][7], sudoku[8][8]]
    else:
        print("Error, out of range")

    # Checks if the number is in the 3x3 square or not
    k = 0  # Increment for for loop set to zero
    num_in_square = 0  # Increment that will be added to if the inputted number is already in the 3x3 square
    for k in range(0, len(square_num_list)):
        print(square_num_list[k], input_num)
        if str(input_num) == square_num_list[k]:
            num_in_square += 1
        else:
            continue
    if num_in_square > 0:
        print("The number is already in the square")

        # The print board function is called again to print the updated sudoku board
        print_board(sudoku)
        num_here += 1
    else:
        print("Number is not in square")
        update_board(blanks)
    
    #If the inputted number cannot be used then the user loses a life
    if num_here > 0:
        helper_variables.lives_left -= 1 #When the user inputs a number that doesn't work, they lose a life

#Function updates the board when the human input is valid
def update_board(blanks):
    # The number inputted replaces the blank in the location
    sudoku[input_row][input_col] = str(input_num)
    print(sudoku[input_row][input_col])
    blanks -= 1  # The blank increment subtracted by one

    # Tells the user how many blanks they have got to fill.
    print("There are", blanks, "left")

#Returns the game state showing if the user is successful or not
def game_state(result):
    #Prints out game won if the sudoku has been solved
    if result == "success":
        return "Game Won"

    #Returns game lost if the sudoku hasn't been solved
    elif result == "failure":
        return "Game Lost"
    
    #Validation 
    else:
        return "Error"

# The user input and game function
def human_play(sudoku,blanks): 
    helper_variables.lives_left = 5  #Sets the lives back to 5 whenever the game starts
    while blanks > 0:
        global input_col, input_num, input_row
        
        print("\033c", end="") #Clears the terminal
        print_board(sudoku) #Calls the print board function to display the sudoku board
        print("There are",blank_checker(sudoku),"blanks left in the sudoku") #Outputs how many blanks are left
        print("Lives left:",helper_variables.lives_left) #Outputs how many lives the user has left

        #The game will end if the user has zero lives and False is returned
        if helper_variables.lives_left <= 0:
            print("You have ran out of lives")
            return False
        
        
        #Try and except used to prevent the program from halting when anything but an integer is inputted
        try:
            # Allows the user to input the exact row of where they want to place a number
            input_row = int(input("Enter which row with the blank you want to select"))
        except:
            print("Invalid input")
            continue
        input_row = input_row - 1  # Matches up with where the user inputted on the grid

        #Try and except used to prevent the program from halting when anything but an integer is inputted
        try:
            # Allows the user to input the exact column of where they want to place a number
            input_col = int(input("Enter which column with the blank you want to select"))
        except:
            print("Invalid input")
            continue
        input_col = input_col - 1  # Matches up with where the user inputted on the grid

        # Sets the value of the location to a variable
        select_space = sudoku[input_row][input_col] #Combines to inputted row and column into one location on the sudoku to be used
        print(select_space)
        
        # Calls function that checks if there is a blank in the location inputted
        is_blank(select_space)

        # User inputs the number they want to fill the gap with and is validated
        input_num = int(input("Enter a number between 1-9  to put in the space"))

        #Increments the attempts function when a number to attempt to fill a blank has been inputted
        helper_variables.attempts += 1 #Adds one attempt to the variable
        print("You have taken",helper_variables.attempts,"moves") #Current attempts would be printed
        
        #Calls the is_valid function
        is_valid(input_num, input_col, input_row)         

        # The print board function is called again to print the updated sudoku board
        print_board(sudoku)
    
    #If all of the blanks have been successfully filled in without running out of lives, return True
    return True

#Function to find the next blank in the sudoku
def comp_blank_finder(sudoku,comp_input_row_col):
    for row in range(9):
        for col in range(9):
            if(sudoku[row][col] == ' '): #If there is a blank;
                #Row and col are set to the coordinates in compinputrowcol
                comp_input_row_col[0] = row
                comp_input_row_col[1] = col
                print(comp_input_row_col[0],comp_input_row_col[1])
                return True
    return False

#Function clears the board, removing previous input so the user can start from scratch again              
def reset_board(sudoku,initial_sudoku):

    #Looks for spaces that have been occupied and removes them
    t = 0    
    for r in range(0,len(sudoku)):
        for s in range(0,len(sudoku[r])):
            #If the value of the sudoku does not equal the original value in the location, it is reset to a blank to match the original sudoku
            if sudoku[r][s] != initial_sudoku[t]: 
                sudoku[r][s] = ' '
            else:
                t += 1
    return sudoku #The sudoku that has been reverted to its original state is returned                                        
            
#Function checks if any numbers in the row matches the input from the computer
def row_check(sudoku,row,comp_input_num):
    # For loop for checking if any numbers in the row matches the inputted number
    for x in range(9):            
        # Checks if the inputted number is the same as one in the row
        if sudoku[row][x] == comp_input_num:
            # If they are the same, return True
            return True

    #If there are none the same, return False
    return False

def col_check(sudoku,col,comp_input_num):
    # New list is created to host the numbers in the column
    tablecol = []  # The elements of the column will be added to a list
    for rows in sudoku:
        # Adds each item in column to list
        tablecol.append(rows[col])

    # For loop for checking if any numbers in the column matches the randominp
    for y in range(9):
        # Checks if the randominp number is the same as one in the column
        if tablecol[y] == comp_input_num:
            # If they are the same, return True
            return True
                                  
    #If they are not the same, return False                              
    return False

def table_check(sudoku,row,col,comp_input_num):

    # Check which 3x3 square the inputted location (inputrow,inputcol) is in
    square_num_list = []  # List where the numbers from 3x3 square will go into
    if (row >= 0) and (row < 3):
        if (col >= 0) and (col < 3):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[0][0], sudoku[0][1], sudoku[0][2], sudoku[1][0]\
                , sudoku[1][1], sudoku[1][2], sudoku[2][0], sudoku[2][1], sudoku[2][2]]
            
        elif (col >= 3) and (col < 6):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[0][3], sudoku[0][4], sudoku[0][5], sudoku[1][3]\
                , sudoku[1][4], sudoku[1][5], sudoku[2][3], sudoku[2][4], sudoku[2][5]]
            
        elif (col >= 6) and (col < 9):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[0][6], sudoku[0][7], sudoku[0][8], sudoku[1][6]\
                , sudoku[1][7], sudoku[1][8], sudoku[2][6], sudoku[2][7], sudoku[2][8]]
            
    elif (row >= 3) and (row < 6):
        if (col >= 0) and (col < 3):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[3][0], sudoku[3][1], sudoku[3][2], sudoku[4][0]\
                , sudoku[4][1], sudoku[4][2], sudoku[5][0], sudoku[5][1], sudoku[5][2]]
            
        elif (col >= 3) and (col < 6):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[3][3], sudoku[3][4], sudoku[3][5], sudoku[4][3]\
                , sudoku[4][4], sudoku[4][5], sudoku[5][3], sudoku[5][4], sudoku[5][5]]
            
        elif (col >= 6) and (col < 9):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[3][6], sudoku[3][7], sudoku[3][8], sudoku[4][6]\
                , sudoku[4][7], sudoku[4][8], sudoku[5][6], sudoku[5][7], sudoku[5][8]]
            
    elif (row >= 6) and (row < 9):
        if (col >= 0) and (col < 3):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[6][0], sudoku[6][1], sudoku[6][2], sudoku[7][0]\
                , sudoku[7][1], sudoku[7][2], sudoku[8][0], sudoku[8][1], sudoku[8][2]]
            
        elif (col >= 3) and (col < 6):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[6][3], sudoku[6][4], sudoku[6][5], sudoku[7][3]\
                , sudoku[7][4], sudoku[7][5], sudoku[8][3], sudoku[8][4], sudoku[8][5]]
            
        elif (col >= 6) and (col < 9):
            # Adds the elements of the square where the number location is to the list
            square_num_list = square_num_list + [sudoku[6][6], sudoku[6][7], sudoku[6][8], sudoku[7][6]\
                , sudoku[7][7], sudoku[7][8], sudoku[8][6], sudoku[8][7], sudoku[8][8]]
    else:
        pass

    # Checks if the number is in the 3x3 square or not
    for y in range(9):
        # If the number is already in the 3x3 square, it is removed from the list
        if square_num_list[y] == comp_input_num:
            #If the inputted number is in the square, return True
            return True
    
    #If they are not the same, return False 
    return False

# The machine input and function
def computer_play(sudoku, blanks):
    print("\033c", end="") #Clears the terminal after every recursion
    print_board(sudoku) 
    #print("There are",blankchecker(sudoku),"left in the sudoku")
    comp_input_row_col = [0,0] #Record of inputcol and inputrow when finding the next blank

    #If the value returned from the function is not False the program will continue
    if comp_blank_finder(sudoku,comp_input_row_col) == False:
        return True

    # Setting row and col to the coordinates where a blank is from the for loop
    row = comp_input_row_col[0]
    col = comp_input_row_col[1]     

    #Checking numbers 1-9 to see what will be best to input in the blank
    comp_input_num = ['1','2','3','4','5','6','7','8','9']
    for num in range(len(comp_input_num)):
        helper_variables.attempts += 1 #Adds one attempt to the variable
        print(helper_variables.attempts) #Current attempts would be printed

        #If number isn't in row, column and table after calling functions to check if they are in those
        if (not row_check(sudoku,row,comp_input_num = comp_input_num[num]) and not col_check(sudoku,col,comp_input_num = comp_input_num[num]) \
            and not table_check(sudoku,row,col,comp_input_num = comp_input_num[num])):
            
            sudoku[row][col] = comp_input_num[num] #Sets the current blank to the input num 

            #If the sudoku has been successfully completed, return True
            if(computer_play(sudoku,blanks)):
                return True
            
            #If it fails, the coordinate is reset to blank and will be attempted again
            sudoku[row][col] = ' '
    
    #Backtracking is triggered here
    return False
        

# Main Program
if __name__ == '__main__':

    # Don't change the layout of the following sudoku examples
    sudoku1 = [
        [' ', '1', '5', '4', '7', ' ', '2', '6', '9'],
        [' ', '4', '2', '3', '5', '6', '7', ' ', '8'],
        [' ', '8', '6', ' ', ' ', ' ', ' ', '3', ' '],
        ['2', ' ', '3', '7', '8', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', ' ', ' ', ' ', '9', ' '],
        ['4', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'],
        ['6', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', ' ', '1', ' ', '7'],
        [' ', ' ', ' ', ' ', '3', '7', '9', '4', ' '],
    ]
    sudoku2 = [
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' '],
        ['7', '3', '4', ' ', '8', ' ', '1', '6', '2'],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', '3', '8'],
        ['5', '6', '8', ' ', ' ', '4', ' ', '1', ' '],
        [' ', ' ', '2', '1', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', '8', ' ', ' ', '2', '5', '4'],
        [' ', '7', ' ', ' ', ' ', '2', '8', '9', ' '],
        [' ', '5', '1', '4', ' ', ' ', '7', '2', '6'],
        ['9', ' ', '6', ' ', ' ', ' ', ' ', '4', '5'],
    ]
    sudoku3 = [
        ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '3', '6', ' ', ' ', ' ', ' ', ' '],
        [' ', '7', ' ', ' ', '9', ' ', '2', ' ', ' '],
        [' ', '5', ' ', ' ', ' ', '7', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '4', '5', '7', ' ', ' '],
        [' ', ' ', ' ', '1', ' ', ' ', ' ', '3', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', ' ', '6', '8'],
        [' ', ' ', '8', '5', ' ', ' ', ' ', '1', ' '],
        [' ', '9', ' ', ' ', ' ', ' ', '4', ' ', ' '],
    ]
    sudoku4 = [
        [' ', '4', '1', ' ', ' ', '8', ' ', ' ', ' '],
        ['3', ' ', '6', '2', '4', '9', ' ', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' '],
        [' ', ' ', ' ', '4', '7', ' ', '2', '1', ' '],
        ['7', ' ', ' ', '3', ' ', ' ', '4', ' ', '6'],
        [' ', '2', ' ', ' ', ' ', ' ', ' ', '5', '3'],
        [' ', ' ', '7', ' ', '9', ' ', '5', ' ', ' '],
        [' ', ' ', '3', ' ', '2', ' ', ' ', ' ', ' '],
        [' ', '5', '4', ' ', '6', '3', ' ', ' ', ' '],
    ]

    # make sure 'option=2' is used in your submission
    option = 2    

    if option == 1:
        sudoku = sudoku1
    elif option == 2:
        sudoku = sudoku2
    elif option == 3:
        sudoku = sudoku3
    elif option == 4:
        sudoku = sudoku4
    else:
        raise ValueError('Invalid choice!')
    
    
    #Saves the original numbers in the sudoku to a list to allow the board to be reset
    initial_sudoku = [] #List will hold the values of the original sudoku before it goes into the humanplay or computerplay functions 
    t= 0    
    for row in sudoku:
        for t in range(0,len(row)):
            if row[t] != " ":
                initial_sudoku.append(row[t])
            else:
                pass

    # add code here to solve the sudoku
    still_play = 0
    attempts = 0
    
    while still_play == 0:
        #Game will ask which version of the game do you want to play
        print("Do you want to play sudoku or let the Computer play it?")
        input_type = input("Select Human or Computer:")
        
        #Human input
        if input_type == "Human" or input_type == "human": 
            print_board(sudoku)
            blank_checker(sudoku)
            time_start = time.time() #Gets the start time for the execution of the sudoku        
            helper_variables.attempts = 0 #Sets attempts to 0
         
            #Will print out the sudoku board after the human input has finished, if the solver is successful
            if(human_play(sudoku,blanks)):
                print("\033c", end="") #Clears the terminal
                print_board(sudoku)
                print("The puzzle has been solved")
                time_end = time.time() #Gets the end time after the sudoku has been completed  
                print("Time taken on the sudoku puzzle:",(time_end-time_start),"seconds") #Prints out the time taken on the sudoku puzzle 
                print(game_state(result = "success")) #Calls the game_state function with the attribute telling it, that the sudoku was solved          
            
            else:
                print("You have ran out of lives, Game Over")
                time_end = time.time() #Gets the end time after the sudoku has been failed 
                print("Time taken on the sudoku puzzle:",(time_end-time_start),"seconds") #Prints out the time taken on the sudoku puzzle
                print(game_state(result = "failure")) #Calls the game_state function with the attribute telling it, that the sudoku was not solved 
                
                time_end = time.time() #Gets the end time after the sudoku has been completed or has been failed 
                print("Time taken on the sudoku puzzle:",(time_end-time_start),"seconds") #Prints out the time taken on the sudoku puzzle 
                
                #The user will be given the option to see the answers using the computer_play function
                try:
                    see_answers = str(input("Do you want to see the answers? Yes or No:"))
                    if see_answers == "Yes" or see_answers == "yes":
                        print("\033c", end="") #Clears the terminal
                        reset_board(sudoku,initial_sudoku) #Resets the sudoku board
                        computer_play(sudoku,blanks) #Calls the computer_play function
                        print("This is the answer to the sudoku")
                    elif see_answers == "No" or see_answers == "no":
                        pass
                    else:
                        print("Invalid input")
                        see_answers = str(input("Do you want to see the answers? Yes or No:"))
                except:
                    print("Invalid Input")
                    see_answers = str(input("Do you want to see the answers? Yes or No:"))
            
            print("You used",helper_variables.attempts,"moves in the sudoku") #Prints out the amount of attempts the user had taken to either complete or fail the puzzle

        #Computer input    
        elif input_type == "Computer" or input_type == "computer":
            print_board(sudoku)
            blank_checker(sudoku)
            helper_variables.attempts = 0 #Sets attempts to 0
            time_start = time.time() #Gets the start time for the execution of the sudoku 
 
            #Will print out the sudoku board after the computer input has finished, if the solver is successful
            if(computer_play(sudoku,blanks)):
                print("\033c", end="") #Clears the terminal
                print_board(sudoku)
                print("The puzzle has been solved") 
                print(game_state(result = "success")) #Calls the game_state function with the attribute telling it, that the sudoku was solved          
            else:
                print("No solution exists")
                print(game_state(result = "failure")) #Calls the game_state function with the attribute telling it, that the sudoku was not solved 
            
            print("There were",helper_variables.attempts,"moves in the sudoku") #Outputs the amount of attempts the computer had taken to either complete or fail the puzzle
            time_end = time.time() #Gets the end time after the sudoku has been completed or has been failed 
            print("Time taken on the sudoku puzzle:",(time_end-time_start),"seconds") #Prints out the time taken on the sudoku puzzle 
        
        #Validation for invalid inputs
        elif input_type == " ":
            print("Incorrect input")
        else:
            print("Incorrect input")    
            
        #Game will ask if you still want to play again
        print("Do you still want to play?")
        resume = input("Yes or No:")

        #If yes, it will return to the start and ask the user what game they want to play
        if resume == "Yes" or resume == "yes":
            reset_board(sudoku,initial_sudoku)
            print_board(sudoku)
            continue

        #If no, the game will stop
        elif resume == "No" or resume == "no":
            still_play = 1
        else:
            print("Invalid input")
    game_kill() #Calls the function to stop the program 
    
