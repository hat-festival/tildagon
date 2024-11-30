from math import floor

sectors = [
    {"red": 1, "green": 0, "offset": 0},
    {"green": 0, "blue": 1, "offset": 60},
    {"red": 0, "blue": 1, "offset": 120},
    {"red": 0, "green": 1, "offset": 180},
    {"green": 1, "blue": 0, "offset": 240},
    {"red": 1, "blue": 0, "offset": 300},
]


def get_sector(degrees):
    """Determine which sector we're in."""
    return int(floor(degrees / 60))


def rgb_from_degrees(degrees):
    """Get RGB from degrees of rotation."""
    sector = sectors[get_sector(degrees)]
    offset = (1 / 60) * (degrees - sector["offset"])

    if get_sector(degrees) % 2 == 1:
        offset = 1 - offset

    return (
        sector.get("red", offset),
        sector.get("green", offset),
        sector.get("blue", offset),
    )
