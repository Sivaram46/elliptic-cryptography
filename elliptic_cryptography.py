from elliptic_element import EllipticGroupElement
from elliptic_group import EllipticGroup

class EllipticCryptography:
    def __init__(self, alpha, sk, a, b, m):
        self.a, self.b, self.m = a, b, m
        self.alpha = EllipticGroupElement(*alpha, self.a, self.b, self.m)
        self.sk = sk
        self.pk = self.alpha * sk
        self.group = EllipticGroup(a, b, m)
        if not len(self.group):
            raise ValueError(f"a={self.a}, b={self.b}, m={self.m} doesn't form a Elliptic group")

    def encipher(self, text, k=3):
        text = text.lower()
        ciphertext = ""
        self.y1 = self.alpha * k
        for char in text:
            m = self.group.elems[ord(char) - ord('a')]
            y = m + (self.pk * k)
            ciphertext += chr(self.group.elems.index(y) + ord('a'))

        return ciphertext, self.y1

    def decipher(self, text):
        plaintext = ""
        for char in text:
            x = self.group.elems[ord(char) - ord('a')]
            c = x - (self.y1 * self.sk)
            plaintext += chr(self.group.elems.index(c) + ord('a'))

        return plaintext

if __name__ == '__main__':
    # message = [(10, 9)]
    message = "sivaram"
    ecc = EllipticCryptography(alpha=(2, 2), sk=7, a=1, b=17, m=23)
    ciphertext = ecc.encipher(message)
    plaintext = ecc.decipher(ciphertext[0])

    print("Original text:", message)
    print("Ciphertext:", ciphertext)
    print("Deciphered:", plaintext)