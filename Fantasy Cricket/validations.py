from utilities import get_user_teamnames_2, get_userteam_details

def validate_teamname(team_name):
    error_0 = "Your team name cannot be an empty string!"
    error_1 = "Your team name shouldn't exceed seventy characters in length!"
    error_2 = "Your team name shouldn't contain only spaces!"
    error_3 = "Your team name shouldn't start with a non alphanumeric character!"
    error_4 = "Your team name shouldn't contain any special characters!"

    list_chars = list(ord(char) for char in team_name)
    contains_special_character = False
    for char in list_chars:
        if ((char >=0 and char <= 31) or (char >= 33 and char <= 47) or (char >= 58 and char <= 64) or (char >= 91 and char <= 96) or (char >= 123 and char <= 127)):
            contains_special_character = True
            break
    user_teamnames_2 = get_user_teamnames_2()
    already_exists = team_name in [user_teamname[0] for user_teamname in user_teamnames_2]
    if len(team_name) == 0:
        return [False, error_0]
    first_character = ord(team_name[0])
    validity = True
    if len(team_name) > 70:
        return [False, error_1]
    if team_name.isspace():
        return [False, error_2]
    if not((first_character > 64 and first_character < 91) or (first_character > 96 and first_character < 123)):
        return [False, error_3]
    if contains_special_character:
        return [False, error_4]
    if already_exists:
        error_4 = "Team " + "\"" + str(team_name) + "\"" + " already exists! Rename your team"
        return [False, error_4]
    return [validity, " "]

def save_team_validation(player_ids_1, user_team_name, match_chosen):
    userteam_details = get_userteam_details(user_team_name, match_chosen)
    player_ids_2 = list(int(player_id) for player_id in userteam_details[2][1:-1].split(", "))
    player_ids_1.sort(), player_ids_2.sort()
    if player_ids_1 == player_ids_2:
        return True
    else:
        return False
