#System imports
import os

#Bring in the env data
from dotenv import load_dotenv
load_dotenv()

#Import our tool kit
import ToolKit

#Create tool kit
OurToolkit = ToolKit.VLToolKit(
    Username = os.getenv("FLEMAIL"),
    Password = os.getenv("FLPASSWORD"),
    Log = True #Just some cool logs
)

print("Test print of user")
print(OurToolkit.User)