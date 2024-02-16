def tallest_skyscraper(arr: list) -> int:
    """
    Calculate the height of the tallest skyscraper in the 2D array.

    Parameters:
    arr (list): A 2D array representing the skyscrapers.

    Returns:
    int: The height of the tallest skyscraper.
    """
    arr = list(map(list, zip(*arr)))
    return max(sum(row) for row in arr)
