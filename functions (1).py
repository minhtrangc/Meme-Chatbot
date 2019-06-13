"""A collection of functions for doing my project."""

def is_question(input_string):
    """See if the user input is a question. From Assignment 3.
    
    Parameters
    ----------
    input_string : string
        String of user's input
    
    Returns
    -------
    output : boolean
        Boolean of True or False whether the user input is a question
    """
    
    # A conditional to determine whether the input string is a question based on the inclusion of a question mark
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output


def is_exclamation(input_string):
    """See if the user input is an exclamation. Modified from Assignment 3.
    
    Parameters
    ----------
    input_string : string
        String of user's input
        
    Returns
    -------
    output : boolean
        Boolean of True or False whether the user input is an exclamation
    """
    
    # A conditional to determine whether the input string is an exclamation based on the inclusion of an exclamation mark
    if '!' in input_string:
        output = True
    else: 
        output = False
        
    return output


def spongebob_meme(input_string):
    """Alternate the capitalization of each letter between capital and lowercase to mimick the Spongebob meme.
    
    Parameters
    ----------
    input_string : string
        Original string that will have its letters alternating between lowercase to uppercase
        
    Returns
    -------
    alternating_string : string
        New string with the original input's letters alternating between lowercase and uppercase
    """
    
    # Temporarily changing the input string into a list in order to alternate between the items in terms of range
    alternating_string = ''
    string_to_list = list(input_string)
    
    for letter in range(len(string_to_list)):
        if letter % 2 == 0:
            alternating_string += string_to_list[letter].lower()
        else:
            alternating_string += string_to_list[letter].upper()
            
    return alternating_string


def phrase_in_laughter(input_string):
    """Insert the input string in the middle of a line of laughter without spaces.
    
    Parameters
    ----------
    input_string : string
        String to be inserted in the middle of the line of laughter
         
    Returns
    -------
    laughing_string : string
        String of laughter that has the input string inserted in between
    """
    
    # Concatenating the input string in between laughter to mimick the sublte phrase insertion bewteen laughter meme.
    laughing_string = 'HAHAHA' + ' ' + input_string + ' ' + 'HAHAAAA'

    return laughing_string


def end_chat(input_list):
    """End the chatbot replies. From Assignment 3.
    
    Parameters
    ----------
    input_list : list
        List of user's input
        
    Returns
    -------
    True : boolean
        True boolean if 'quit' is within the input to end Mimi's replies later on
    False : boolean
        False boolean if 'quit' is not within the input and does not end Mimi's replies later on
    """
    
    # Check if 'quit' is in the input list because it indicates the user is done with the chatbot
    if 'quit' in input_list:
        return True
    else:
        return False
