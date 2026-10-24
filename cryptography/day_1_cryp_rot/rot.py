def rot(text, shift):
  result = []

  for char in text:
    if 'a' <= char <= 'z':
      shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
      result.append(shifted)
    elif 'A' <= char <= 'Z':
      shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
      result.append(shifted)
    else:
      result.append(char)

  return ''.join(result)

message = input("Enter the text to be encoded/decoded: ")
shift = int(input("Enter the shift value (1-25): "))
encoded_text = rot(message, shift)
print("Encoded/Decoded text:", encoded_text)