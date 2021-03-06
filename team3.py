####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rankine' # Only 10 chars displayed.
strategy_name = '50 rounds change'
strategy_description = 'After 50 moves will deploy a slightly different strategy'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
  
    def fifty_rounds(my_history):
        global fifty_moves
        fifty_moves = False
        if my_history  >= 50:
            fifty_moves = True 
            
    global fifty_moves
    if fifty_rounds:
        return 'b'
    else:
        if len(my_history) == 0:
            return 'b'
        elif len(my_history) == 1:
            return 'c'
        elif their_history[-1] == 'b':
            return 'b'
        elif their_history[-1] == 'c':
            return 'c'
        else:
            return 'c'
        return 'c'