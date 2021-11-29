import controller
from itertools import chain


class Robot(controller.Robot):
    def __init__(self):
        super().__init__()
        self.left_wheels = [self.getDevice(f'wheel{i}') for i in (1, 3)] 
        self.right_wheels = [self.getDevice(f'wheel{i}') for i in (2, 4)] 
        for wheel in chain.from_iterable([self.left_wheels, self.right_wheels]):
            wheel.setPosition(float('inf'))
            wheel.setVelocity(0.0)
