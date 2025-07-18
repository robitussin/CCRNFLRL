import gym

env = gym.make("FrozenLake-v1", render_mode="human")
env.reset()
# render the environment
env.render()

# observation space - states
env.observation_space

# actions: left -0, down - 1, right - 2, up- 3
env.action_space


# generate random action
randomAction = env.action_space.sample()
returnValue = env.step(randomAction)
# format of returnValue is (observation,reward, terminated, truncated, info)
# observation (object)  - observed state
# reward (float)        - reward that is the result of taking the action
# terminated (bool)     - is it a terminal state
# truncated (bool)      - it is not important in our case
# info (dictionary)     - in our case transition probability


env.render()

# perform deterministic step 0,1,2,3
returnValue = env.step(1)


# reset the environment
env.reset()

# transition probabilities
# p(s'|s,a) probability of going to state s'
#          starting from the state s and by applying the action a

# env.P[state][action]
env.P[0][1]
# output is a list having the following entries
# (transition probability, next state, reward, Is terminal state?)

# close the environment
env.close()
