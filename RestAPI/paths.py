from flask_restful import Api, Resource, reqparse
from dbFunctions import *
import numpy as np
import json

class UserPath(Resource):
    def get(self):
        jsonData = executeQuery("Select * from users;")
        return jsonData, 200    

class UserNamePath(Resource):

    def get(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("username")
        parser.add_argument("password")

        args = parser.parse_args()
        jsonData = executeQuery("SELECT * FROM users WHERE password = " + "\'" + str(args["username"]) + "\'" + "AND username ="  + "\'" +str(args["password"]) + "\';" )
        
        hasData = "results" in jsonData
        if hasData:
            return jsonData, 200
        else:
            return 400

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("username")
        parser.add_argument("password")

        args = parser.parse_args()

        insert("INSERT INTO users (username,password) VALUES(" + "\'" + str(args["username"])  + "\'" + "," + "\'" + str(args["password"]) + "\'" + ");")
        return 200

class MakeMove(Resource):


    def get(self, gameid):
        parser = reqparse.RequestParser()
        parser.add_argument("gameid")
        args = parser.parse_args()
        jsonData = executeQuery("SELECT * FROM moves WHERE gameid = " + "\'" + str(args["gameid"]) + "\';" )
        j = json.loads(jsonData)
        print(j)
        #new board of size 6x9
        board = np.zeros((6,9))


        #populates the board
        for move in j['results']:
            board[move['x']][move['y']] = move['playerid']

        ###Fully populated board
        board = np.flip(board, 0)

        #check if player 1 won
        for player in range(3):
            if player == 0:
                print("")
            else:
                ##Check Horizontol win coniditon
                for col in range(9-3):
                    for row in range(6):
                        if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                            print("player " + str(player) + " wins!")
                            insert("UPDATE games SET gamestate = " + "\'" + str(player) + "\' WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")

                ##Check vertical win condition
                for col in range(9):
                    for row in range(6-3):
                        if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                            insert("UPDATE games SET gamestate = " + "\'" + str(player) + "\' WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")
        
                ##Check right diagnol 
                for col in range(9-3):
                    for row in range(6-3):

                        if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                            insert("UPDATE games SET gamestate = " + "\'" + str(player) + "\' WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")
                ##Check left diagnol
                for col in range(9-3):
                    for row in range(3, 6):
                        
                        if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                            insert("UPDATE games SET gamestate = " + "\'" + str(player) + "\' WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")

        print(board)
                    
        return jsonData, 200

    def post(self, gameid):
        parser = reqparse.RequestParser()
        parser.add_argument("gameid")
        parser.add_argument("y")
        parser.add_argument("playerid")

        args = parser.parse_args()

        jsonData = executeQuery("SELECT * FROM moves WHERE gameid = " + "\'" + str(args["gameid"]) + "\';" )
        j = json.loads(jsonData)

        jsonDataForGame = executeQuery("SELECT * FROM games WHERE gameid = " + "\'" + str(args["gameid"]) + "\';" )
        j2 = json.loads(jsonDataForGame)
        player1 = ""
        player2 = ""

        for move in j2['results']:
            if(str(args["playerid"]) == str(move['player_1'])):
                player2 = str(move['player_2'])
                print("dsadddddddddddd====")
            else:
                player2 = str(move['player_1'])
                print("AS=================")
        print(player2)
        #new board of size 6x9
        board = np.zeros((6,9))


        #populates the board
        for move in j['results']:
            board[move['x']][move['y']] = move['playerid']

        ###Fully populated board
        placed = True
        board = np.flip(board, 0)
        for row in range(6):
            if board[5-row][int(args["y"])] == 0 and placed:
                insert("INSERT INTO moves (gameid,x,y,playerid) VALUES(" + "\'" + str(args["gameid"])  + "\'" + "," + "\'" + str(row) + "\'" + "," + "\'" + str(args["y"]) + "\'" + "," + "\'" + str(args["playerid"]) + "\'"  ")")
                insert("UPDATE games SET current_player_turn = " + "\'" + player2 + "\' WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")
                placed = False
                print("Places success at " + str(5-row) + "x" + args["y"])
        
        if placed:
            print("invalid move!")

        
        return 200

class AllGame(Resource):
    def get(self):
        jsonData = executeQuery("SELECT * FROM games;" )

        hasData = "gameid" in jsonData
        if hasData:
            return jsonData, 200
        else:
            return 400

class Game(Resource):
    def get(self, gameid):
        parser = reqparse.RequestParser()
        parser.add_argument("gameid")

        args = parser.parse_args()

        jsonData = executeQuery("SELECT * FROM games WHERE gameid = " + "\'" + str(args["gameid"]) + "\';" )

        hasData = "gameid" in jsonData
        if hasData:
            return jsonData, 200
        else:
            return 400

    def post(self, gameid):
        parser = reqparse.RequestParser()
        parser.add_argument("player_1")

        args = parser.parse_args()

        insert("INSERT INTO games (player_1, current_player_turn) VALUES(" + "\'" + str(args["player_1"]) + "\'" + "," +"\'" + str(args["player_1"]) + "\'"  ");")
        return 200     

class FindGame(Resource):
    def get(self, playerid):
        parser = reqparse.RequestParser()
        parser.add_argument("playerid")

        args = parser.parse_args()

        jsonData = executeQuery("SELECT * FROM games WHERE player_1 = " + "\'" + str(args["playerid"]) + "\' and gamestate = \'-1\';" )

        hasData = "gameid" in jsonData
        if hasData:
            return jsonData, 200
        else:
            return 400

class JoinGame(Resource):
    def post(self, gameid):
        parser = reqparse.RequestParser()
        parser.add_argument("player_2")
        parser.add_argument("gameid")
        args = parser.parse_args()

        insert("UPDATE games SET player_2 = " + "\'" + str(args["player_2"]) + "\' WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")
        insert("UPDATE games SET gamestate = 0 WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")
        return 200


class disconnect(Resource):
    def post(self, gameid):
        parser = reqparse.RequestParser()
        parser.add_argument("gameid")
        args = parser.parse_args()

        insert("UPDATE games SET gamestate = -1 WHERE gameid = " + "\'" +  str(args["gameid"]) + "\';")
        return 200