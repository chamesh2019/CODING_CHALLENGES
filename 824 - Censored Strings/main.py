def unsensor(text: str, vovels: list) -> str:
    """
    Replaces asterisks in the given text with the specified vowels from the `vovels` list.
    
    Args:
        text (str): The input text with asterisks to be replaced.
        vovels (list): List of vowels to replace the asterisks in the text.
        
    Returns:
        str: The text with asterisks replaced by the specified vowels.
    """
    
    for vovel in vovels:
        text = text.replace("*", vovel, 1)
    return text