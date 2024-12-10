# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SHARED INFO:
#
# Script: Greetings
# Version: 2.1
# Description: Greet new viewers by playing a sound and/or a text
#                   message when they write in chat for the first time
#                   each session.
#              Can also be used to play sounds when a user sends
#                   additional messages.
# Change: Fixed blocking no default for "Character series to swap"
#           option when options were still not saved
#         Fixed empty "Users not to greet + Blacklisted words" option
#           was resulting like not greeting anybody at all
# Services: Twitch, Youtube
# Overlays: None
# Update Date: 2023/10/21
#
# Note: if you're updating for a previous 1.x version, new versions 2.x
#       have no code retrocompatibility at all, so I suggest to:
# 1. note all settings from old version
# 2. completely delete old version
# 3. put new version
# 4. apply settings noted from old version
#
# Note: if you're updating from a previous 2.x version,
#       you may have to delete old "lib" directory before update,
#       because all new releases use new lib versions.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHANGELOG:
#
# 2018/05/01 v1.0 - First public release
# 2018/05/01 v1.1 - Fixed compatibility with Mixer and Youtube
# 2018/10/05 v1.2 - Possibility to use a TSS Bot to read user name
# 2018/14/12 v1.2.1 - Now TTS "blacklist filter" is now case-insensitive
# 2018/17/12 v1.2.2 - Now you can filter nicknames, to not greet them
#                       neither textually (aka: your own bots)
# 2019/04/07 v1.3 - Now you can set a different sentence for VIPs,
#                       subriscribers and moderators
# 2021/12/06 v1.4.3 -
#       Now you can filter nicknames to not check their messages
#           and play no sound (aka: your own bots)
#       Fixed youtube name showing
#       Hidden the whole old TTS setting stuff,
#           looking for a new working TTS server
# 2021/12/08 v1.4.4 - Hotfixes, thanks to Castorr91
# 2022/02/09 v1.5 - Now you can filter message by starting characters
#                       or words (i.e.: ! for chat commands)
# 2022/02/16 v1.5.1 - Fixed typo on "Ignore messages starting by"
#                       splitter character (was comma, have to be space)
# 2022/08/05 v1.5.2 - Fixed volume setting for sounds
# 2023/07/29 v2.0 -
#       TTS Functions restored, enhanced and tweaked
#           (original code from LuisSanchezDev's The NewTTS script,
#               recently reworked by me as The ReNewTTS script)
#       Settings section with fields to totally customize greetings
#          details per specific users
#       Minor fixes and tweaks
#       Adopting file organization in subfolders
#       NOTE: There's no retrocompatibility with old 1.x versions
#           You'll have to delete old versions first
#           (while noting old settings)
# 2023/10/21 v2.1 -
#       Fixed blocking no default for "Character series to swap" option
#           when options were still not saved
#       Fixed empty "Users not to greet + Blacklisted words" option was
#           resulting like not greeting anybody at all
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Import Libraries
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import clr, os, sys, time, re
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

# Add script's folder to path to be able to find the other modules
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from tts_media_utils_106 import MediaDownloader
from settings_utils_103 import Settings
from scripts_utils_101 import *


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   [Required] Script Information
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ScriptName = "Greetings"
Website = "https://www.patcha.it"
Description = "It greets viewers first time they write on chat and can also"\
                " play sound for additional messages"
Creator = "Patcha"
Version = "2.1"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Define Global Variables
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SCRIPT_NAME = ScriptName.replace(" ", "")
DIRECTORY = os.path.dirname(__file__)
SETTINGS_PATH = os.path.join(DIRECTORY, "Settings")
SETTINGS_FILE = os.path.join(SETTINGS_PATH, "settings.json")
DEFAULTS = {}
CHUNK = 1024

