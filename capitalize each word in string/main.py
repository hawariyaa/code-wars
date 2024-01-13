# capitailze each word in a string
def to_jaden_case(string):
    # ...
    new = []
    for word in string.split():
         new.append(word.capitalize())
    return " ".join(new)