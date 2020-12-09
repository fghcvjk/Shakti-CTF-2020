import hashlib
from secret import flag
import string

chars = list(string.ascii_lowercase + string.digits)
m = hashlib.md5()
assert len(flag) == 5
assert all(c in chars for c in flag)
m.update("shaktictf{" + flag + "}")
print m.hexdigest()
