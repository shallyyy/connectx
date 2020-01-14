from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import psycopg2
from paths import *

app = Flask(__name__)
api = Api(app)

api.add_resource(UserPath, "/user/")

api.add_resource(UserNamePath,"/user/<string:name>")

api.add_resource(MakeMove, "/move/<string:gameid>")

api.add_resource(Game, "/games/<string:gameid>")

api.add_resource(JoinGame, "/joinGame/<string:gameid>")

api.add_resource(FindGame, "/findGame/<string:playerid>")

api.add_resource(AllGame, "/getGames/")


api.add_resource(disconnect, "/disconnect/<string:gameid>")



app.run(debug=True, host= 'localhost')

