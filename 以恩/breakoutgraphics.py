"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
SPEED_UP = 1           # Speed adding up after brick is broken

# Global Variables
is_first_click = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 speed_up=SPEED_UP):
        self.speed_up = speed_up

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.window.add(self.paddle, x=self.window_width/2-paddle_width/2,
                        y=self.window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'orange'
        self.window.add(self.ball, x=self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_ball)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if j == 0:
                    brick.fill_color = 'yellow'
                elif i % 2 == 1:
                    brick.fill_color = 'blue'
                elif i % 2 == 0:
                    brick.fill_color = 'red'
                self.window.add(brick, x=i*(brick_width+brick_spacing), y=j*(brick_height+brick_spacing)+brick_offset)
        self.brick_counts = BRICK_COLS*BRICK_ROWS

        # score counter
        self.score = 0
        self.score_label = GLabel(f'Score: {self.score}')
        self.window.add(self.score_label, x=0, y=self.window_height-self.score_label.height)

    # Start with mouse click
    def start_ball(self, mouse):
        global is_first_click
        if is_first_click is True:
            is_first_click = False
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # Let paddle follow the mouse
    def paddle_move(self, mouse):
        if PADDLE_WIDTH/2 <= mouse.x <= self.window_width-PADDLE_WIDTH/2:
            self.paddle.x = mouse.x-PADDLE_WIDTH/2

    # Reset the ball
    def set_reset(self):
        global is_first_click
        is_first_click = True
        self.__dx = 0
        self.__dy = 0
        self.ball.x = self.window_width/2-self.ball.width/2
        self.ball.y = self.window_height/2-self.ball.height/2

    # score counter
    def set_score(self):
        self.score += 1
        self.__dy += self.speed_up
        self.score_label.text = f'Score: {self.score}'

    def set_vx(self, new_vx):
        self.__dx = new_vx

    def set_vy(self, new_vy):
        self.__dy = new_vy

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy
