import random
import  string

a = string.ascii_letters + string.punctuation + string.digits
# random.shuffle(a)
s = "".join(random.sample(a,10))
print(a)
print(s)
