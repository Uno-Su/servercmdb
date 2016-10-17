import hashlib


def md5_crypt(string):
    return hashlib.new('md5', string).hexdigest()


def salt_crypt(string, salt):
    return md5_crypt(string.encode() + salt.encode())


