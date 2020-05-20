# SPDX-License-Identifier: AGPL-3.0-or-later
import arcade
import time


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()


arcade.Window()
# Keep the window open for 5 seconds, as a placeholder
time.sleep(5)
