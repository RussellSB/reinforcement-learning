from frozen_lake import FrozenLake

def main():
    seed = 0

    # Small lake
    lake = [['&', '.', '.', '.'],
            ['.', '#', '.', '#'],
            ['.', '.', '.', '#'],
            ['#', '.', '.', '$']]

    env = FrozenLake(lake, slip=1, max_steps=16, seed=seed)
    env.play()

    print('# Model-based algorithms')
    gamma = 0.9
    theta = 0.001
    max_iterations = 100

    print('')

    print('## Policy iteration')
    #policy, value = policy_iteration(env, gamma, theta, max_iterations)
    #env.render(policy, value)

    print('')

    print('## Value iteration')
    #policy, value = value_iteration(env, gamma, theta, max_iterations)
    #env.render(policy, value)

main()