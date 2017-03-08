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
  * Columnar transposition cipher (not implemented yet)
  * Double transposition cipher (not implemented yet)

# What's the big deal?

I use my free time to create cool things and release them - for free - here on GitHub. It's that simple!

If you like what I do and want to see more, [consider becoming a Patreon supporter](https://www.patreon.com/aaronpowell). To give back to the community, 10% of your monthly support is donated to the amazing open-source initiatives that help make these projects happen.

# How to install

Cipher-Python is designed to be a portable library that can be included in any project. To add Cipher-Python to your project, simply download or clone this repository and copy the "cipher" folder into your own Python project.

## How to use: Atbash cipher
The Atbash cipher, originally used with the Hebrew alphabet, gets its name from the first, second, and second-to-last letters of the alphabet (Aleph, Tav, Beth, and Shin, or "ATBSh"). To create an atbash cipher alphabet, simply take the alphabet and reverse it. That means "ABCDEFGHIJKLMNOPQRSTUVWXYZ" becomes "ZYXWVUTSRQPONMLKJIHGFEDCBA". Let's take a look at it in action:

    import cipher

    ciphertext = cipher.atbash("Python is so cool!")
    print(ciphertext)

## How to use: Caesar cipher
The caesar cipher is a popular substutution cipher first used by Julius Caesar in his own private correspondence. It's also known as a shift cipher, Caesar's code, or Caesar shift. In a caesar cipher, each letter of the alphabet is shifted left or right by a constant value. For example, because caesar ciphers often shift the alphabet by 3, "a" becomes "d", "b" becomes "e", "c" becomes "f", etc. Cipher-Python defaults to a shift value of 3, but you can override this with any shift value you would like. For example:

    import cipher
    
    # Default shift of 3
    ciphertext = cipher.caesar("Python is so cool!")
    print(ciphertext)

    # Custom shift
    ciphertext = cipher.caesar("Python is so cool!", 11)
    print(ciphertext)
