def get_individual_scores(arr):
    player_one_strike = True
    player_one_score = 0
    player_two_score = 0

    for runs in arr:
        if player_one_strike:
            player_one_score += runs
        else:
            player_two_score += runs
        
        if runs % 2 != 0:
            player_one_strike = not player_one_strike
    
    return f'P1 : {player_one_score}, P2 : {player_two_score}'

arr = [1,2, 2]
print(get_individual_scores(arr))