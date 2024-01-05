import string
alphabet = list(string.ascii_letters)

def encryption(key, message): #abcd
        cipher = " "
        for i in message:
            position = alphabet.index(i)
            new_position = position+key
            cipher += alphabet[new_position]
        print(cipher)


def decryption(key, message):
        decrypted_text= " "
        for i in message:
            position = alphabet.index(i)
            new_position = position-key
            decrypted_text += alphabet[new_position]
        print(decrypted_text)    
     
        


end  = False
while not end:
    What_You_Want = input("Type Encrypt of encryption or Type Decrypt for Decryption:\n")
    key = int(input("Enter the key:\n"))
    text = input("type your message:\n")

    if What_You_Want == "Encrypt":
        encryption(key, message=text)
    else:
        decryption(key, message=text)
    Yes_NO = input("you want to continue: (Yes/No) :-")
    if Yes_NO == "No":
        end = True
        print("Bye...!")          

