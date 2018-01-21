info = {"Name": "Sterling", "Age": "28", "State of birth": "California", "Favorite language": "I like everything so far!"}

def dictionaryInfo(info):
    for key, data in info.iteritems():
        print key, "=", data
dictionaryInfo(info)
