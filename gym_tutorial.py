import gym

env = gym.make("CartPole-v0")
env.reset()
print(env.reset())
box = env.observation_space
print(box)
action = env.action_space.sample()
observation, reward, done, info = env.step(action)

done = False
while not done:
    observation, r, d, _ = env.step(env.action_space.sample())
