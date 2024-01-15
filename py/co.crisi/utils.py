"""A sample module."""



def feet_to_meters(feet):
    """Convert feet to meters."""
    try:
        value = float(feet)
    except ValueError:
        print(f"Unable to convert to float: {feet}")
        return None
    else:
        return (0.3048 * value * 10000.0 + 0.5) / 10000.0
