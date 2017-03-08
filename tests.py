import cipher

plaintext = 'Hello, world!'
print("Plaintext: {}".format(plaintext))

# Test atbash cipher
ciphertext = cipher.atbash(plaintext)
print("Atbash: {}".format(ciphertext))

# Test default caesar cipher
ciphertext = cipher.caesar(plaintext)
print("Default Caesar (shift 3): {}".format(ciphertext))

# Test caesar cipher with custom shift
ciphertext = cipher.caesar(plaintext, 19)
print("Caesar (shift 19): {}".format(ciphertext))

# Test rot13 cipher
ciphertext = cipher.rot13(plaintext)
print("ROT13: {}".format(ciphertext))

# Test keyword cipher
ciphertext = cipher.keyword('python', plaintext)
print("Keyword (keyword 'python'): {}".format(ciphertext))
