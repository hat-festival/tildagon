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

# segments = []
# for i in range(6):
#     offset = i * 60
#     red = blue = green = None
#     if i == 0:
#         red = 1
#         green = 0
#     if i == 1:
#         green = 0
#         blue = 1
#     if i == 2:
#         red = 0
#         blue = 1
#     if i == 3:
#         red = 0
#         green = 1
#     if i == 4:
#         green = 1
#         blue = 0
#     if i == 5:
#         red = 1
#         blue = 0
#     segments.append({"red": red, "green": green, "blue": blue, "offset": offset})


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

    rgb = [segment.get(x, offset) for x in ["red", "green", "blue"]]
    return {
        "decimals": tuple(rgb),
        "inverse": tuple([1 - x for x in rgb]),
        "bytes": tuple([int(x * 255) for x in rgb]),
    }
