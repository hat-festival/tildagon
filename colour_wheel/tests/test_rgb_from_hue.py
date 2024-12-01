from lib.rgb_from_hue import (
    get_sector,
    get_segments,
    rgb_from_degrees,
    rgb_from_hue,
)


def test_get_sector():
    """Test we can get the sector."""
    assert get_sector(0) == 0
    assert get_sector(60) == 1
    assert get_sector(150) == 2  # noqa: PLR2004


def test_rgb_from_degrees():
    """Test we can rgb from hue."""
    expectations = (
        (0, (1, 0, 0)),
        (15, (1, 0.25, 0)),
        (30, (1, 0.5, 0)),
        (60, (1, 1, 0)),
        (90, (0.5, 1, 0)),
        (120, (0, 1, 0)),
        (150, (0, 1, 0.5)),
        (180, (0, 1, 1)),
        (210, (0, 0.5, 1)),
        (240, (0, 0, 1)),
        (270, (0.5, 0, 1)),
        (300, (1, 0, 1)),
        (330, (1, 0, 0.5)),
    )

    for expectation in expectations:
        assert rgb_from_degrees(expectation[0])["decimals"] == expectation[1]


def test_rgb_from_hue():
    """Test we can rgb from hue."""
    expectations = (
        (0, (255, 0, 0)),
        (1 / 3, (0, 255, 0)),
        (1 / 2, (0, 255, 255)),
        (2 / 3, (0, 0, 255)),
    )

    for expectation in expectations:
        assert rgb_from_hue(expectation[0])["bytes"] == expectation[1]


def test_get_segments():
    """Test we get the segments."""
    assert get_segments() == [
        {"offset": 0, "red": 1, "blue": 0},
        {"offset": 60, "blue": 0, "green": 1},
        {"offset": 120, "red": 0, "green": 1},
        {"offset": 180, "red": 0, "blue": 1},
        {"offset": 240, "blue": 1, "green": 0},
        {"offset": 300, "red": 1, "green": 0},
    ]