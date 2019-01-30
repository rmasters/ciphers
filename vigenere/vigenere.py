import string

def generate_tabula_recta(alphabet):
    """
    Build an alphabet table as so:

    Alpha     Array     Alphabet-index

      A B C     0 1 2     0 1 2
    A A B C   0 A B C   0 0 1 2
    B B C D   1 B C D   1 1 2 3
    C C D E   2 C D E   2 2 3 4

    """

    table = []
    for x in range(0, len(alphabet)):
        table.append([])
        for y in range(0, len(alphabet)):
            # Wrap around the alphabet if overflow
            alpha_idx = (x + y) % len(alphabet)
            table[x].append(alphabet[alpha_idx])

    return table


def repeat_string_to_length(repeat_str, length):
    quot, rem = divmod(length, len(repeat_str))
    return repeat_str * quot + repeat_str[:rem]


def encrypt(cleartext, passphrase, alphabet=None):
    if alphabet is None:
        alphabet = string.ascii_uppercase

    table = generate_tabula_recta(alphabet)
    keyword = repeat_string_to_length(passphrase, len(cleartext))

    ciphertext = ''
    for i in range(0, len(cleartext)):
        ciphertext += table[alphabet.find(cleartext[i])][alphabet.find(keyword[i])]

    return ciphertext


def decrypt(ciphertext, passphrase, alphabet=None):
    if alphabet is None:
        alphabet = string.ascii_uppercase

    table = generate_tabula_recta(alphabet)
    keyword = repeat_string_to_length(passphrase, len(ciphertext))

    cleartext = ''
    for i in range(0, len(ciphertext)):
        col = table[alphabet.find(keyword[i])].index(ciphertext[i])
        cleartext += alphabet[col]

    return cleartext



