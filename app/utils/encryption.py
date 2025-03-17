import bcrypt

def hashed_password(password):
    pass_b = password.encode('utf-8') # convert to pybytes
    hashed_password = bcrypt.hashpw(pass_b, bcrypt.gensalt())

    return hashed_password.decode('utf-8')

def descrypt_password(password, hashed_password):
    retval = False
    pass_b = password.encode('utf-8')
    hs_pass_b = hashed_password.encode('utf-8')

    if bcrypt.checkpw(pass_b, hs_pass_b):
        retval = True
    
    return retval