# TTS vars
global LIB_PATH, MEDIA_DWNL, DWNL_SET
LIB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
MEDIA_DWNL = None
DWNL_SET = {}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   [Required] Initialize Data (Only called on load)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Init():
    global SETTINGS, DIRECTORY
    global DEFAULTS, TIMEOUT
    global DWNL_SET, LIB_PATH, MEDIA_DWNL
    global CHANNEL_NAME
    global GREETED_LIST, ALIAS_DICT
    global NO_GREET_LIST, NO_MSG_LIST
    global NO_START_GREET, NO_START_MSG
    global AUDIO_PATH
    global GREET_AUDIO, GREET_VOLUME
    global NEW_MSG_AUDIO, NEW_MSG_VOLUME
    global CUSTOM_GREET, CUSTOM_AUDIO
    global TTS_CUSTOM_GREET, TTS_CUSTOM_USER

    # Create Settings Directory
    if not os.path.exists(SETTINGS_PATH):
        os.makedirs(SETTINGS_PATH)

    TIMEOUT = 30
    DEFAULTS = {
        "script": SCRIPT_NAME,
        "base_response": "Hi {0}! HeyGuys",
        "vip_response": "",
        "sub_response": "",
        "mod_response": "",
        "tts_alias_list": "",
        "do_not_greet": "",
        "greet_wave": "Hi.mp3",
        "greet_volume": 100,
        "no_start_greet": "",
        "msg_wave": "Page_Turn.mp3",
        "no_start_msg": "",
        "do_not_msg": "",
        "msg_volume": 100,
        "custom_greet": "",
        "custom_audio": "",
        "custom_greet_tts" : "",
        "custom_user": "",
        "tts_bot_on": False,
        "tts_lang": "English (US) [en-US]",
        "tts_volume_on": True,
        "tts_volume": 90,
        "tts_pitch_on": True,
        "tts_pitch": 100,
        "tts_speed_on": True,
        "tts_speed": 100,
        "tts_replaces": "_",
        "tts_case": "",
        "tts_chars_swapping": "",
        "tts_clean_repeated_letters": True,
        "tts_confirm": "Configuration updated successfully",
        "tts_params": "",
        "tts_webservice": "https://translate.google.com/translate_tts?ie="\
                            "UTF-8&tl={1}&client=tw-ob&q={0}",
        "tts_audio_format" : ".mp3",
    }

    SETTINGS = Settings(SETTINGS_FILE, DEFAULTS)
    GREETED_LIST = []

    cache_folder = os.path.join(LIB_PATH, "cache")
    loop_start = time.time()
    while True:
        try:
            if (time.time() - loop_start) > TIMEOUT:
                break
            if os.path.isdir(cache_folder):
                run_cmd('RMDIR /Q/S "{0}"'.format(cache_folder))
            os.mkdir(cache_folder)
            break
        except:
            continue

   # TTS settings: length and timeout are in seconds
    DWNL_SET = {
        "script": SCRIPT_NAME,
        "lang": SETTINGS.tts_lang,
        "volume_on": SETTINGS.tts_volume_on,
        "pitch_on": SETTINGS.tts_pitch_on,
        "speed_on": SETTINGS.tts_speed_on,
        "volume": SETTINGS.tts_volume / 100.0,
        "pitch": SETTINGS.tts_pitch / 100.0,
        "speed": SETTINGS.tts_speed / 100.0,
        "length": 26,
        "timeout": TIMEOUT,
        "keep": False,
        "case": SETTINGS.tts_case,
        "clean_rep_lett": False,
        "clean_rep_word": False,
        "max_rep_word": 3,
        "alias_on" : False,
        "alias_list": SETTINGS.tts_alias_list,
        "chars_swapping": SETTINGS.tts_chars_swapping,
        "clean_urls": False,
        "replace_urls": "",
        "replaces": SETTINGS.tts_replaces,
        "emote_name_upper": True,
        "emote_prefix": "",
        "cut_max_chars": True,
        "max_chars": 200,
        "params": SETTINGS.tts_params,
        "webservice": SETTINGS.tts_webservice,
        "audio_format" : SETTINGS.tts_audio_format,
        "_path": LIB_PATH,
        "_cache": cache_folder,
    }

    # Save on TTS bot resources and threads, if bot is not enabled
    if SETTINGS.tts_bot_on:
        MEDIA_DWNL = MediaDownloader(DWNL_SET)

    CHANNEL_NAME = Parent.GetChannelName()
    if isinstance(CHANNEL_NAME, str):
        CHANNEL_NAME = CHANNEL_NAME.lower()

    AUDIO_PATH = os.path.join(DIRECTORY, "audio")

    GREET_AUDIO = is_existing_file_path(SETTINGS.greet_wave, AUDIO_PATH)
    NEW_MSG_AUDIO = is_existing_file_path(SETTINGS.msg_wave, AUDIO_PATH)

    ALIAS_DICT = parse_alias_list(SETTINGS.tts_alias_list, True)
    NO_GREET_LIST = parse_black_listed_words(SETTINGS.do_not_greet)

    NO_MSG_LIST = SETTINGS.do_not_msg.split(",")
    NO_MSG_LIST = [x.strip().lower() for x in NO_MSG_LIST]

    if SETTINGS.no_start_greet:
        NO_START_GREET = SETTINGS.no_start_greet.split(" ")
        NO_START_GREET = [x.strip().lower() for x in NO_START_GREET]
        NO_START_GREET = tuple(NO_START_GREET)
    else:
        NO_START_GREET = tuple()

    if SETTINGS.no_start_msg:
        NO_START_MSG = SETTINGS.no_start_msg.split(" ")
        NO_START_MSG = [x.strip().lower() for x in NO_START_MSG]
        NO_START_MSG = tuple(NO_START_MSG)
    else:
        NO_START_MSG = tuple()

    GREET_VOLUME = from_zero_to_one_dot_zero(SETTINGS.greet_volume, 100.0)

    NEW_MSG_VOLUME = from_zero_to_one_dot_zero(SETTINGS.msg_volume, 100.0)

    CUSTOM_GREET = parse_split_by_quotes(SETTINGS.custom_greet)
    TTS_CUSTOM_GREET = parse_split_by_quotes(SETTINGS.custom_greet_tts)

    CUSTOM_AUDIO = parse_split_by_quotes(SETTINGS.custom_audio)
    CUSTOM_AUDIO = is_existing_file_path_list(CUSTOM_AUDIO, AUDIO_PATH)

    TTS_CUSTOM_USER = SETTINGS.custom_user.lower()
    TTS_CUSTOM_USER = fix_parsed_indexes_in_lists(
                        parse_quote_colon_sets(TTS_CUSTOM_USER))
    TTS_CUSTOM_USER = flols_tdols(TTS_CUSTOM_USER)

    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   [Required] Execute Data / Process messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Execute(data):
    if data.IsChatMessage() and not data.IsFromDiscord():
        user = data.UserName.lower()
        msg = data.GetParam(0).lower()

        if user != CHANNEL_NAME:
            # Check if current user has an alias in ALIAS_DICT
            name = user if not user in ALIAS_DICT else ALIAS_DICT[user]

            # Blacklist check is on the alias, if any
            if user not in GREETED_LIST and \
                    not is_black_listed_word(name, NO_GREET_LIST) and \
                    (not NO_START_GREET or not msg.startswith(NO_START_GREET)):

                # Custom configs check
                customs = [-1,-1,-1]
                if user in TTS_CUSTOM_USER:
                    customs = TTS_CUSTOM_USER[user]

                # Custom message
                if customs and customs[0] > -1 and  \
                        CUSTOM_GREET and len(CUSTOM_GREET) > customs[0]:
                    response = CUSTOM_GREET[customs[0]]

                # Messages by role
                elif SETTINGS.mod_response and \
                        Parent.HasPermission(data.User, "Moderator", ""):
                    response = SETTINGS.mod_response
                elif SETTINGS.sub_response and \
                        Parent.HasPermission(data.User, "Subscriber", ""):
                    response = SETTINGS.sub_response
                elif SETTINGS.vip_response and \
                        Parent.HasPermission(data.User, "VIP Exclusive", ""):
                    response = SETTINGS.vip_response

                # Base message, default
                else:
                    response = SETTINGS.base_response

                # Play message
                if response:
                    Parent.SendStreamMessage(response.format(name, user))


                # Base sound, default
                response_audio = GREET_AUDIO

                # Custom sound
                if len(customs) > 1 and customs[1] > -1 and \
                        CUSTOM_AUDIO and len(CUSTOM_AUDIO) > customs[1]:
                    response_audio = CUSTOM_AUDIO[customs[1]]

                # Play sound
                if response_audio:
                    while not audio_player(
                            response_audio.format(name, user), GREET_VOLUME):
                        continue


                # Base TTS, default
                if SETTINGS.tts_bot_on:
                    tts_response = name

                    # Custom TTS
                    if len(customs) > 2 and customs[2] > -1 and \
                            TTS_CUSTOM_GREET and \
                            len(TTS_CUSTOM_GREET) > customs[2]:
                        tts_response = TTS_CUSTOM_GREET[customs[2]]

                    # Play TTS
                    if tts_response:
                        MEDIA_DWNL.append_and_play(
                            tts_response.format(name, user))

                GREETED_LIST.append(user)


            # for new messages sound, checks are on username,
            #   not on the alias
            else:
                if user not in NO_MSG_LIST and \
                        (not NO_START_MSG or not msg.startswith(NO_START_MSG)):
                    if NEW_MSG_AUDIO:
                        audio_player(NEW_MSG_AUDIO, NEW_MSG_VOLUME)


    return

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   [Required] Tick method (Gets called during every iteration even
#               when there is no incoming data)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Tick():
    return

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   [Optional] Reload Settings (Called when a user clicks the
#               Save Settings button in the Chatbot UI)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ReloadSettings(jsonData):
    global MEDIA_DWNL
    Unload()
    Init()
    if SETTINGS.tts_bot_on and MEDIA_DWNL and SETTINGS.tts_confirm:
        MEDIA_DWNL.append_and_play(SETTINGS.tts_confirm)
    return

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   [Optional] Unload (Called when a user reloads their scripts or
#               closes the bot / cleanup stuff)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Unload():
    global MEDIA_DWNL
    if MEDIA_DWNL:
        MEDIA_DWNL.close()
        del MEDIA_DWNL
    return


def parse_black_listed_words(words):
    words = words.split(",")
    words = [x.strip().lower() for x in words]
    words = [x.split("+") for x in words]
    return words


def is_black_listed_word(name, list):
    if (name and list and any(list)):
        comp = name.lower()
        for words in list:
            if (words and any(word.strip() for word in words)):
                if all(word.lower() in comp for word in words):
                    return True
    return False


def fix_parsed_indexes_in_lists(list, how = -1, prevent_negative = False):
    if list and isinstance(how, int):
        list_type = type([])
        delete_list = []

        for i, x in enumerate(list):
            if type(x) == list_type:
                list[i] = fix_parsed_indexes_in_lists(x, how, prevent_negative)
            else:
                try:
                    list[i] = int(x) + how
                    if prevent_negative and list[i] < 0:
                        delete_list.append(i)
                except:
                    pass #not number

        for d in sorted(delete_list, reverse=True):
            del list[d]

    return list


def parse_quote_colon_sets(text_to_split):
    list = parse_split_by_quotes(text_to_split)
    list = [parse_split_by_char(x, ":") for x in list]
    return list


def parse_split_by_quotes(text_to_split):
    return parse_split_by_char(text_to_split, "\"", True)


def parse_split_by_char(text_to_split, char, doubled = False):
    list = [text_to_split]
    try:
        if text_to_split and char:
            text_to_split = strip_one(text_to_split, char)
            if doubled:
                char += char
            list = text_to_split.split(char)
    except:
        pass
    return list


# From list of lists > to dictionary of lists
def flols_tdols(list_of_lists):
    dict_of_lists = {}

    if list_of_lists:
        for item in list_of_lists:
            if item:
                dict_of_lists[item[0]] = []
                for i in item[1:]:
                    dict_of_lists[item[0]].append(i)

    return dict_of_lists


def strip_one(text, char = ""):
    if text:
        if text.startswith(char):
            text = text[1:]
        if text.endswith(char):
            text = text[:-1]
    return text


def is_existing_file_path(path, folder = ""):
    if not os.path.isfile(path):
        sub = os.path.join(folder, path)
        local = os.path.join(DIRECTORY, path)

        if folder and os.path.isfile(sub):
            return sub
        elif os.path.isfile(local):
            return local
        else:
            return None

    return path


def is_existing_file_path_list(list, folder = ""):
    if list:
        for i, s in enumerate(list):
            list[i] = is_existing_file_path(s, folder)
    return list


def audio_player(path, vol):
    if path and vol:
        return Parent.PlaySound(path, vol)
    return True
