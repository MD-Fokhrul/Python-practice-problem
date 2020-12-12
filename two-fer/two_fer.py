def two_fer(name = "you"):
    try:
        return "One for " + name +", one for me."
    except:
        raise Exception("may be input Error")
        
