import bcrypt

SALT = bcrypt.gensalt()


def encryptPassword(password: str):
    return bcrypt.hashpw(password, SALT)


def comparePassword(password: str, pwHashed):
    return bcrypt.checkpw(password, pwHashed)
