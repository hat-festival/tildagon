
multiplier = 1 / 60


def rgb_from_degrees(degrees):
    if degrees >= 0 and degrees < 60:
        r = 1
        g = 0
        b = multiplier * degrees

    if degrees >= 60 and degrees < 120:
        r = 1 - multiplier * (degrees - 60)
        g = 0
        b = 1

    if degrees >= 120 and degrees < 180:
        r = 0
        g = multiplier * (degrees - 120)
        b = 1

    if degrees >= 180 and degrees < 240:
        r = 0
        g = 1
        b = 1 - multiplier * (degrees - 180)

    if degrees >= 240 and degrees < 300:
        r = multiplier * (degrees - 240)
        g = 1
        b = 0

    if degrees >= 300 and degrees < 360:
        r = 1
        g = 1 - multiplier * (degrees - 300)
        b = 0

    return (r, g, b)
