import re

#this part of the code that takes in an empty string and returns zero
def add(numbers_string) :
    match_found = re.search("^//(.*)\n", numbers_string) 
    if numbers_string == "" :
        return 0 

#this part of the code deals with other delimiters that could be found in a string   
    elif match_found :
        delimiter = match_found.groups()[0]
        numbers = numbers_string[3 + len(delimiter):]
        strings_list = numbers.split(delimiter)
        sum = 0
        for i in strings_list :
            num_int = int(i)
            sum += num_int
        return sum

# this part of the code incorporates regular expressions in order to deal with a new line or a character
    elif ("\n" in numbers_string) or ("," in numbers_string): 
        sum = 0 
        for i in re.split("[,\n]", numbers_string)  :
            num_int = int(i) 
            sum += num_int
        return sum 

#this part of the code rejects negative values 
    elif ("-" in numbers_string) :
        raise Exception("Negatives not allowed.")

#this part of the code that takes in a single number string and returns that number as an integer    
    else: 
      return int(numbers_string) 