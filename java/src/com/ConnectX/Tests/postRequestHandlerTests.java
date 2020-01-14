package com.ConnectX.Tests;
import com.ConnectX.RestAPI.PostRequestHandler;
import org.junit.Test;


import static org.junit.Assert.*;

public class postRequestHandlerTests {
    public PostRequestHandler handler = new PostRequestHandler();
    @Test
    public void testUserInsert(){
        String username = "Test";
        String password = "Test";
        assertEquals(true, handler.insertUser(username, password));
    }
    @Test
    public void testExistingUserInput(){
        String username = "Shally";
        String password = "Root";
        assertEquals(false, handler.insertUser(username, password));
    }
    @Test
    public void testCreateGame(){
        String uid = "1";
        assertEquals(true, handler.createGame(uid));
    }
    @Test
    public void testUnableToCreateGame(){
        String uid = "-2";
        assertEquals(false, handler.createGame(uid));
    }
    @Test
    public void testUnableToJoinGame(){
        String uid = "-2";
        int gameID =-2;
        assertEquals(false, handler.joinGame(uid, gameID));
    }
    @Test
    public void testUnableToMakeMove(){
        String uid = "-2";
        int gameID = -2;
        int selection = 4;
        assertEquals(false, handler.makeMove(selection,gameID, uid));
    }
    @Test
    public void testMakeMove(){
        String uid = "1";
        int gameID = 2;
        int selection = 4;
        assertEquals(true, handler.makeMove(selection, gameID, uid));
    }

}
