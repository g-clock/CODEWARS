def correct(string):
    newstring = ""
    for char in string:
        if char == "0":
          newstring += "O"
        elif char == "1":
          newstring += "I"
        elif char == "5":
          newstring += "S"
        else:
          newstring += char
    return newstring
