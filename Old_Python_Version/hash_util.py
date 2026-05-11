import hashlib
import bcrypt

def hashPassword(password, hash_type):

    Ltype = hash_type

    if Ltype == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    
    elif Ltype == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    
    elif Ltype == "sha224":
        return hashlib.sha224(password.encode()).hexdigest()
    
    elif Ltype == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()
    
    elif Ltype == "bcrypt":
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)
    
    else:
        print("Unsupported Hash")