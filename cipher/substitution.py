##### CREATIVE COMMONS LICENSE BLOCK #####
# This program is licensed under a Creative Commons Attribution 4.0
# International License (CC BY 4.0). You are free to share (copy and
# redistribute the material in any medium or format) and adapt (remix,
# transform, and build upon the material) for any purpose, even
# commercially, as long as you give appropriate credit, provide a link
# to the license, and indicate if changes were made. You may do so in
# any reasonable manner, but not in any way that suggests the licensor
# endorses you or your use.

from cipher import settings

def _atbash(alphabet, char):
    return alphabet[len(alphabet)-1-alphabet.index(char)]
	
def _caesar(alphabet, char, shift):
    return alphabet[(alphabet.index(char)+shift) % len(alphabet)]
	
def atbash(text):
    output = ''
    
    for char in text:
        if char in settings.LOWERCASE:
            output += _atbash(settings.LOWERCASE, char)
        elif char in settings.UPPERCASE:
            output += _atbash(settings.UPPERCASE, char)
        else:
            output += char
    
    return output
	
def caesar(text, shift=3):
    output = ''
    
    for char in text:
        if char in settings.LOWERCASE:
            output += _caesar(settings.LOWERCASE, char, shift)
        elif char in settings.UPPERCASE:
            output += _caesar(settings.UPPERCASE, char, shift)
        else:
            output += char
        
    return output
	
def rot13(text):
    return caesar(text, 13)

# NOTE: Currently converts all plaintext to lowercase (so, no uppercase
# letters for now). Will fix in the future.
def keyword(key, text):
    # Construct new cipher alphabets
    alphabet = key.lower()
    
    i = settings.LOWERCASE.index(alphabet[len(alphabet) - 1])
    for x in range(len(settings.LOWERCASE)):
        i = (i + 1) % len(settings.LOWERCASE)
        if settings.LOWERCASE[i] not in alphabet:
            alphabet += settings.LOWERCASE[i]
        
    # Return substitution with no shift
    output = ''
    for char in text:
        if char.lower() in alphabet:
            output += alphabet[settings.LOWERCASE.index(char.lower()) % len(settings.LOWERCASE)]
        else:
            output += char
        
    return output
