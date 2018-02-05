####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'PPEaters' # Only 10 chars displayed.
strategy_name = 'Winning'
strategy_description = 'Skill'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    global Move_B
   
    global Initial_Move
    
    def Move_B (their_history):
        global Move_B
        Move_B = False
        if their_history[-1]== 'b':
            Move_B = True
    
    
            
    def Initial_Move (my_history):
        global Initial_Move
        Initial_Move = False
        if len(my_history)==0:
            Initial_Move = True
            
                
         
        
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    

    
    if Initial_Move:
        return 'c'
   
   
    if Move_B:
        return 'b'
        
    else:
        return 'c'
        