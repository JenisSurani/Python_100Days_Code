#win32com.client is a Python module that allows you to use Windows COM objects.
import win32com.client as wincl



# SAPI (Speech API) is a built-in Windows speech synthesis system.
# wincl.Dispatch("SAPI.SpVoice") creates an instance of the SAPI.SpVoice object, which is responsible for text-to-speech conversion.
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices() # retrieves all available voices installed on your system. vcs stores a list of voice objects.

#selects the second available voice (because indexing starts at 0).
speaker_number = 2  # can select from 0,1,2 as you have 3 voice models in your system


print(f"The Speaker is: {vcs.Item(speaker_number).GetAttribute("Name")}")# speaker name

spk.Voice #returns the currently selected voice object.
spk.rate=-20
spk.Volume=100 # setting up the properties

spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
spk.Speak("Hi Jenis")
spk.rate=1
spk.Speak("Hello Jenish surani, Keep it up")

# __________________

# speaker_number = 1  # can select from 0,1,2 as you have 3 voice models in your system
# print(f"The Speaker is: {vcs.Item(speaker_number).GetAttribute("Name")}")# speaker name

# spk.Voice # returns the currently selected voice object.
# spk.rate= 1
# spk.Volume=100 # setting up the properties
# spk.SetVoice(vcs.Item(speaker_number)) # set voice

# print("\nSetting up the voice model,Please Wait..\n")
# spk.Speak("Hello Mike check!!") 
# def textToSpeech(text:str):
    
#     print(f"Shoutout to {text}")
#     spk.Speak(f"Shoutout to {text}")
    

# list=["Rahul","Keshav","Jenish","Shubham","Shreya","Mansi","Dhoom","Kachraseth"]

# for person in list:
#     textToSpeech(person)
    
    











# Author : Jenis Surani
# Topic  : None (Shoutouts)
# Date   : 24/02/2025