from lib.utils import rgb_from_degrees


def test_rgb_from_degrees():
    """Test we can rgb from hue."""
    expectations = (
        (0, (1, 0, 0)),
        (15, (1, 0, 0.25)),
        (30, (1, 0, 0.5)),
        (60, (1, 0, 1)),
        (90, (0.5, 0, 1)),
        (120, (0, 0, 1)),
        (150, (0, 0.5, 1)),
        (180, (0, 1, 1)),
        (210, (0, 1, 0.5)),
        (240, (0, 1, 0)),
        (270, (0.5, 1, 0)),
        (300, (1, 1, 0)),
        (330, (1, 0.5, 0)),
    )

    for expectation in expectations:
        assert rgb_from_degrees(expectation[0]) == expectation[1]
