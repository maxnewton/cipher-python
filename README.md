# Cipher-Python Module
Cipher-Python is a library of easy-to-use [classical cryptographs](https://en.wikipedia.org/wiki/Classical_cipher) for any code-writing (or breaking!) enthusiast. It's based on [Cipher++](https://github.com/maxnewton/cipherplusplus), a C++ implementation of classical ciphers I began working on a few months ago.

Cipher-Python includes:

* Substitution ciphers
  * Atbash cipher
  * Caesar cipher
  * ROT13 cipher
  * Keyword cipher

With plans to add:

* Transposition ciphers
  * Columnar transposition cipher
  * Double transposition cipher

# What's the big deal?

I use my free time to create cool things and release them - for free - here on GitHub. It's that simple!

If you like what I do and want to see more, [consider becoming a Patreon supporter](https://www.patreon.com/aaronpowell). To give back to the community, 10% of your monthly support is donated to the amazing open-source initiatives that help make these projects happen.

# How to install

Cipher-Python is designed to be portable, and can be included in any Python project. To add Cipher-Python to your project, simply download or clone this repository and copy the "cipher" folder into your project directory.

## How to use: Atbash cipher
The Atbash cipher gets its name from the first, second, and second-to-last letters of the Hebrew alphabet (Aleph, Tav, Beth, and Shin, or "ATBSh"). To use this cipher, simply take the alphabet and reverse it ("ABCDEFGHIJKLMNOPQRSTUVWXYZ" becomes "ZYXWVUTSRQPONMLKJIHGFEDCBA"). Let's take a look at it in action:

    import cipher

    ciphertext = cipher.atbash("Hello, world!")
    print(ciphertext)

## How to use: Caesar cipher
The caesar cipher is one of the most popular substutution ciphers, first used by Julius Caesar in private letters and other correspondence. It's also known as a shift cipher, Caesar's code, or Caesar shift. In a caesar cipher, each letter of the alphabet is shifted left or right by a constant value. Caesar ciphers often shift the alphabet by 3 letters, so "a" becomes "d", "b" becomes "e", "c" becomes "f", etc. Cipher-Python shifts a caesar cipher-encrypted string by 3 letters by default, but you can override this with any number you like. For example:

    import cipher
    
    # Default shift of 3
    ciphertext = cipher.caesar("Hello, world!")
    print(ciphertext)

    # Shift alphabet by 11 letters
    ciphertext = cipher.caesar("Hello, world!", 11)
    print(ciphertext)

# How to use: ROT13 cipher
A ROT13 cipher splits the alphabet right down the center, so "a" corresponds to "m" (and vise versa), "b" to "n", "c" to "o", etc. More simply, it's a caesar cipher with a constant shift (or ROTation) of 13 letters.

    import cipher

    ciphertext = cipher.rot13("Hello, world!")
    print(ciphertext)

    # Let's compare it to the caesar cipher (hint: it's the same!)
    ciphertext = cipher.caesar("Hello, world!", 13)
    print(ciphertext)

## How to use: Keyword cipher

