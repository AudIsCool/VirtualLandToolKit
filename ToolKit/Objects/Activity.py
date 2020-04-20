"""
+---------------------------------------------------------------------+
|                         Created by Aud (:                           |
+---------------------------------------------------------------------+
|  + Started on 4-19-20                                               |
+---------------------------------------------------------------------+


+---------------------------------------------------------------------+
|                        OBJECT -> Activity                           |
+---------------------------------------------------------------------+
|  This Object takes in the Activity json object gotten from          |
|  Futureland and convert it to a python object for usage later.      |
|  It's also easier to work with since we can just do OBJ.ATTRIBUTE   |
|  instead of OBJ["ATTRIBUTE"]                                        |
+---------------------------------------------------------------------+
"""

#Self imports
import ToolKit.Objects as FLObjects

#System imports
import json


class Activity:
    #Take in the object and convert it to what we need
    def __init__(self, FLActivityJSON):
        #Check if we even got actvity data
        try:
            #Break down key into ID and type
            self.Key = FLActivityJSON["key"]
            KeyData  = self.Key.split("-")
            
            #Actually refine data
            self.Id      = KeyData[1]
            self.Type    = KeyData[0]
            self.Subtype = FLActivityJSON["type"]
            self.Date    = FLActivityJSON["date"]

            #Setup the data types
            if(self.Type == "output"):
                self.Data = FLObjects.Output(FLActivityJSON["output"])

            elif(self.Type == "comment"):
                self.Data = FLObjects.Comment(FLActivityJSON["comment"])

            elif(self.Type == "user"):
                self.Data = FLObjects.User(FLActivityJSON["user"])

            elif(self.Type == "project"):
                self.Data = FLObjects.Project(FLActivityJSON["project"])

        #If we didn't get one of these the JSON is bad and toss error
        except:
            raise ValueError("JSON given was incorrectly formatted and we couldn't build a Activity Object out of it")
        


    #For printing our object
    def __str__(self):
        #Build the pretty print from JSON 
        return json.dumps(self.toJSON(), indent=4, sort_keys=False)


    #Pretty print our user object
    def toJSON(self):
        #Rebuild the object so we can use JSON pretty print
        Object = {
            #Attributes
            "Id":      self.Id,
            "Type":    self.Type,
            "Subtype": self.Subtype,
            "Date":    self.Date,
            "Type":    self.Type,
            "Data":    self.Data.toJSON(),

            #Functions
            "toJSON()" :  "Function, takes in nothing, returns JSON of object" 
        }

        return Object

