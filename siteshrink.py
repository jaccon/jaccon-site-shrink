
import os
import time
ts = str(time.time())

# setup
version = "0.2.1.2023"
command1 = "wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --no-parent "

print ("☠️☠️☠️ Jaccon Site Shrink ☠️☠️☠️ " + version)
print ("")
print ("HOW TO USE")
print ("This script builded to help a developers to understand how to clone html websites. ")
print ("Using with moderation... ")
print ("")
print ("")

ask1 = input('1️⃣ - Type the website url: ')
print ("")

ask2 = input('2️⃣ - Type the directory path to save the downloads or blank to save in shrink folder: ')
print ("")

if ask2 == "":
  ask2 = ("./shrink-"+ts)
  print ("Save files to:" + ask2)

print ("Shrink setup information: ")
print("Shrink the url: " + ask1)
print("Save the files to directory: " + ask2)
print ("")
print ("")

aks3 = input('3️⃣ - Confirm the information and type Y to continue: ')

if(aks3 == "Y"):
  print ("")
  print ("Start download.... please waiting to finish")
  print("")
  executeCommand = command1 + " -P " + ask2 + " " + ask1
  print(executeCommand)
  os.system(executeCommand)
  
else:
  time.sleep(.04)
  print("")
  print("")
  print(" 💩 💩 💩 Download is canceled, check the parameters and try again !!!")
