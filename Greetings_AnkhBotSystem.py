#---------------------------------------
# SHARED INFO:
#
# Script: Greetings
# Version: 1.4.4
# Description: Produces a greetings sound and message when somebody write first time in a session. It can reproduce another sound each time somebody writes again in chat. Sounds can still be disabled, to just greet textually for first message in chat.
# Change: Now you can set a different sentence for VIP, subriscribers and moderators.
# Services: Twitch, Mixer, Youtube
# Overlays: None
# Update Date: 2021/12/08
#
#---------------------------------------
# CHANGELOG:
#
# 2018/05/01 v1.0 - Initial Release
# 2018/05/01 v1.1 - Fixed compatibility with Mixer and Youtube
# 2018/10/05 v1.2 - Possibility to use a TSS Bot to read user name
# 2018/14/12 v1.2.1 - Now TTS nick "black list filter" is case-insensitive
# 2018/17/12 v1.2.2 - Now you can filter nicknames to not greet them neither textually (aka: your own bots)
# 2019/04/07 v1.3 - Now you can set a different sentence for VIP, subriscribers and moderators.
# 2021/12/06 v1.4.1 - Now you can filter nicknames to not check their messages and play no sound (aka: your own bots)
# 2021/12/06 v1.4.2 - Fixed youtube name showing
# 2021/12/06 v1.4.3 - Hidden the whole text to speach setting stuff, looking for a new working TTS server
# 2021/12/08 v1.4.4 - Hotfixes thank to Castorr91
#
#---------------------------------------


#---------------------------------------
# Import Libraries
#
# This is where you will import any necessary
# libraries that you require for your Python Script.
#
#---------------------------------------
import cgi, clr, codecs, json, os, sys, urllib
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")


#---------------------------------------
# [Required] Script Information
#
# These variables are required since they will be
# used to Display Errors in the PythonScriptErrorlog.txt
# located in the Logs folder / Scripts Tab under
# settings in case a script is not behaving properly.
# This is required for both StreamlabsSystems
# & StreamlabsParameters.
#
#---------------------------------------
ScriptName = "Greetings"
Website = "http://www.patcha.it"
Description = "It greets viewers first time they write on chat"
Creator = "Patcha"
Version = "1.4.4"


#---------------------------------------
# Set Variables
#
# Declare your Global Variables next.
# You will be able to use these within the Init,
# Tick and Execute functions. Once you want to edit
# a Global Variable you will need to use ex:
# global m_Response
#     m_Response = "This is the replacement"
#
#---------------------------------------
settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
CHUNK = 1024

