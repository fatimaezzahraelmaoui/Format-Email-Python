import re

def Email(email):
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+$",eamil))

em =Email("sara23@gamil.com")
print(em)
            