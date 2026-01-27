# This program demonstrates a simple game statistics system.
# It uses lists to store player data, functions to organize the code,
# and list slicing to compute the K/D/A ratio of each player.
# The program displays each player's game statistics in a readable format.

# Displays the basic in-game statistics of a player
def display_player_stats(player_stats):
    name, id, level, rank, kills, deaths, assist = player_stats

    print("| PSI (STATS SECTION) |")
    print(f"Player Name   : {name} ({id})")
    print(f"Player Level  : {level}")
    print(f"Player Rank   : {rank}")
    print(f"Player Kills  : {kills}")
    print(f"Player Deaths : {deaths}")
    print(f"Player Assists: {assist}")

# Calculates the K/D/A ratio using kills, deaths, and assists and Prevents division by zero when deaths is equal to 0
def calculate_player_kda(player_kda):
    kills, deaths, assits = player_kda

    if deaths == 0:
        return kills + assits
    return (kills + assits) / deaths

# Main function to show player statistics
def show_player(player):
    display_player_stats(player)
    playerKDA = calculate_player_kda(player[4:])
    print(f"Player K/D/A Ratio: {playerKDA:.2f}")
    print()


# User Input Section (Newly added feature)
print("| PSI (INPUT SECTION) |")
name = input("Enter Player Name: ")
id = input("Enter Player ID: ")
level = int(input("Enter Player Level: "))
rank = input("Enter Player Rank: ")
kills = int(input("Enter Player Kills: "))
deaths = int(input("Enter Player Deaths: "))
assists = int(input("Enter Player Assists: "))

# Store user input in a list method
player = [name, id, level, rank, kills, deaths, assists]

# Main function to display player stats
show_player(player)

