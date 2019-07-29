import random
import string

def key_gen():
    key = "".join(random.choices(string.ascii_letters+string.digits,k=100))
    return key

if __name__ == "__main__":
    print(key_gen())
