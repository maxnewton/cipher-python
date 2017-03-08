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

Cipher++ is designed to be a portable library that can be included in any project. To include Cipher++ in your project, simply download or clone this repository and copy the contents of the "include" folder into your own C++ project.

To download and compile the sample programs that come with Cipher++, choose from one of the following options. First, download or clone the repository:

    git clone https://github.com/maxnewton/cipherplusplus
    cd cipherplusplus

## How to use: Atbash cipher
The Atbash cipher, originally used with the Hebrew alphabet, gets its name from the first, second, and second-to-last letters of the alphabet (Aleph, Tav, Beth, and Shin, or "ATBSh"). To create an atbash cipher alphabet, simply take the alphabet and reverse it. That means "ABCDEFGHIJKLMNOPQRSTUVWXYZ" becomes "ZYXWVUTSRQPONMLKJIHGFEDCBA". Let's take a look at it in action:

    import cipher

    ciphertext = cipher.atbash("Python is so cool!")
    print(ciphertext)
