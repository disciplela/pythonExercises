from caesar_cipher_title import title
print(title)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, cipher_direction, shift_amount):
    end_text = ''
    if cipher_direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            find_position = alphabet.index(char)
            end_text += alphabet[find_position + shift_amount]
        else:
            end_text += char        
        
    print(f'The {cipher_direction}d text is {end_text}')

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))  
    shift = shift % 26
    print('\n')


    caesar(text, direction, shift)

    restart_function = input(f'Would you like to continue? "y" for yes, "n" for no:\n').lower()

    if restart_function == 'y':
        restart = True
    else:
        restart = False
        print('Thanks for playing')
 
 
    
    
    
    
#     def encrypt(plaintext, shift_amount):
#     cipher_text = ''
#     for letter in plaintext:
#         find_position = alphabet.index(letter)
#         test_for_zed = find_position + shift_amount
#         if test_for_zed >= len(alphabet):
#             past_zed_calc = test_for_zed - len(alphabet)
#             cipher_text += alphabet[past_zed_calc]
#         else:
#             cipher_text += alphabet[find_position + shift_amount]
 

#     print(f'Your encrypted message is: {cipher_text}')

# def decrypt(encrypted_text, shift_amount):
    
#     deciphered_message = ''
#     for letter in encrypted_text:
#         position = alphabet.index(letter)
#         test_for_zed = position - shift_amount
#         if test_for_zed < 0:
#             past_zed_calc = 26 + test_for_zed
#             deciphered_message += alphabet[past_zed_calc]
#         else:
#             deciphered_message += alphabet[position - shift_amount]
#     print(f'Your decoded message is: {deciphered_message}')

# if direction == 'encode':    
#     encrypt(plaintext = text, shift_amount = shift)
# elif direction == 'decode':
#     decrypt(encrypted_text = text, shift_amount = shift)
# else:
#     print('You entered an invalid option.')
    
    
    #Alternative method_
        # if test_for_zed > len(alphabet):
        #     cipher_text += test_for_zed - len(alphabet)
        # else:
        #     cipher_text += alphabet[find_position + shift_amount]
        # if test_for_zed > len(alphabet):
    # cipher_text = ''
    # for letter in range(0, len(plaintext)):
    #     find_index = alphabet.index(plaintext[letter])
    #     index_count = find_index + shift     
    #     shifted_letter = (alphabet[find_index + shift_amount])
    #     cipher_text += shifted_letter
    # print(cipher_text)


