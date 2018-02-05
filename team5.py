####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Super cool' # Only 10 chars displayed.
strategy_name = 'super cool strategy'
strategy_description = 'Retaliates unless opponent betrays too much'

global numberOfBetrayals

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    def probability_of_betrayal(betrayals, totalRounds):
        betrayalProbability = (betrayals/totalRounds) * 100 #Calculates the percentage of times the opponent has been betraying.
        if betrayalProbability >= 70: # If the opponent colludes at least 70% of the time, switch to betraying only.
            return True
        else:
            return False
            
    global numberOfBetrayals

    if len(my_history) == 0: #if its the first round, initialize the numberOfBetrayals variable.
        numberOfBetrayals = 0 #This is a variable which holds the number of times the opponent has betrayed.

    if len(my_history) >= 100: #After 100 rounds, call the probability_of_betrayal procedure to see whether the opponent has mainly been betraying
        if probability_of_betrayal(numberOfBetrayals, len(my_history)): #If opponent is mainly betraying, betray them from now on.
            return 'b'
        
    if len(my_history) == 0: #start off by colluding
        return 'c'
    elif their_history[-1] == 'b': #if the opponent betrayed in the previous round, betray them in return
        numberOfBetrayals += 1 #add to the total number of times the opponent colluded
        return 'b'
    elif their_history[-1] == 'c': #if the opponent colluded in the previous round, collude with them in return.
        return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             