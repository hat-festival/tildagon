from collections import deque
from math import floor


def get_segments():
    """Get the segments."""
    pattern = deque([1, None, 0, 0, None, 1])
    offsets = {"red": 0, "green": 2, "blue": 4}

    segments = []
    for i in range(6):
        segments.append({"offset": i * 60})
        for component, offset in offsets.items():
            pattern.rotate(0 - offset)
            if pattern[i] is not None:
                segments[-1][component] = pattern[i]
            pattern.rotate(offset)

    return segments


segments = get_segments()


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
