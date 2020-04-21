"""
+---------------------------------------------------------------------+
|                         Created by Aud (:                           |
+---------------------------------------------------------------------+
|  + Started on 4-19-20                                               |
+---------------------------------------------------------------------+


+---------------------------------------------------------------------+
|                        OBJECT -> Comment                            |
+---------------------------------------------------------------------+
|  This Object takes in the Comment json object gotten from           |
|  Futureland and convert it to a python object for usage later.      |
|  It's also easier to work with since we can just do OBJ.ATTRIBUTE   |
|  instead of OBJ["ATTRIBUTE"]                                        |
+---------------------------------------------------------------------+
"""
#System imports
import json

#Import our self madeobjects
import ToolKit.Objects as FLObjects

class Comment:
    #Take in the object and convert it to what we need
    def __init__(self, FLCommentJSON):
        #Check if we even got the right data 
        try:
            #Setup our data
            self.Id        = FLCommentJSON["id"]
            self.Text      = FLCommentJSON["value"]
            self.CreatedAt = FLCommentJSON["createdAt"]
            self.User      = FLObjects.User(FLCommentJSON["user"])
            self.OutputId  = FLCommentJSON["output"]["id"] #We're not doing the whole object because the comment doesn't conatin the note, and calling our object would be suicide without the note

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
            "Text"      : self.Text,
            "CreatedAt" : self.CreatedAt,
            "User"      : self.User.toJSON(),
            "Output"    : self.OutputId,

            #Functions
            "toJSON()" :  "Function, takes in nothing, returns JSON of object" 
        }

        return Object

