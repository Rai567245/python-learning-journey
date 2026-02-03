# This program demonstrates a simple game statistics system.
# It uses lists to store player data, functions to organize the code,
# and list slicing to compute the K/D/A ratio of each player.
# The program displays each player's game statistics in a readable format.

# List of character and its in-game statistics
player1 = ["Rai", "011901", 19, "Platinum III", 150, 75, 40]

# Displays the basic in-game statistics of a player
def display_player_stats(player_stats): 
    name, id, level, rank, kills, deaths, assists = player_stats

    print("| PLAYER GAME STATISTICS |")
    print(f"Player Name   : {name} ({id})")
    print(f"Player Level  : {level}")
    print(f"Player Rank   : {rank}")
    print(f"Player Kills  : {kills}")
    print(f"Player Deaths : {deaths}")
    print(f"Player Assists: {assists}")

# Calculates the K/D/A ratio using kills, deaths, and assists and Prevents division by zero when deaths is equal to 0
def calculate_player_kda(player_kda):
    kills, deaths, assists = player_kda

    if deaths == 0:
        return kills + assists
    return (kills + assists) / deaths

# Calls the display and calculation functions and Displays the player's K/D/A ratio
def show_player(player):
    display_player_stats(player)
    playerKDA = calculate_player_kda(player[4:])
    print(f"Player K/D/A Ratio: {playerKDA:.2f}")
    print()

# Program execution
show_player(player1)
