from alphabets import alphabet
import logo

print(logo.logo+"\n\n")

def crypt(direction, text, shift):
    msg = "encoded" if direction == 'encode' else "decoded"
    coded_message = ""
    if direction == 'decode':
      shift *= -1
    for char in text:
      if char not in alphabet:
        coded_message += char
      else:
        index_of_char = (alphabet.index(char) + shift) % 26
        coded_message += alphabet[index_of_char]
    print(f"The {msg} text is {coded_message}")

flag = True
while flag:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == 'encode' or direction == 'decode': 
    crypt(direction, text, shift)
  else:
    print("Enter the correct direction: encode (or) decode.\n")

  continue_game = input("Do you wish to continue? 'Yes' (or) 'No'\n").lower()
  if continue_game == 'no':
     flag = False