from flask import Flask, jsonify
import psycopg2
import json

conn = psycopg2.connect(host="localhost",database="connectx", user="postgres", password="root")

cur = conn.cursor()
cur.execute("SET search_path TO tables;")
def executeQuery(query):
        cur.execute(query)
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data_inner = []
        for result in rv:
            json_data_inner.append(dict(zip(row_headers,result)))
        json_dict = {"results": json_data_inner}
        return json.dumps(json_dict, default=str)

def executeQueryParameterised(query, param):
        cur.execute(query, (param,))
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data_inner = []
        for result in rv:
            json_data_inner.append(dict(zip(row_headers,result)))
        json_dict = {json_data_inner}
        return json.dumps(json_dict)

def insert(query):
    print(query)
    cur.execute(query)
    conn.commit()
    return 200

def delete(query):
    cur.execute(query)
    conn.commit()
    return 200