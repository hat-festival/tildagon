from events.input import BUTTON_TYPES, Buttons

import app

from .lib.utils import rgb_from_degrees


class ColourWheel(app.App):
    """Rorate the colours."""

    def __init__(self):
        """Construct."""
        self.button_states = Buttons(self)
        self.rotation = 0

    def update(self, _):
        """Update badge."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        """Draw screen."""
        ctx.save()
        rgb = rgb_from_degrees(self.rotation)
        ctx.rgb(*rgb).rectangle(-120, -120, 240, 240).fill()
        self.rotation = (self.rotation + 1) % 360

        ctx.restore()


__app_export__ = ColourWheel
