package com.ConnectX;

import org.json.JSONException;

public class Main {

    public static void main(String[] args)  {
        try {
            connectx game = new connectx();
            game.runGame();
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
