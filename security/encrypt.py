##Side task to add a little twist
##simple caesar cipher, will shift each letter by 5, so: A -> F...
# based on the range of the ascii table 94
from robots.robots import robot1,robot2
shift = 5

def encryption(message, shift):
    encrypted = ''
    for char in message:
        encrypted += chr((ord(char) + shift - 32) % 95 + 32)
    return encrypted

#reverse the operation to decrypt the message
def decryption(text, shift):
    decrypted = ''
    for char in text:
        decrypted += chr((ord(char) - shift - 32) % 95 + 32)
    return decrypted

def send_message(robot, message,shift):
    encrypted = encryption(message, shift)
    print(f"Encrypted message from Robot{robot['id']}: {encrypted}")
    return encrypted

def decrypt_message(robot, encrypted_message, shift):
    decrypted = decryption(encrypted_message, shift)
    print(f"Decrypted message from Robot{robot['id']}: {decrypted}")
    return decrypted

#print(f"Fruit delivered to base by Robot {robot['id']}")