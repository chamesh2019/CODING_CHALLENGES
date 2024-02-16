def bonus(days: int) -> int:
    """
    Calculate bonus based on the number of days worked.
    
    Parameters:
    days (int): The number of days worked.
    
    Returns:
    int: The bonus amount.
    """
    if days > 48:
        return (8 * 550) + (8 * 325) + (days - 48) * 600
    
    if days > 40:
        return (8 * 325) + (days - 40) * 550
    
    if days > 32:
        return (days - 32) * 325

    return 0