class Settings:
    # Tries to load settings from file if given 
    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile = None):
        if settingsFile is not None and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig',mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig') 
        else: #set variables if no settings file
            self.BaseResponse = "Hi {0}! HeyGuys"
            self.VIPResponse = ""
            self.SubResponse = ""
            self.ModResponse = ""
            self.InfoResponse= "Ok, I got it!"
            self.DoNotGreet = ""
            self.GreetWave = "Hi.mp3"
            self.GreetVolume = "100"
            self.DoNotMsg = ""
            self.MsgWave = "Page_Turn.mp3"
            self.MsgVolume = "100"
        # TTSBot is deprecatd, so always keeps defaults
        self.TTSBot = False
        self.TTSBotVolume = "100"
        self.TTSBlackListedWords = "Nigger, Jew, Nazi, Nigga"
        self.TTSBotLanguage = "US English Female"
        self.TTSBotUser = ""
        self.TTSBotKey = ""
        self.TTSOverlayFont = "Roboto"
        self.TTSOverlayFontSize = "32"
        self.TTSOverlayFontColor = "rgba(65,65,244,1)"
        self.TTSOverlayBorderColor = "rgba(66,244,125,1)"
        self.TTSOverlayBackgroundColor = "rgba(255,255,255,1)"

    # Reload settings on save through UI
    def ReloadSettings(self, data):
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        with codecs.open(settingsFile,  encoding='utf-8-sig',mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig',mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return


#---------------------------------------
# [Required] Intialize Data (Only called on Load)
#
# Initialize anything that you want here.
# This function will only be called when
# the script is loaded.
#
#---------------------------------------
def Init():
    global MySettings
    global l_GreetedUsers
    global chanName
    global greet
    global newMsg
    global l_DontGreet
    global greetVol
    global l_DontMsg
    global newMsgVol
    global ttsBot
    global ttsBotKey
    global ttsBlackListedWords
    global ttsBotUser
    global oFontC
    global oFontBC
    global oFontBkgC

    MySettings = Settings(settingsFile)
    l_GreetedUsers = []

    chanName = Parent.GetChannelName().lower()

    greet = MySettings.GreetWave
    if not os.path.isfile(greet):
        if os.path.isfile("Services\Scripts\Greetings\\" + greet):
            greet = "Services\Scripts\Greetings\\" + greet
        else:
            greet = ""

    newMsg = MySettings.MsgWave
    if not os.path.isfile(newMsg):
        if os.path.isfile("Services\Scripts\Greetings\\" + newMsg):
            newMsg = "Services\Scripts\Greetings\\" + newMsg
        else:
            newMsg = ""

    l_DontGreet = MySettings.DoNotGreet.split(",")
    l_DontGreet = [x.strip().lower() for x in l_DontGreet]

    l_DontMsg = MySettings.DoNotMsg.split(",")
    l_DontMsg = [x.strip().lower() for x in l_DontMsg]

    try:
        greetVol = int(MySettings.GreetVolume)
    except ValueError:
        greetVol = 100

    try:
        newMsgVol = int(MySettings.MsgVolume)
    except ValueError:
        newMsgVol = 100

    ttsBot = MySettings.TTSBot
    ttsBotKey = MySettings.TTSBotKey
    if not ttsBotKey:
        ttsBot = False

    ttsBlackListedWords = ParseBlackListedWords(MySettings.TTSBlackListedWords)

    ttsBotUser = MySettings.TTSBotUser.strip()
    if not ttsBotUser:
        ttsBotUser = chanName

    oFontC = RgbaToHex(MySettings.TTSOverlayFontColor).replace("#", "")
    oFontBC = RgbaToHex(MySettings.TTSOverlayBorderColor).replace("#", "")
    oFontBkgC = RgbaToHex(MySettings.TTSOverlayBackgroundColor).replace("#", "")

    return


#---------------------------------------
# [Required] Execute Data / Process Messages
#
# The execute function will be called when there is
# a new chat message to be processed.
# If there are no new messages then this function
# will not be called. It also receives data which you can
# process to create your own commands, games, ...
# More info on the data type can be found below.
#
#---------------------------------------
def Execute(data):
    if data.IsChatMessage() and not data.IsFromDiscord():
        user = data.UserName.lower()

        if user != chanName:
            if user not in l_GreetedUsers and user not in l_DontGreet:
                l_GreetedUsers.append(user)
                if MySettings.ModResponse and Parent.HasPermission(data.User, "Moderator", ""):
                    Parent.SendStreamMessage(MySettings.ModResponse.format(user))
                elif MySettings.SubResponse and Parent.HasPermission(data.User, "Subscriber", ""):
                    Parent.SendStreamMessage(MySettings.SubResponse.format(user))
                elif MySettings.VIPResponse and Parent.HasPermission(data.User, "VIP Exclusive", ""):
                    Parent.SendStreamMessage(MySettings.VIPResponse.format(user))
                else:
                    Parent.SendStreamMessage(MySettings.BaseResponse.format(user))

                if not greet == "":
                    while not SoundPlayer(greet, greetVol):
                        continue
                    if ttsBot and not CheckIsBlackListedWord(user):
                        response = "https://warp.world/scripts/tts-message?streamer={0}&key={1}&viewer={2}&bar={3}&font={4}&sfont={5}&bfont={6}&gfont={7}&voice={8}&vol={9}&alert=false&message={10}".format(\
                            chanName, ttsBotKey, user, oFontBkgC, oFontC, MySettings.TTSOverlayFontSize, oFontBC, urllib.quote(cgi.escape(MySettings.TTSOverlayFont)), urllib.quote(cgi.escape(MySettings.TTSBotLanguage)), MySettings.TTSBotVolume, user)
                        response = Parent.GetRequest(response, {})

            else:
                if user not in l_DontMsg:
                    if not newMsg == "":
                        SoundPlayer(newMsg, newMsgVol)

    return


#---------------------------------------
# [Required] Tick Function
#
# This is the Tick function and will be executed
# every time the program progresses.
# As you can see there is no data variable here.
# So use this function when you don't require data,
# but want to do something while there is no data.
#
#---------------------------------------
def Tick():
    return


def UpdateSettings():
    with open(m_ConfigFile) as ConfigFile:
        MySettings.__dict__ = json.load(ConfigFile)
    return


def SetDefaults():
    global MySettings
    MySettings = Settings()
    MySettings.SaveSettings(settingsFile)
    return


def CheckIsBlackListedWord(user):
    for Words in ttsBlackListedWords:
        if all(Word.lower() in user for Word in Words):
            return True
    return False


def ParseBlackListedWords(Words):
    # i.e.: "Nigger, Jew, Nazi, Nigga, Mother+Fucker"
    Words = Words.split(",")
    Words = [x.strip().lower() for x in Words]
    Words = [x.split("+") for x in Words]
    return Words


def GenerateTTSBotUrl():
    response = json.loads(Parent.GetRequest("https://warp.world/scripts/tts-user?streamer=" + ttsBotUser, {}))
    if response["status"] == 200:
        return response["response"]
    else:
        return ""


def GenerateTTSBotKey():
    response = GenerateTTSBotUrl()
    if response:
        return response.split("/")[-2]
    else:
        return response


def GenerateAndWhisperTTSBotKey():
    response = GenerateTTSBotUrl()
    Parent.SendStreamMessage(str(response))
    if response:
        key = response.split("/")[-2]
        Parent.SendStreamMessage(ttsBotUser+" "+response+" "+key)
        Parent.SendStreamWhisper(chanName, "OBS Browser Source URL for {0}: {1} your key is {2}".format(ttsBotUser, response, key))
        os.startfile(response)


def RgbaToHex(rgba):
    # i.e. "rgba(66,244,125,1)"
    rgba = rgba.replace("rgba(", "")
    rgba = rgba.replace(")", "")

    strings = rgba.split(",")
    if len(strings) < 3:
        return "#000000"

    values = tuple(map(int, strings[0:3]))
    return '#%02x%02x%02x' % values


def SoundPlayer(path, vol):
    if not path == "" and not vol == 0:
        return Parent.PlaySound(path, vol)
    return True
