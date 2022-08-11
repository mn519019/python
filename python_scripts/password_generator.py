import string
from random import *

format   = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(format) for x in range(randint(10,16)))
print(password)