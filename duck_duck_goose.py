# https://www.codewars.com/kata/582e0e592029ea10530009ce

def duck_duck_goose(players, goose):
    total_players = len(players)
    
    # Modulo by total_players to "walk in a circle".
    # Minus 1 since list index starts at 0
    player_selection = (goose % total_players) - 1
    
    player_name = players[player_selection].name
    
    return player_name