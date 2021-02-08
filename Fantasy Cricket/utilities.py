import sqlite3 as sq
matches_query = "SELECT MATCHNUMBER, VERSUS FROM MATCHES;"
batsmen_query = "SELECT PLAYER FROM PLAYERS WHERE PLAYERTEAM = 'IND' AND PLAYERROLE = 'BAT';"
user_teamnames_query = "SELECT SQUADNAME FROM USERSQUADS;"

def get_connection():
    conn = sq.connect('storage.db')
    curs = conn.cursor()
    lis = [conn, curs]
    return lis

def get_matches():
    conn, curs = get_connection()
    curs.execute(matches_query)
    matches = curs.fetchall()
    conn.close()
    return matches

def get_versus(match_number):
    conn, curs = get_connection()
    curs.execute("SELECT VERSUS FROM MATCHES WHERE MATCHNUMBER = '" + str(match_number) + "';")
    versus = curs.fetchone()
    conn.close()
    return versus

def get_full_teamname(team_code):
    conn, curs = get_connection()
    curs.execute("SELECT TEAMNAME FROM TEAMS WHERE TEAMCODE = '" + str(team_code) + "';")
    full_teamname = curs.fetchone()
    conn.close()
    return full_teamname

def get_list_players(team, role):
    conn, curs = get_connection()
    curs.execute("SELECT PLAYERID, PLAYERNAME, PLAYERVALUE FROM PLAYERS WHERE PLAYERTEAM = '" + str(team) + "' AND PLAYERROLE = '" + str(role) + "';")
    players = curs.fetchall()
    conn.close()
    return players

def get_player_details(player_id):
    conn, curs = get_connection()
    curs.execute("SELECT PLAYERNAME, PLAYERTEAM, PLAYERROLE, PLAYERVALUE FROM PLAYERS WHERE PLAYERID = '" + str(player_id) + "';")
    players = curs.fetchone()
    conn.close()
    return players

def get_match_details(match_chosen):
    conn, curs = get_connection()
    curs.execute("SELECT PLAYERIDS, SCORED, FACED, FOURS, SIXES, BOWLED, RUNSGIVEN, WICKETS, CATCHES, STUMPINGS, ROS FROM MATCHES WHERE MATCHNUMBER = '" + str(match_chosen) + "';")
    match_details = curs.fetchone()
    conn.close()
    return match_details

def insert_usersquad(squad_info, commit_flag):
    conn, curs = get_connection()
    squad_name = squad_info[0]
    match_number = squad_info[1]
    points_used = squad_info[2]
    team_value = squad_info[3]
    player_ids = squad_info[4]
    conn, curs = get_connection()
    try:
        curs.execute("INSERT INTO USERSQUADS(SQUADNAME, MATCHNUMBER, POINTSUSED, TEAMVALUE, PLAYERIDS) VALUES ('" + str(squad_name) + "', " + str(match_number) + ", " + str(points_used) + ", " + str(team_value) + ", '" + str(player_ids) + "')")
        if commit_flag:
            conn.commit()
        else:
            conn.rollback()
    except sq.IntegrityError:
        conn.close()
        return [False, True]
    except:
        conn.close()
        return [False, False]
    conn.close()
    return [True, False]

def delete_usersquad(user_team_name):
    conn, curs = get_connection()
    curs.execute("DELETE FROM USERSQUADS WHERE SQUADNAME = '" + str(user_team_name) + "';")
    conn.commit()

def get_user_teamnames(match_number):
    conn, curs = get_connection()
    curs.execute("SELECT SQUADNAME FROM USERSQUADS WHERE MATCHNUMBER = '" + str(match_number) + "';")
    user_teamnames = curs.fetchall()
    return user_teamnames

def get_user_teamnames_2():
    conn, curs = get_connection()
    curs.execute(user_teamnames_query)
    user_teamnames_2 = curs.fetchall()
    return user_teamnames_2

def get_userteam_details(team_name, match_number):
    conn, curs = get_connection()
    curs.execute("SELECT POINTSUSED, TEAMVALUE, PLAYERIDS FROM USERSQUADS WHERE SQUADNAME = '" + str(team_name) + "' AND MATCHNUMBER = '" + str(match_number) + "';")
    userteam_details = curs.fetchone()
    return userteam_details
