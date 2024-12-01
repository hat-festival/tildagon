from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .lib.utils import rgb_from_degrees


class ColourWheel(app.App):
    """Rorate the colours."""

    def __init__(self):
        """Construct."""
        self.button_states = Buttons(self)
        eventbus.emit(PatternDisable())

        self.rotation = 0
        self.increment = 2
        self.increment_limit = 16

    def update(self, _):
        """Update badge."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()
        elif self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            if self.increment < self.increment_limit:
                self.increment += 1
        elif self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            if self.increment > 1:
                self.increment -= 1

    def draw(self, ctx):
        """Draw screen."""
        ctx.save()
        rgb = rgb_from_degrees(self.rotation)
        ctx.rgb(*rgb["decimals"]).rectangle(-120, -120, 240, 240).fill()

        for i in range(12):
            tildagonos.leds[i + 1] = rgb["bytes"]

        tildagonos.leds.write()

        # ctx.rgb(1, 1, 1).move_to(-80, 0).text("Hat Village")

        self.rotation = (self.rotation + self.increment) % 360

        ctx.restore()


__app_export__ = ColourWheel
