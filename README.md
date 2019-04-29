# Error-Correction-Transmission
This program generates a bit sequence from a message with error correction bits.

##
In the error correction program the code would check a received sequence of twelve ones and zeros to determine whether any bits had been corrupted during a transmission. In this program I am going to generate a bit sequence based on an input message. The program has a query loop that allows the user to generate more than one bit sequence. Each time through the loop, it asks the user to input a character message which is read into a string. The string is then processed as follows:

1) Through a function that takes a single character as input and returns a list containing eight ones and zeros that represents the binary form of the character's value in the ASCII sequence. I determined a character's index in the ASCII code using the ord() function. I converted this index value into its binary equivalent using the repeated division by 2 method by generating a list of integer 1 and 0 values rather than a string.
2) And then through a function that takes a list containing eight ones and zeros and then returning a new list containing the 12 bits corresponding to the error correction code used in the previous error correction code. This time, I examine the appropriate subset of data bits, I am not looking to see if a check bit is correct. I am calculating the correct check bit value that goes with the even or odd number of ones in the data bits. Once I have generated these four check bits, I am going to create the list of 12 bit values that will be sent in a transmission for that data byte and then return this list.
3) Using these two functions, I created a single list of ones and zeros that corresponds to the data transmission I would make for my input message, having converted each character into its corresponding 12 bits and then print out this data transmission sequence.
