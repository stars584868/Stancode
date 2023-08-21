"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    death = 0

    # Add the animation loop here!
    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)
        # Check the border and middle of the ball to change the directions
        ball_upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball_upper_right = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        ball_lower_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        ball_lower_right = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,
                                                         graphics.ball.y+graphics.ball.height)
        ball_middle = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width/2,
                                                    graphics.ball.y + graphics.ball.height/2)
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window_width - graphics.ball.width:
            graphics.set_vx(-vx)
        if graphics.ball.y <= 0:
            graphics.set_vy(-vy)
        if graphics.ball.y >= graphics.window_height - graphics.ball.height:
            graphics.set_reset()
            death += 1
        if ball_lower_left or ball_lower_right or ball_upper_left or ball_upper_right \
                is not graphics.ball or graphics.score:
            if ball_upper_left is not None:
                graphics.set_vy(-vy)
                if ball_upper_left is not graphics.paddle:
                    graphics.window.remove(ball_upper_left)
                    graphics.set_score()
            elif ball_upper_right is not None:
                graphics.set_vy(-vy)
                if ball_upper_right is not graphics.paddle:
                    graphics.window.remove(ball_upper_right)
                    graphics.set_score()
            elif ball_lower_left is not None:
                graphics.set_vy(-vy)
                if ball_lower_left is not graphics.paddle:
                    graphics.window.remove(ball_lower_left)
                    graphics.set_score()
            elif ball_lower_right is not None:
                graphics.set_vy(-vy)
                if ball_lower_right is not graphics.paddle:
                    graphics.window.remove(ball_lower_right)
                    graphics.set_score()
            elif ball_middle is graphics.paddle:
                graphics.set_reset()
        # Stop the game when the live become zero or the bricks are all broken
        if death == NUM_LIVES or graphics.brick_counts == graphics.score:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
