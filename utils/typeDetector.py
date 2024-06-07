def isPrimitive(var):
    """
    Checks if the given variable is of a primitive type.
    
    Parameters:
    var (any): The variable to check.
    
    Returns:
    bool: True if the variable is a primitive type, False otherwise.
    """
    return isinstance(var, (int, float, bool, str, bytes))