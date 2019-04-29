#!/usr/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               00598949                                                    #
#                               mkhan8@unh.newhaven.edu                                     #
#############################################################################################

# Function Definitions

# Function to generate an 8 bit sequence for a character using ASCII value of the character


def binary_generator(pchar, psequence):

    print("Processing: ", pchar)
    # Gets the ASCII value of character using ord()
    data = ord(pchar)
    print("ASCII Value: ", data)

    # Converting the ASCII value to binary sequence
    while data != 0:
        if data % 2 == 0:
            psequence.append(0)
        else:
            psequence.append(1)
        data //= 2

    print("Length of sequence: ", len(psequence))

    # Checks the length of the generated sequence; adds padding bit '0' if less than 8
    if len(psequence) < 8:
        print("Length is less than 8 bit. Correcting...")

        length = 8 - len(psequence)
        padding = [0]

        psequence = psequence + padding*length

    # Reverses the sequence
    psequence.reverse()
    print("Length of corrected sequence: ", len(psequence))
    print("Sequence", psequence)

    # Return the Sequence
    return psequence

#############################################################################################


# Function to do a parity check and return the parity bit to be inserted into the sequence


def parity_check(psequence, bit, pset):
    # Counter to determine the parity
    count = 0

    # Counter using the sequence
    for seq in pset :
        count += psequence[seq]

#    print("Count for the sequence is: ", count)

    # If count is even
    if (count % 2) == 0:
#        print("Set count is even")
        bit = [0]

    # If count is odd
    else:
#        print("Set count is odd")
        bit = [1]

    # Return the parity bit
    return bit

#############################################################################################

# Function to insert 4 correction bits into the generated 8 bit sequence


def check_bit(psequence) :

    # Parity bit list
    parity = []
    print("Processing sequence: ", psequence)

    # List of a set of bits to be calculated
    set1 = [0,1,3,4,6]
    set2 = [0,2,3,5,6]
    set3 = [1,2,3,7]
    set4 = [4,5,6,7]

    # Function call to check parity
    parity = parity_check(psequence, parity, set1)
#    print("psequence ", psequence, "parity ", parity, "set1 ", set1)
    # Inserting the returned parity into the first bit in the sequence
    psequence.insert(0, parity[0])

    # Function call to check parity
    parity = parity_check(psequence, parity, set2)
#    print("psequence ", psequence, "parity ", parity, "set2 ", set2)
    # Inserting the returned parity into the second bit in the sequence
    psequence.insert(1, parity[0])

    # Function call to check parity
    parity = parity_check(psequence, parity, set3)
#    print("psequence ", psequence, "parity ", parity, "set3 ", set3)
    # Inserting the returned parity into the fourth bit in the sequence
    psequence.insert(3, parity[0])

    # Function call to check parity
    parity = parity_check(psequence, parity, set4)
#    print("psequence ", psequence, "parity ", parity, "set4 ", set4)
    # Inserting the returned parity into the fifth bit in the sequence
    psequence.insert(7, parity[0])

    print("12 bit sequence: ", psequence)

    # Return the parity corrected bit
    return psequence

#############################################################################################

# Function to format the 12 bit output sequence


def merge(psequence) :

    string = ''

    # Convert to string
    for bit in range(0, len(psequence)):
        string += str(psequence[bit])

#    print("psequence ", psequence, "string ", string)

    # Insert string back into list
    psequence = string

    # Return List
    return psequence

#############################################################################################

# Main Program

# Initial response parameter for the while loop asking user if they want to check another sequence
res = 'Yes'

# While loop to ask user to input sequence to process
while res != 'No' or res != 'no' or res != 'n' or res != 'N':

    # Takes a string input and stores it into message
    message = input("Please enter your message (Char only): ")
    print("You entered '", message, "'. Processing the message...")

    # List to store the 12 bit sequence generated for each character
    tsequence = []

    # Loop to process each character in the input message
    for char in message:
        # List to store the sequence generated for each character
        sequence = []
        sequence = binary_generator(char, sequence)
#        print("Sequence after binary generator", sequence)
        sequence = check_bit(sequence)
        sequence = merge(sequence)

        # Appends the 12 bit sequence generated for the character
        tsequence.append(sequence)

    # Prints out the total sequence generated
    print("Final message: ", tsequence)

#############################################################################################

    # Check to process another sequence
    print("Do you want to generate another sequence? [Y/N]")
    res = input("")
    if res == 'No' or res == 'no' or res == 'n' or res == 'N':
        print("You chose NOT to continue... Exiting program!...")
        break
    else:
        print("You chose to continue")
        continue

else:
    # If loop exits unexpectedly display error
    print("Oops! something is wrong!")

#############################################################################################
#                                       End of Program                                      #
#############################################################################################
