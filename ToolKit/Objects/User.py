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
    #Take in the object and convert it to what we need
    def __init__(self, FLUserJSON):
        #Check if we even got a user id
        try:
            #Setup our data
            self.Id               = FLUserJSON["id"]
            self.Username         = FLUserJSON["futureland_user"]
            self.CreatedAt        = FLUserJSON["createdAt"]

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
            "CreatedAt":        self.CreatedAt,

            #Functions
            "toJSON()" :  "Function, takes in nothing, returns JSON of object" 
        }

        return Object

