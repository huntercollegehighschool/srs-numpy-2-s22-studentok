"""
# Column Cypher
# =============
# 
A column cipher works by writing the message in rows of a fixed length, and then extracting the columns and concatenating them.  So the message
"THISISACOLUMNCYPHER" with rows of length 5, would be written::
 
#     THISI
#     SACOL
#     UMNCY
#     PHERX

and then be sent as "TSUPHAMHICNESOCRILYX".  Note that you want to pad the message with extra characters to make it a multiple of the number of columns.
# 
In this exercise we will use numpy multidimensional arrays to encode a message as a column cypher.
"""

"""
1. Import numpy (as np) so that you have access to all numpy methods. Code: import numpy as np
"""


"""
2. A message is defined below. Use np.array(<list>) to convert message into an array of characters, then print the array (note: you will have to convert message to a LIST of characters first.)

"""
message = "THISMESSAGEISVERYSECRETX"



"""
3. Use <array>.shape = (<number of rows>, <number of columns>) to create a column cypher with 3 columns. Print the result
Note: You can calculate how many rows you will need, or the shape function can do that automatically if you make the number of rows -1.
"""


"""
4. Use <var> = np.transpose(<array>) to switch the rows and the columns. Print the new array.
"""

"""
5. When you index the transposed array, you should get a row of the array. For example, <array>[0] should be the first row of characters.

Declare a new variable that will store the encoded message, and set it to an empty string. Loop through the rows of the array. Use ''.join(<array>) to convert the array of characters to a string. Then add that string to the encoded message. Print the final result.
"""
