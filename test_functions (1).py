"""Test for my functions."""

from functions import is_question, is_exclamation, spongebob_meme, phrase_in_laughter, end_chat

def test_is_question():
    
    # Test that is_question can take inputs and return outputs
    assert callable(is_question)
    
    # Test that is_question returns a boolean
    assert isinstance(is_question('hi'), bool)
    
    # Test that an input string returns the expected result
    assert is_question('hello?') == True
    
def test_is_exclamation():
    
    # Test that is_exclamation can take inputs and return outputs
    assert callable(is_exclamation)
    
    # Test that is_exclamation returns a boolean
    assert isinstance(is_exclamation('hi'), bool)
    
    # Test that an input string returns the expected result
    assert is_exclamation('hello!') == True
    
def test_spongebob_meme():
    
    # Test that spongebob_meme can take inputs and return outputs
    assert callable(spongebob_meme)
    
    # Test that spongebob_meme returns a string
    assert isinstance(spongebob_meme('i think i will pass'), str)
    
    # Test that spongebob_meme returns the expected result
    assert spongebob_meme('i like you') == 'i lIkE YoU'
    
    assert spongebob_meme('I am bored') == 'i aM BoReD'

def test_phrase_in_laughter():
    
    # Test that insert_phrase_in_laughter takes inputs and returns outputs
    assert callable(phrase_in_laughter)
    
    # Test that phrase_in_laughter returns a string
    assert isinstance(phrase_in_laughter('I am sad'), str)
    
    # Test that phrase_in_laughter returns the expected results
    assert phrase_in_laughter('rejection is inevitable') == 'HAHAHA rejection is inevitable HAHAAAA'
    
def test_end_chat():
    
    # Test that end_chat takes inputs and returns outputs
    assert callable(end_chat)
    
    # Test that end_chat returns a boolean
    assert isinstance(end_chat(['a', 'b']), bool)
    
    # Test that phrase_in_laughter returns the expected results
    assert end_chat(['quit']) == True