"""
+---------------------------------------------------------------------+
|                         Created by Aud (:                           |
+---------------------------------------------------------------------+
|  + Started on 4-19-20                                               |
+---------------------------------------------------------------------+


+---------------------------------------------------------------------+
|                        OBJECT -> Project                            |
+---------------------------------------------------------------------+
|  This Object takes in the Project json object gotten from           |
|  Futureland and convert it to a python object for usage later.      |
|  It's also easier to work with since we can just do OBJ.ATTRIBUTE   |
|  instead of OBJ["ATTRIBUTE"]                                        |
+---------------------------------------------------------------------+
"""
#System imports
import json

#Self imports
import ToolKit.Objects as FLObjects


class Project:
    #Take in the     object and convert it to what we need
    def __init__(self, FLProjectJSON):
        #Check if we even got the right data
        try:
            #Setup our data
            self.Id        = FLProjectJSON["id"]
            self.Slug      = FLProjectJSON["slug"]
            self.Title     = FLProjectJSON["title"]
            self.CreatedAt = FLProjectJSON["createdAt"]
            self.User      = "Check parent" #Short fix for now

            #If a user creates a project I need to catch the user tagged to it
            if "user" in FLProjectJSON:
                self.User = FLObjects.User(FLProjectJSON["user"])

        #If we didn't get one of these the JSON is bad and toss error
        except:
            raise ValueError("JSON given was incorrectly formatted and we couldn't build a Project Object out of it")
        


    #For printing our object
    def __str__(self):
        #Build the pretty print from JSON 
        return json.dumps(self.toJSON(), indent=4, sort_keys=False)


    #Pretty print our user object
    def toJSON(self):
        #Rebuild the object so we can use JSON pretty print
        Object = {
            #Attributes
            "Id"        : self.Id,
            "Slug"      : self.Slug,
            "Title"     : self.Title,
            "CreatedAt" : self.CreatedAt,

            #Functions
            "toJSON()" :  "Function, takes in nothing, returns JSON of object" 
        }

        return Object

