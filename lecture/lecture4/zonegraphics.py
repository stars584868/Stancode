from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(width=window_width, height=window_height)
        # Create zone
        self.zone = GRect(zone_width, zone_height)
        self.zone.color = 'blue'
        self.window.add(self.zone, x=(self.window.width-self.zone.width)/2,
                        y=(self.window.height-self.zone.height)/2)
        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.set_ball_postition()
        self.window.add(self.ball)
        # Initialize mouse listeners

    def set_ball_postition(self):
        self.ball.x = random.randint(0, self.window.width-self.ball.width)
        self.ball.y = random.randint(0, self.window.height-self.ball.height)

    def get_vx(self):
        return random.randint(0, MAX_SPEED)

    def get_vy(self):
        return random.randint(MIN_Y_SPEED, MAX_SPEED)
