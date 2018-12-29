# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = 0.1
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

    # Comment : Having a low discount makes the agent prefer instant rewards 
    # => Prefers the close exit (+1) and risks the cliff (-10)

def question3b():
    answerDiscount = 0.3
    answerNoise = 0.1
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

    # Comment : Having a low discount makes the agent prefer instant rewards, but adding noise
    # constraints him to not take risks => The agent prefers exit (+1) but avoids the cliff (-10)

def question3c():
    answerDiscount = 0.1
    answerNoise = 0.0
    answerLivingReward = 2.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

    # Comment : Having a low discount makes the agent prefer instant rewards, but adding a +1 < livingReward < +10
    # makes him prefer not to take the exit(+1) and take the exit(+10) via the shortest path 

def question3d():
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

    # Comment : When livingReward > max(Exitrewards) the agent prefers 
    # to stay in the map rather than taking the exit


def question3e():
    answerDiscount = 0.9
    answerNoise = 0.3
    answerLivingReward = 11.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

    # Comment : When livingReward > max(Exitrewards) the agent prefers 
    # to stay in the map rather than taking the exit

def question6():
    answerEpsilon = 1
    answerLearningRate = 1
    return 'NOT POSSIBLE' 

    # Even if we maximize epsilon so that the agent try to explore the other regions in the east of the map,
    # and even if we maximize the learning rate to make sure that the agent learn very fast, we do not garanty 
    # experimentaly that the agent learn the optimal policy in 50 iterations

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
