"""
+---------------------------------------------------------------------+
|                         Created by Aud (:                           |
+---------------------------------------------------------------------+
|  + Started on 4-19-20                                               |
+---------------------------------------------------------------------+


+---------------------------------------------------------------------+
|                           OBJECT -> User                            |
+---------------------------------------------------------------------+
|  This Object takes in the User json object gotten from Futureland   |
|  and convert it to a python object for usage later. It's also       |
|  easier to work with since we can just do OBJ.ATTRIBUTE instead of  | 
|  OBJ["ATTRIBUTE"]                                                   |
+---------------------------------------------------------------------+
"""

#System imports
import json


class User:
    #Take in the user object and convert it to what we need
    def __init__(self, FLUserJSON):
        #Check if we even got a user id
        try:
            #Setup our data
            self.Id               = FLUserJSON["id"]
            self.Username         = FLUserJSON["futureland_user"]
            self.Email            = FLUserJSON["email"]
            self.Plan             = FLUserJSON["plan"]
            self.SupportPack      = FLUserJSON["support_pack"]
            self.ProfilePic       = FLUserJSON["original_avatar_link"]
            self.SlackUserId      = FLUserJSON["slack_user_id"]
            self.Anonymous        = FLUserJSON["anonymous"]
            self.TwitterUsername  = FLUserJSON["twitterUsername"]
            self.LastVideoUpdate  = FLUserJSON["lastVideoUpdate"]
            self.RegistrationType = FLUserJSON["registrationType"]
            self.Timezone         = FLUserJSON["timezone"]
            self.CreatedAt        = FLUserJSON["createdAt"]
            self.UpdatedAt        = FLUserJSON["updatedAt"]
            self.Projects         = [] #TODO: Create an object for projects

        #If we didn't get one of these the JSON is bad and toss error
        except:
            raise ValueError("JSON given was incorrectly formatted and we couldn't build a User Object out of it")
        


    #For printing our object
    def __str__(self):
        #Build the pretty print from JSON 
        return json.dumps(self.toJSON(), indent=4, sort_keys=False)


    #Pretty print our user object
    def toJSON(self):
        #Rebuild the object so we can use JSON pretty print
        Object = {
            #Attributes
            "Id":               self.Id,
            "Username":         self.Username,
            "Email":            self.Email,
            "Plan":             self.Plan,
            "SupportPack":      self.SupportPack,
            "ProfilePic":       self.ProfilePic,
            "SlackUserId":      self.SlackUserId,
            "Anonymous":        self.Anonymous,
            "TwitterUsername":  self.TwitterUsername,
            "LastVideoUpdate":  self.LastVideoUpdate,
            "RegistrationType": self.RegistrationType,
            "Timezone":         self.Timezone,
            "CreatedAt":        self.CreatedAt,
            "UpdatedAt":        self.UpdatedAt,
            "Projects":         self.Projects,

            #Functions
            "toJSON()" :  "Function, takes in nothing, returns JSON of object" 
        }

        return Object

