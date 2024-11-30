from math import floor

# undefined component will be calculated, using "offset"
# this can be generated
segments = [
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
    sector = get_sector(degrees)
    segment = segments[sector]
    offset = (1 / 60) * (degrees - segment["offset"])

    if sector % 2 == 1:
        offset = 1 - offset

    return [segment.get(x, offset) for x in ["red", "green", "blue"]]
