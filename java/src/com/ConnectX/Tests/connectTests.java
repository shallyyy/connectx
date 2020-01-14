package com.ConnectX.Tests;
import org.json.JSONException;
import org.junit.Test;

import com.ConnectX.connectx;

import java.util.ArrayList;

import static org.junit.Assert.*;

public class connectTests {
    public connectx game;
    {
        try {
            game = new connectx();
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    @Test
    public void boardForSpecifcGameTest() throws JSONException {
        assertEquals("\n" +
                "\n" +
                "\n" +
                "\n" +
                "\n" +
                "\n" +
                "\n" +
                "\n" +
                "\n" +
                "[1][ ][ ][1][ ][1][1][ ][1]\n" +
                "[1][1][ ][1][2][ ][ ][ ][1]\n" +
                "[1][ ][1][2][ ][ ][1][ ][1]\n" +
                "[1][ ][1][1][ ][ ][1][ ][1]\n" +
                "[1][1][ ][1][ ][1][1][ ][1]\n" +
                "[2][1][ ][1][ ][1][1][1][1]\n", game.getBoard(1));
    }

    @Test
    public void loginTestTrue() throws JSONException {
        assertEquals(true, game.login("Shally", "Root"));
    }
    @Test
    public void loginTestFalse() throws JSONException {
        assertEquals(false, game.login("Root", "Root"));
    }
    @Test(expected =  RuntimeException.class)
    public void registerExistingUser() throws JSONException {
        game.registerCheck("Shasslly", "Root");
    }
    @Test
    public void checkWinTest(){
        assertEquals(true, game.checkIfGameOver(1,1));
    }
    @Test
    public void checkLoseTest(){
        assertEquals(true, game.checkIfGameOver(1,3));
    }
    @Test
    public void checkOngoingTest(){
        assertEquals(true, game.checkIfGameOver(1,0));
    }
    @Test
    public void checkPlayerTwoJoined() throws JSONException {
        assertEquals(true, game.checkIfPlayerTwoJoined(1));
    }
    @Test
    public void checkPlayerTwoDidNotJoin() throws JSONException {
        assertEquals(false, game.checkIfPlayerTwoJoined(2));
    }
    @Test
    public void findGameTest() throws JSONException {
        assertEquals(2, game.findCurrentOpenGameForUser("23"));
    }
    @Test
    public void doNotFindGameTest() throws JSONException {
        assertNotEquals(3, game.findCurrentOpenGameForUser("23"));
    }
    @Test
    public void checkForCurrentTurnTest() throws JSONException {
        assertEquals(true, game.checkForGameStatusChanges(4, "1"));
    }
    @Test
    public void checkForNotCurrentTurnTest() throws JSONException {
        assertEquals(false, game.checkForGameStatusChanges(4, "2"));
    }
    @Test
    public void checkStatsTest() throws JSONException {
        assertEquals("====================================\n" +
                "Root's Stats:\n" +
                " Wins:\t5\n" +
                " Loses:\t4\n" +
                " Ties:\t0", game.openStats( "1"));
    }
    @Test
    public void checkIfScoreboardPopulated() throws JSONException {
        assertTrue(game.populateScoreboard().size()>0);
    }
    @Test
    public void checkScoreboardDisplayTest() throws JSONException {
        ArrayList<ArrayList<String>> input = new ArrayList<ArrayList<String>>();
        input.add(new ArrayList<>());
        input.get(0).add("1");
        input.get(0).add("Test");
        input.get(0).add("5");
        input.get(0).add("3");
        input.get(0).add("1");
        assertEquals("====================================\n" +
                "Test's stats:\n" +
                "Games Won:5\n" +
                "Games Lost:3\n" +
                "Games Tied:1", game.openLeaderboard(input));
    }

}
