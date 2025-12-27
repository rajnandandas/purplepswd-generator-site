# password_logic.py
import random
import string

def generate_password(length=12, symbols=True):
    chars = string.ascii_letters + string.digits
    spc_chars = string.punctuation
    if symbols:
        chars += spc_chars
        pswd_final = ""
        while (len(set(pswd_final) & set(spc_chars))==0) or (len(set(pswd_final) & set(string.digits))==0):
            pswd_final = "".join(random.choice(chars) for _ in range(length))
        return pswd_final
    return "".join(random.choice(chars) for _ in range(length))
