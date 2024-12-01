from lib.utils import get_sector, get_segments, rgb_from_degrees


def test_get_sector():
    """Test we can get the sector."""
    assert get_sector(0) == 0
    assert get_sector(60) == 1
    assert get_sector(150) == 2  # noqa: PLR2004


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
        assert rgb_from_degrees(expectation[0])["decimals"] == expectation[1]


def test_get_segments():
    """Test we get the segments."""
    assert get_segments() == [
        {"red": 1, "green": 0, "offset": 0},
        {"green": 0, "blue": 1, "offset": 60},
        {"red": 0, "blue": 1, "offset": 120},
        {"red": 0, "green": 1, "offset": 180},
        {"green": 1, "blue": 0, "offset": 240},
        {"red": 1, "blue": 0, "offset": 300},
    ]
