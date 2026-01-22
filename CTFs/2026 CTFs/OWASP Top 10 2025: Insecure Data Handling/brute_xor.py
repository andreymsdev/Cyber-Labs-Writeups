import base64

# List of encrypted notes from the lab
encrypted_notes = [
    "BiA8RSIrPhE4JjFULzA1VC9lP145ZS1eJiorQyQyeVA/ZWoRGwh3EQgqN1cuNzxfKCB5QyQqNBEJaw==", # Note 1
    "GyQqQjwqK1VrNzxCLjF5XSIrMgtrLS1FOzZjHmQsN0UuNzdQJ2stWSZqK1Q4IC0OPyoyVCV4OFModGsC"  # Note 2
]

# The key found through brute force
key = "KEY1"

print(f"--- Decrypting Notes using Key: {key} ---")

for i, note_b64 in enumerate(encrypted_notes, 1):
    # Step 1: Decode from Base64 to get raw bytes
    cipher_data = base64.b64decode(note_b64)
    
    # Step 2: Decrypt using Repeating XOR logic
    decrypted = ""
    for j in range(len(cipher_data)):
        # The modulo operator (%) ensures the 4-char key repeats over the message
        decrypted += chr(cipher_data[j] ^ ord(key[j % 4]))
    
    print(f"\n[+] Note #{i} Decrypted:")
    print(f"    {decrypted}")