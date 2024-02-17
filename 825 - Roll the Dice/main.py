faces = ["", "---/-O-/---", "O--/---/--O", "O--/-O-/--O", "O-O/---/O-O","O-O/-O-/O-O", "O-O/O-O/O-O"]

def dice(number: int) -> str:
    """
    A function that takes an integer number and returns a string representing the result of rolling a dice with the given number of spots.
    """
    result = ""
    while number >= 6:
        if result:
            result += ", "
        result += faces[6]
        number -= 6
    
    if number and result:
        result += ", "
    result += faces[number]
    return result