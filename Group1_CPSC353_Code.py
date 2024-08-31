""" 
This is the One Time Pad Encryption Function. 
One Time Pad uses a key that is the same exact length as the message.

Input: the message and key containing only letters and spaces (will fail gracefully is given anything else)
Output: the encrypted message and the key (with some words labeling each)

"""
def oneTimePadEncr(message_input, key_input):
    
    # Frist we make sure that the lengths of the message and key match
    length = len(message_input)     # We will use this later so it gets its own variable
    if length != len(key_input):
        return "There was an issue. The length of the key is not the same as the length of the encrypted message. Please try again."

    
    # We want to make sure the message and key are in capital letters and do not contain special characters
    message = []            # This is the version of the message in capital letters
    key = []                # This is the version of the key in capital letters
    for k in range(length):
        # This section checks the message and fills the message list with the proper letters in upper case
        if message_input[k] == " ":                                             # If the message is a space
            message.append(" ")
        elif ord(message_input[k]) > 96 and ord(message_input[k]) < 123:         # If the message is lower case 
            message.append(message_input[k].upper())
        elif ord(message_input[k]) > 64 and ord(message_input[k]) < 91:         # If the message is in upper case
            message.append(message_input[k])
        else:
            print("An unacceptable character was included in the message")      
            return "Please try again only using letters and spaces"
        
        # This section checks the key and fills the key list with the proper letters in upper case
        if key_input[k] == " ":                                         # If the key is a space
            key.append(" ")
        elif ord(key_input[k]) > 96 and ord(key_input[k]) < 123:         # If the key is lower case
            key.append(key_input[k].upper())
        elif ord(key_input[k]) > 64 and ord(key_input[k]) < 91:         # If the key is in upper case
            key.append(key_input[k])
        else:
            print("An unacceptable character was included in the key")      
            return "Please try again only using letters and spaces"


    encr = []                               # This is the encrypted message that we will output

    # This for loop adds the key letter to the associated letter in the message to encrypt it, and then appends the encrypted letter to the encrypted message 
    for i in range(length):                 
        
        # If the "letter" of the message is a space
        if message[i] == " ":
            letterEncr = (26 + ord(key[i]) - 65) % 27 + 65      # 26 is our decided value for a space, ord() changes the value to be the ASCII number value, we subtract 65 to get the key down to our 0-26 range, we mod by 27 to make sure that the total remains below 27, we add 65 to get it back to the correct ASCII value
            if letterEncr == 91:         # If the letter is supposed to be a space it will be 91 right now, we must correct that
                encr.append(chr(32))    # the character chr() for 32 is a space
            else:                       
                encr.append(chr(letterEncr))    # letterEncr is technically a number that represents a letter, it is not a character until you use chr()
        
        # If the "letter" of the message is actually a letter
        else:
            letterEncr = (( ord(message[i]) - 65 + ord(key[i]) - 65) ) % 27 + 65      # This will subtract the base value A from each letter, add the value of the key in its 0-16 form, and mod 27 to make sure values are between 0 and 26, add 65 to get it back to the ASCII table leter
            if letterEncr == 91:             # If the letter is supposed to be a space it will be 91 right now, we must correct that
                encr.append(chr(32))
            else:
                encr.append(chr(letterEncr))

    # This prettifies the lists back into a string so it is easy to read and can be copied and pasted for decryption
    final_encrypt = "".join(encr)
    final_key = "".join(key)

    return  "Encrypted Message is: "+ final_encrypt + "     and     Key is: " + final_key

# ^^^ Above it returns a whole statement with labels for the encryption message and key. If the testing makes more sense for it to say something else feel free to change. 

""" 
This is the One Time Pad Decryption Function. 
One Time Pad uses a key that is the same exact length as the message.

Input: the encrypted message and key containing only letters and spaces (will fail gracefully is given anything else)
Output: the decrypted message

"""
def oneTimePadDecr(encr_mess, key):
    # Change the input encryption message into a list of characters
    encr = []
    encr[:0] = encr_mess
    
    # initialize our descryption list
    decr = []
    
    # make sure that the length of the message and the key match
    length = len(encr_mess)
    if length != len(key):
        return "There was an issue. The length of the key is not the same as the length of the encrypted message. Please try again."

    # This for loop 
    for i in range(length):                 
        # make sure the key is right
        if key[i] == " " or ( ord(key[i]) > 64 and ord(key[i]) < 91):
            pass
        else:
            return "There was an issue. Your key contains an unacceptable character. It should only be comprised of spaces and capital letters"

        # If the "letter" of the encrypted message is a space
        if encr[i] == " ":
            letterDecr = (26 - ord(key[i]) + 65) % 27 + 65      # The space value starts at 26, we subtract the value of the key which is the ord()-65 (double negative makes a positive so we add 65), mod 27 to bring it back to our range of 0-26, then add 65 to bring it back to ASCII
            if letterDecr == 91:         # If the letter is supposed to be a space it will be 91 right now, we must correct that
                decr.append(chr(32))
            else:
                decr.append(chr(letterDecr))        # note: letterDecr is actually the number value of the letter
        
        # If the "letter" of the encrypted message is actually a letter
        elif ord(encr[i]) > 64 and ord(encr[i]) < 91:
            letterDecr = (( ord(encr[i]) - 65 - ord(key[i]) + 65) ) % 27 + 65      # This will subtract the base value A from each letter, subtract the value of the simplified letters together, and mod 27 to get values between 0 and 26, add 65 to get it back to the ASCII table leter
            if letterDecr == 91:             # If the letter is supposed to be a space it will be 91 right now, we must correct that
                decr.append(chr(32))
            else:
                decr.append(chr(letterDecr))
        
        # If the "letter" doesn't fit the specifications
        else:
            return "There was an issue. Your encrypted message contains an unacceptable character. It should only be comprised of spaces and capital letters."

    return "".join(decr)        # This is the pretty string version of the decr list





# My personal testing. Feel free to delete or change. 
message = input("Write message: ")
key = input("Write key of the same length as the message: ")
print(oneTimePadEncr(message, key))

decryption = input("Encrypted Message: ")
key = input("Key: ")
print("The message is: " + oneTimePadDecr(decryption, key))