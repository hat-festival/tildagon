from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable
from tildagonos import tildagonos

import app

from .lib.rgb_from_hue import rgb_from_hue


class HatVillage(app.App):
    """Village of Hats."""

    def __init__(self):
        """Construct."""
        self.button_states = Buttons(self)
        eventbus.emit(PatternDisable())

        self.hue = 0
        self.hue_increment = 0.005

        self.font_size = 48
        self.text_step_start = 240
        self.text_step = self.text_step_start
        self.text_step_increment = 8
        self.text_step_limit = -340

        self.text = "Hat Village"

    def update(self, _):
        """Update badge."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        elif self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.text_step_increment += 4

        elif self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            self.text_step_increment -= 4

    def draw(self, ctx):
        """Draw screen."""
        ctx.save()
        rgb = rgb_from_hue(self.hue)

        self.light_leds(rgb)
        self.fill_screen(ctx, rgb)
        self.write_text(ctx, rgb)

        self.hue = (self.hue + self.hue_increment) % 1.0

        ctx.restore()

    def fill_screen(self, ctx, rgb):
        """Fill the screen."""
        ctx.rgb(*rgb["decimals"]).rectangle(-120, -120, 240, 240).fill()

    def light_leds(self, rgb):
        """Light the LEDs."""
        for i in range(12):
            tildagonos.leds[i + 1] = rgb["bytes"]
        tildagonos.leds.write()

    def write_text(self, ctx, rgb):
        """Draw the text."""
        ctx.font_size = self.font_size
        baseline_offset = 12
        outline_size = 1

        for i in [0 - outline_size, outline_size]:
            for j in [0 - outline_size, outline_size]:
                ctx.rgb(*rgb["inverse"]).move_to(
                    self.text_step + i, baseline_offset + j
                ).text(self.text)

        ctx.rgb(*rgb["decimals"]).move_to(self.text_step, baseline_offset).text(
            self.text
        )

        self.text_step -= self.text_step_increment
        if self.text_step < self.text_step_limit:
            self.text_step = self.text_step_start


__app_export__ = HatVillage
