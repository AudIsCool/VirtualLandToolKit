#System imports
import os
import json 
import asyncio
import requests
import platform
from datetime import datetime

#Import our self madeobjects
import ToolKit.Objects as FLObjects


#For coloured printing on errors
from colorama import init
from termcolor import colored

"""
+---------------------------------------------------------------------+
|                         Created by Aud (:                           |
+---------------------------------------------------------------------+
|  + Started on 4-19-20                                               |
+---------------------------------------------------------------------+


+---------------------------------------------------------------------+
|                         OBJECT -> VLToolKit                         |
+---------------------------------------------------------------------+
|  This is your standard API Wrapper interface for the VirtualLand    |
|  Webapp.                                                            |
|                                                                     |
|  == Arguments ==                                                    |
|     Log (Bool)                                                      |
|       If set to true the program will log everything it does to     |
|       the console                                                   |                                                   |
|                                                                     |
+---------------------------------------------------------------------+
"""


#Build a wrapper class because fuck you that's why
class VLToolKit:
    #Constructor
    def __init__(self, *args, **kwargs):
        #Setup internal config
        self.LogMessages    = kwargs.get("Log") #If the user wants logging set it to true
        self.LoopDelay      = 10   #In seconds
        self.Token          = None
        self.User           = None
        self.LatestActivity = None
        
        #Init Logging
        self.InitLogging()

        #Verify Auth
        self.Log("__init__", "Attempting login...")
        Username = kwargs.get("Username")
        Password = kwargs.get("Password")

        #Send request and save it as possible
        LoginRequest = self.Login(Username, Password)

        #Save the user and token
        self.User  = LoginRequest[0]
        self.Token = LoginRequest[1]
        self.Log("__init__", "User {} saved, with token of {} length".format(self.User.Username, len(self.Token)))
        self.Log("__init__", "Initialized... Ready for tasking")


    """
    +---------------------------------------------------------------------+
    |                       == Useful Functions ==                        |
    +---------------------------------------------------------------------+
    |   These functions are useful for you! Call on them to do stuff.     |
    |                                                                     |
    |   Function List                                                     |
    |       Login(Username, Password)                                     |
    |                                                                     |
    +---------------------------------------------------------------------+
    """


    """
        Login(Username, Password)
            Logs you into the account that belongs to the username and 
            password given (they're both strings duh)

            Returns a 
    """
    def Login(self, Username, Password):
        #Build request
        self.Log("Login", "Building Login Request")
        LoginUrl = "https://futureland.tv/api/auth/login"
        LoginInfo = {
            "email" : Username,
            "password" : Password,
        }

        #Make login
        self.Log("Login", "Sending Login Request")
        LoginAttempt = requests.post(
            LoginUrl, 
            json=LoginInfo
        )

        #Deal with what came back
        LoginObject = LoginAttempt.json()
        self.Log("Login", "Login came back with code: {}".format(LoginAttempt.status_code))

        #Login was bad
        if(LoginAttempt.status_code != 200):
            self.Error("Login", "Login failed, without it we can't continue so we're killing. ")

            #If user fucked login
            if "ref" not in LoginObject:
                self.Error("Login", "[LOGINFAILTURE] SERVER SAID: {}".format(
                    LoginObject["message"]
                ))

            #If server had an internal error
            else:
                self.Error("Login", "[LOGINFAILTURE] SERVER SAID: {}, with ref ID of {}".format(
                    LoginObject["message"],
                    LoginObject["ref"]
                ))


            #Exit because without login it's difficult
            exit()


        #Login was fantastic lets get to work
        if(LoginAttempt.status_code == 200):
            #Tell the user, then create a user block and return it
            self.Log("Login", "Login was good, building user object and returning...")

            #Create a user
            User = FLObjects.Me(LoginObject["user"])

            #Return that and the function
            return (User, LoginObject["token"])


    """
        Start()
            Starts the toolkit's main loop
    """
    def Start(self):
        asyncio.run(self.Loop())


    """
        FetchActivities
            Fetches all activities in futureland
    """
    async def FetchActivities(self):
        #Get the data
        Data = requests.get("https://futureland.tv/api/activity")

        ActivityList = []

        for Activities in Data.json():
            ActivityList.append(FLObjects.Activity(Activities))

        return ActivityList


    """
    +---------------------------------------------------------------------+
    |                        == Event  Functions==                        |
    +---------------------------------------------------------------------+
    |   These functions are fired by the internal looping system          |
    |   But you can over write them to do your own thin                   |
    +---------------------------------------------------------------------+
    """

    
    """
        OnNewActivity(ToolKit.Objetcs.Activty)
            Is fired when the toolkit sees a new activty
    """
    async def OnNewAcvitity(self, Activity):
        if(Activity.Type == "user"):
            self.Log("OnNewAcvitity", "New {} posted with the ID {} from user {}".format(Activity.Type, Activity.Id, Activity.Data.Username))
            return

        else:
            self.Log("OnNewAcvitity", "New {} posted with the ID {} from user {}".format(Activity.Type, Activity.Id, Activity.Data.User.Username))


    """
    +---------------------------------------------------------------------+
    |                       == Unuseful Functions==                       |
    +---------------------------------------------------------------------+
    |   These functions are useless to you probably...                    |
    |    We use them internally though soooooo....                        |
    +---------------------------------------------------------------------+
    """

    """
        Loop()
            The tool kit's main loop, looks for activties and displays new ones
    """
    async def Loop(self):
        while True:
            ActitivtyCheck = await self.CheckForNewActivties()

            if(ActitivtyCheck != False):
                await self.OnNewAcvitity(ActitivtyCheck)

            await asyncio.sleep(self.LoopDelay)
        

    """
        CheckForActivities()
            Called by Loop, returns the latest activty if there's a new one
            Returns false if there's nothing
    """
    async def CheckForNewActivties(self):
        #Fetch latest activity
        Activity = await self.FetchLatestActivity()
        
        #If there's a new activity save it then return it
        if Activity.Id != self.LatestActivity:
            self.LatestActivity = Activity.Id
            return Activity

        #If there isn't, return false and carry on
        else:
            return False



    """
        FetchLatestActivity
            Fetches newest actvity 
    """
    async def FetchLatestActivity(self):
        #There's no better way to do this atm, I can only fetch ALL activities
        Activities = await self.FetchActivities()
        return Activities[0]
        

    """
        InitLogging()
            Clears screens and sets up coloured printing
    """
    def InitLogging(self):
        #Start up pretty colours
        init()

        #Clear teh console
        if(self.LogMessages == True):
            #If on windows
            if(platform.system() == "Windows"):
                os.system("cls")
            
            #if not
            else:
                os.system("clear")


    """
        Log(Function, Message)
            Takes in the function name (string) and message (string)
            the function wants to say and pretty prints it into 
            the console
    """
    def Log(self, Function, Message):
        #If the user said we could log, do some fancy loggin
        if(self.LogMessages):
            CurrentDate = datetime.now().date()
            CurrentTime = datetime.now().time()

            Date = "{}/{}/{}".format(CurrentDate.month, CurrentDate.day, CurrentDate.year)
            Time = "{}:{}:{}".format(CurrentTime.hour, CurrentTime.minute, CurrentTime.second)

            LogDate = "{} - {}".format(Date, Time)

            LogMessage = "[{}][{}()][FuturelandToolKit]: {}".format(LogDate, colored(Function, "green"), colored(Message, "cyan"))

            print(LogMessage)

    """
        Error(Function, ErrorMessage)
            Takes in the function name (string) and error message
            (string) the function wants to say and pretty 
            prints it into the console
    """
    def Error(self, Function, ErrorMessage):
        CurrentDate = datetime.now().date()
        CurrentTime = datetime.now().time()

        Date = "{}/{}/{}".format(CurrentDate.month, CurrentDate.day, CurrentDate.year)
        Time = "{}:{}:{}".format(CurrentTime.hour, CurrentTime.minute, CurrentTime.second)

        LogDate = "{} - {}".format(Date, Time)

        LogMessage = "[{}][{}()][FuturelandToolKit]: {}".format(LogDate, Function, ErrorMessage)

        print(colored(LogMessage, "red"))