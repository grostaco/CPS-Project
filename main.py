from navigation import Environment, State, Robot


TIME_STEP = 64


def move(env: Environment):
    print('Moving')
    robot = env['Robot']
    for left_wheel in robot.left_wheels:
        left_wheel.setVelocity(10.0)
    for right_wheel in robot.right_wheels:
        right_wheel.setVelocity(10.0)


def rotate(env: Environment):
    print('Rotating')
    robot = env['Robot']
    for left_wheel in robot.left_wheels:
        left_wheel.setVelocity(10.0)
    for right_wheel in robot.right_wheels:
        right_wheel.setVelocity(0.0)
def noop(env: Environment):
    print('In noop')
    robot = env['Robot']
    for left_wheel in robot.left_wheels:
        left_wheel.setVelocity(0.0)
    for right_wheel in robot.right_wheels:
        right_wheel.setVelocity(0.0)


env: Environment = {'Robot': Robot(), 'TIME_STEP': TIME_STEP}
state = State(noop)
move_state = State(rotate)
state.connect(move_state, lambda e: e['TIME_STEP'] == 100)
move_state.connect(state, lambda e: e['TIME_STEP'] == 120)


while env['Robot'].step(env['TIME_STEP']) != -1:
    if new_state := state.update(env):
        state = new_state
    env['TIME_STEP'] += 1
