letters = list('abcdefghijklmnopqrstuvwxyz')

print("Type 'encode' to encrypt, type 'decode' to decrypt:")
choice = input()

if choice != 'encode' and choice != 'decode':
    print("Invalid choice.")
    exit()

message = input("Type your message: ").lower()
shift_number = int(input("Type your shift number: "))

if choice == 'decode':
    shift_number*=-1

message_indexes = list(map(lambda x: letters.index(x) + shift_number, list(message)))
decoded_message = ''.join(list(map(lambda x: letters[x], message_indexes)))

if choice == 'decode':
    print(f"Original message: {decoded_message}")
else:
    print(f"Encoded: {decoded_message}")

