from robot import Robot, Robot2
from campy.graphics.gwindow import GWindow


print(f'robot_starter.py(__name__): {__name__}')


def main():
    Robot.say_hi()

    window = GWindow()

    r1 = Robot(183, 70, color='blue')
    r1.say_hi()
    r1.self_intro()
    r1.bmi()
    ball1 = r1.give_me_a_ball(400)

    r2 = Robot(140, 50)
    r2.self_intro()
    r2.bmi()
    ball2 = r2.give_me_a_ball(300)

    r3 = Robot2(183, 78, color2='magenta', count2=10)
    r3.stars_count()
    r3.say_hi()
    r3.bmi()
    ball3 = r3.give_me_a_ball(100)
    window.add(ball3)

    window.add(ball1)
    window.add(ball2)


if __name__ == '__main__':
    main()
