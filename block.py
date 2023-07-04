from hashlib import sha256


def updatehash(*args):
    hashing_text = ""
    h = sha256()

    for arg in args:
        hashing_text += arg
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block():
    data = ""
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def set_hash(self):
        return updatehash(self.previous_hash,
                          str(self.number),
                          self.data,
                          str(self.nonce))

    def __str__(self):
        return "\n Block:" + str(
            self.number) + "\n Hash: " + self.set_hash() + "\n Previous:" + self.previous_hash + "\n Data:" + self.data + "\n Nonce:" + str(
            self.nonce)
