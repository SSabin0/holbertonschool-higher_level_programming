#!/usr/bin/python3
def no_c(my_string):
    # 1. Start with an empty string container
    final_string = ""
    
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            # 2. Save the character into your container instead of printing it
            final_string += my_string[i]
            
    # 3. Return the actual built string, NOT an empty one!
    return final_string
