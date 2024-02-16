def right_triangle(x: int, y: int, z: int) -> bool:
    sides = [x, y, z]
    if not all(side > 0 for side in sides):
        return False

    longest = max(sides)
    sides.remove(longest)

    if sides[0] ** 2 + sides[1] ** 2 == longest ** 2:
        return True
    
    return False

    