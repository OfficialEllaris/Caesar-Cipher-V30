alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(direction, text, shift):
  cipher_text = ""

  if direction == "encode":
    for letter in text:
      cipher_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
    print(f"The encoded text is {cipher_text}")
  elif direction == "decode":
    for letter in text:
      cipher_text += alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
    print(f"The encoded text is {cipher_text}")
  else:
    print("Invalid direction! Please type 'encode' or 'decode'.")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction, text, shift)