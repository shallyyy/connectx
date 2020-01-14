package com.ConnectX.Tests;
import com.ConnectX.RestAPI.GetRequestHandler;
import org.json.JSONException;
import org.junit.Test;


import static org.junit.Assert.*;

import static org.junit.Assert.assertEquals;

public class getHandlerRequestsTests {
    GetRequestHandler handler = new GetRequestHandler();

    @Test
    public void getUserWithName() throws JSONException {
        String [] results = handler.getUserWithName("Shally", "Root");
        assertEquals("1", results[0] );
        assertEquals("Shally", results[2] );
    }

    @Test (expected = NullPointerException.class)
    public void getWrongUserWithName() throws JSONException {
        String [] results = handler.getUserWithName("Shalsaly", "Root");
        assertEquals(null, results[0] );
        assertEquals(null, results[2] );
    }

    @Test
    public void getGameInfoTest() throws JSONException {
        assertTrue(handler.getGameInfo(1).length()>0);
    }

    @Test (expected = JSONException.class)
    public void getWrongGameInfoTest() throws JSONException {
        assertTrue(handler.getGameInfo(-1).length()==0);
    }
    @Test
    public void getgamesTest() throws JSONException {
        assertTrue(handler.getGames().length()>0);
    }
    @Test
    public void getAllUsersTest() throws JSONException {
        assertTrue(handler.getALlUsers().length()>0);
    }
    @Test
    public void getOpenGames() throws JSONException {
        assertTrue(handler.getOpenUserGame("1").length()>0);
    }
    @Test
    public void getBoard() throws JSONException {
        assertTrue(handler.getBoard(1).length()>0);
    }
}
