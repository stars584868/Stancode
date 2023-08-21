from campy.graphics.gobjects import GOval       # class外空2行，內1行，底1行


print(f'robot.py(__name__): {__name__}')


class Robot:
    # Constructor
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    # method
    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f'h={self.h}/w{self.w}')

    def bmi(self):
        h_in_meter = self.h/100
        print('bmi', self.w/(h_in_meter**2))

    @staticmethod
    def say_hi():
        print('hi')


class Robot2(Robot):
    def __init__(self, height2, weight2, color2='green', count2=3):
        super().__init__(height2, weight2, color=color2)
        self.count = count2

    def stars_count(self):
        for i in range(self.count):
            print(i+1)
