# Fundamental Math for Data Science ---> Code Challenge
# Purpose: In the code editor below, we have written out a function called coin_flip_experiment() that simulates flipping two fair coins. Using a for loop we run coin_flip_experiment() a specific number of times. As this loop iterates, we track how often both coins come up as heads. Finally, using matplotlib, we plot the proportion of experiments resulting in two heads after each trial.
# The number of times coin_flip_experiment() runs is determined by the num_trials variable on line 21. Currently, this variable is set to 5. Run the program a few times. On the resulting plot, the orange horizontal line is the true probability of observing two heads (0.25). The blue line is the proportion of heads we see throughout our trials. What do you notice about the blue line after each run?
# You should see that the proportion of two heads after five trials is inconsistent. In some experiments, we may see zero observations of two heads, while in others, we may see almost all five observations are two heads. To simulate the law of large numbers, we need to do more trials. Set the num_trials variable to different values, such as these below: 10, 1000, 100000
# Take note of what you observe. Where does the blue line on the graph converge to after many trials?


import matplotlib.pyplot as plt
import numpy as np
import codecademylib3

def coin_flip_experiment():
  # defining our two coins as lists
  coin1 = ['Heads', 'Tails']
  coin2 = ['Heads', 'Tails']
 
  # "flipping" both coins randomly
  coin1_result = np.random.choice(coin1)
  coin2_result = np.random.choice(coin2)
 
  # checking if both flips are heads
  if coin1_result == 'Heads' and coin2_result == 'Heads':
    return 1
  else:
    return 0
 
# how many times we run the experiment
num_trials = 5
prop = []
flips = []
# keep track of the number of times heads pops up twice
two_heads_counter = 0
 
# perform the experiment five times
for flip in range(num_trials):
  # if both coins are heads add 1 to the counter
  two_heads_counter += coin_flip_experiment()
  # keep track of the proportion of two heads at each flip 
  prop.append(two_heads_counter/(flip+1))
  # keep a list for number of flips
  flips.append(flip+1)
 
# plot all flips and proportion of two heads
plt.plot(flips, prop, label='Experimental Probability')
plt.xlabel('Number of Flips')
plt.ylabel('Proportion of Two Heads')

plt.hlines(0.25, 0, num_trials, colors='orange', label='True Probability')
plt.legend()


 
plt.show()

#After setting num_trials to large numbers, we see that the proportion of trials resulting in two heads converges to 0.25. The horizontal line at y=0.25 is completely covered after about one hundred thousand flips. By simulating a huge number of flips in Python, we have shown that the true probability of seeing two heads on two separate coin flips is equal to 0.25.
