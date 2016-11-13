#######################################################################
#                                                                     #
# David Fuller                                                        #
#                                                                     #
# Project Euler: Problem 4.                                           #
#                                                                     #
# 11/11/2016                                                          #
#                                                                     #
#######################################################################

#######################################################################
#                                                                     #
#                          IMPORT STATEMENTS                          #
#                                                                     #
#######################################################################

from tkinter import *   # For GUI
import time             # For keeping track of elapsed time

#######################################################################
#                                                                     #
#                              CONSTANTS                              #
#                                                                     #
#######################################################################

TITLE               = "Project Euler: Problem 2"   # GUI Title.
GEOMETRY            = "300x163"                    # GUI screen size.
HIGHEST_THREE_DIGIT = 999                          # Highest 3 digit
                                                   #     number.

#######################################################################
#                                                                     #
#                             EULER CLASS                             #
#                                                                     #
#######################################################################

class Euler:
    # Function decides whether palindrome or not
    # PRE: input must be a string
    def isPal(self, input):
        length = len(input)
        for i in range(int(length / 2)):
            if (input[i] != input[length - i - 1]):
                return False
        return True

    # Method finds solution to Project Euler: Problem 4
    def findSolution(self):
        # Store x and y as highest possible 3-digit numbers
        x = HIGHEST_THREE_DIGIT
        y = HIGHEST_THREE_DIGIT

        # Store num as x * y
        palindrome = x * y

        # While num is not palindromic and x is greater
        # than 900, decrement y and x appropriately
        while (not self.isPal(str(palindrome))):
            y -= 1

            palindrome = x * y

            # if y drops to 900, put y back to 999 and
            # decrement x
            if (y <= 900):
                y = 999
                x -= 1

        # Return highest palindrome
        return palindrome

#######################################################################
#                                                                     #
#                              GUI CLASS                              #
#                                                                     #
#######################################################################

class EulerForm:
    def __init__(self, parent, msg):
        # Set up GUI
        self.parent = parent
        self.parent.title(TITLE)
        self.parent.geometry(GEOMETRY)

        # Create solution StringVar
        self.solution = StringVar()
        self.solution.set("")

        # Create GUI Widgets
        self.descriptionMessage = Message(parent, \
                                          text = msg, \
                                          width = 280)
        self.solutionButton = Button(parent, \
                                     text = "Find Solution", \
                                     command = self.findSolution)
        self.solutionLabel = Label(parent, \
                                   textvariable = self.solution)

        # Place GUI Widgets
        self.descriptionMessage.pack()
        self.solutionButton.pack()
        self.solutionLabel.pack()

    # Method finds and displays solution and elapsed time
    def findSolution(self):
        # Store start time
        start = time.time()

        # Project Euler object
        euler = Euler()
        solution = euler.findSolution()

        # Calculate elapsed time, rounded to 2 decimals
        elapsed = ("%.2f" % (time.time() - start))

        # Display the sum, as well as elapsed time
        solution = str(solution) + \
                   " found in " + \
                   str(elapsed) + \
                   " seconds."
        self.solution.set(solution)

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

# Method sets up Problem description
def createDescription():
    description = "A palindromic number reads the same both ways. " + \
                  "The largest palindrome made from the product of" + \
                  " two 2-digit numbers is 9009 = 91 × 99.\n\n" + \
                  "Find the largest palindrome made from the " + \
                  "product of two 3-digit numbers."
    return description

# Define main - app driver
def main():
    # Initialize GUI
    root = Tk()

    # Call function to set up Problem description
    description = createDescription()

    # Set up EulerForm
    euler = EulerForm(root, description)

    # Keep app running
    root.mainloop()

# Begin app
main()
