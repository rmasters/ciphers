from vigenere import repeat_string_to_length, encrypt, decrypt


def test_repeat_string():
    assert 'abca' == repeat_string_to_length('abc', 4)


def test_encrypt():
    assert 'JSOPQKRVNR' == encrypt('HELLOWORLD', 'CODE')


def test_decrypt():
    assert 'HELLOWORLD' == decrypt('JSOPQKRVNR', 'CODE')


def test_decrypt_gchq():
    assert 'ONEHUNDREDYEARS' == decrypt('UPLXAPKHKFFUGTZ', 'GCHQ')

