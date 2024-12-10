[![development status | 7 - Inactive](https://img.shields.io/badge/development_status-7_--_Inactive-orange)](https://pypi.org/classifiers/)
[![code style: pep-008](https://img.shields.io/badge/code_style-pep--0008-FFF8FF)](https://peps.python.org/pep-0008/)
![license](https://img.shields.io/badge/license-MIT-green)
![release](https://img.shields.io/github/v/release/PatchaIT/greetings)
[![next](https://img.shields.io/badge/next-v2.0.1-yellow)](https://github.com/PatchaIT/TheRenewTTS/tree/greetings_v2.1.0)
___
<h1 align="center">
Greetings
</h1>
<p align="center">
<sup>
(On your Streamlabs Chatbot) Greet new viewers by playing a sound and/or a
  text message when they write in chat for the first time each session.
Can also be used to play sounds when users send additional messages.
</sup>
</p>

## Table of Contents

* [About the Project](#about-the-project)
  * [Warning Notes](#warning-notes)
* [In Shorts](#in-shorts)
* [Changelog](#changelog)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Vip, Subscriber, Moderator Message](#vip-subscriber-moderator-message)
  * [Alias](#alias)
  * [Ignore Starting By](#ignore-starting-by)
  * [Do Not Greet](#do-not-greet)
  * [Greetings Audio](#greetings-audio)
    * [New Message Audio](#new-message-audio)
  * [Customize Per User](#customize-per-user)
    * [How To Set](#how-to-set)
    * [Omit Customizations](#omit-customizations)
    * [Special Chars](#special-chars)
    * [Examples](#examples)
  * [TTS: Text To Speach](#tts-text-to-speach)
    * [Custom TTS](#custom-tts)

## About The Project

Hi all,
 this script is mainly dedicated to streamers with low chat activity.

It just produces a sound and writes a greetings message when somebody
 sends his first message in chat, for current session.

Additionally, it can also reproduce another sound each time somebody
 writes again in chat, to get the streamer's attention on chat activity.

Anyway you can disable one or all sounds, so it would only greet
 textually for first user's message in chat.

Enjoy.

### Warning Notes

Note:  
 If you're updating from a previous 1.x version to new 2.x versions,
  they have no code retrocompatibility at all, so I suggest to:
1. note all settings from old version
2. completely delete old version
3. put new version
4. apply settings noted from old version

Note:  
 If you're updating from a previous 2.x version,
  you may have to delete old "lib" directory before update,
  because all new releases use new lib versions.

Note for Save Settings:  
 Sometimes Streamlabs Chatbot doesn't trigger `ReloadSettings` method on new
  settings save from Save Settings GUI button.
 
 If you can't hear TTS say the `Configuration updated successfully` sentence
  (by default `Configuration updated successfully`) probably new settings
  are saved, but you can't be sure if they're already reloaded and applied
  into current Chatbot session.
 
 In this case I'd suggest you to shut down and restart the Chatbot,
  or at least to refresh scripts from Scripts screen (the circle arrow icon
  on the top right).
 After that, make some checks to see if new settings are actually applied.
 
 Anyway, after every Chatbot start or reboot, I always suggest to refresh
  scripts at least once.

## In Shorts

- Script: Greetings
- Version: 2.0.1
- Description: Greet new viewers by playing a sound and/or a text
      message when they write in chat for the first time each session.
    Can also be used to play sounds when users send additional messages.
- Change: TTS Functions restored
      (libraries reworked from LuisSanchezDev's TheNewTTS script);
    Customizations per user
- Services: Twitch, Youtube
- Overlays: None
- Made By: @Patcha_it
- Update Date: 2023/10/02

## Changelog

- 2018/05/01 v1.0.0
  - Initial Release
- 2018/05/01 v1.1.0
  - Fixed compatibility with Mixer and Youtube
- 2018/10/05 v1.2.0
  - Added option for Text To Speach feature to read writer's nickname
- 2018/14/12 v1.2.1
  - Now TTS nick `black list filter` is case-insensitive
- 2018/17/12 v1.2.2
  - Now you can filter nicknames not to greet neither textually
    (aka: your own bots)
- 2019/04/07 v1.3.0
  - Now you can set a different sentence for VIP, subriscribers
    and moderators
- 2021/12/06 v1.4.1
  - Now you can filter nicknames to not check their messages
    and play no sound (aka: your own bots)
- 2021/12/06 v1.4.2
  - Fixed youtube name showing
- 2021/12/06 v1.4.3
  - Hidden the whole old TTS setting stuff, looking for a new
    working TTS server
- 2021/12/08 v1.4.4
  - Hotfixes thank to Castorr91
- 2022/02/09 v1.5.0
  - Now you can filter message by starting characters or words
    (i.e.: ! for chat commands)
- 2022/02/16 v1.5.1
  - Fixed typo on `Ignore messages starting by` splitter character
    (was comma, have to be space)
- 2022/08/05 v1.5.2
  - Fixed volume setting for sounds
- 2023/07/29 v2.0.0 -
  - TTS Functions restored, enhanced and tweaked
      (original code from LuisSanchezDev's The NewTTS script,
      recently reworked by me as The ReNewTTS script)
  - Settings section with fields to totally customize greetings
      details per specific users
  - Minor fixes and tweaks
  - Adopting file organization in subfolders
  - NOTE: There's no retrocompatibility with old 1.x versions
      You'll have to delete old versions first
        (while noting old settings)
- 2023/10/02 v2.0.1
  - Wrong default files into .zip distribution

PS:
Thanks @Castorr91 for some fixes suggestion. ;)

## Getting Started

### Prerequisites

Have an installation of Streamlabs Chatbot, already logged in to your accounts.
* [Download Streamlabs Chatbot](https://streamlabs.com/desktop-chatbot)

Follow this tutorial to prepare your Streamlabs Chatbot installation to accept scripts.
* [[Streamlabs Chatbot] Scripts Explained by Castorr91](https://www.youtube.com/watch?v=l3FBpY-0880)

### Installation

1. Download the latest version of the script.
2. If you haven't already, open your Streamlabs Chatbot and log in to your Streamer and Bot accounts.
3. On the left side, wait for the `Scripts` tab to pop up and click it.
4. On the top right corner of the window, next to the reload button is an import script button (Arrow pointing right to a box) and select the script downloaded before.
5. You will receive a message box confirming the import, accept it.
6. The window will update and show the `Greetings` script.
7. Click on the `Greetings` name to see the configuration pane.

## Usage

### Vip, Subscriber, Moderator Message

You can customize greeting message distinguishing between moderators,
  subscribers and VIPs.

Note:  
 Priority levels are `moderator -> subscriber -> VIP -> everyone`.  
 Which means if your moderator is also subscriber, he'll still have
  moderator's message; or if your subscriber is also VIP, he'll still
  have subscriber's message, and so on.

### Ignore Starting By
  <sup>(Don't greet messages starting by)</sup>

If your chat uses often messages starting by some characters or words,
 like chat minigames, commands or emotes, you can filter those message,
 by listing sequences of characters, and seaparte each sequence with a space.

If you also want to filter them for `New message audio` function, just list
 them the same way into the `Ignore messages starting by` field.

Note: spaces cannot be set into character sequences, because they're used
 as separators.

### Alias
If you want some users to be named with a different name, you can set an
 alias for each of them.

Just use this format to apply it:
```
TwitchNickName:Alias
```
(note: should work also for Youtube nicknames)

For every user you can set an alias, use semicolon to separate them:
```
AnUserNickName:HisAlias;AnotherUserNickName:AnotherAlias
```

You can use spaces and punctuation in aliases,
 except colon and semicolon.

### Do Not Greet
  <sup>(Users not to greet)</sup>

If you have bots or other users you don't want to greet on chat, just
 list their nick separated by commas, into field
 `Users not to greet + Blacklisted words`.

Into this same field, you can also filter black listed words to prevent
 sudden inopportune nicknames to be greeted by the script.
You can use plus simbol + between two words meaning `any character
 between them` like: Bad+Word would filter both BadWord and BadDamnWord.

If you also want to filter them for `New message audio` function, when
 they write a new message in chat, just list them also into the field
 `Users not to check messages`.  
You find it into `Chat message sound` settings section.
Only Twitch or Youtube nicknames can be listed there, no words.

### Greetings Audio

You can disable audio by writing no file name (empty field) on field
 `Greeting audio`, or set `Volume greeting audio` to zero.

You can also personalize your sounds to play a different file, editing
 `Greeting audio` field.

Note:  
 If the file is not located into script's audio subfolder or
  script's folder itself, please use its absolute path.

Note:  
 Audio files have to be in `mp3` format.

#### New Message Audio
  <sup>(After First Message)</sup>

It works same identical way as greeing audio, except it's setting
 field is named `New message audio`, it's volume settings is
 `Volume new message audio` and it is played when a new chat messages
 is sent by a viewer after he/her was already greeted on first message.

For `starting by` and `not greet` fields, they also work the same way
 than their twin fields on `General` settings section, except they're
 applied to new chat messages viewers sends after their first message.

### Customize Per User

This is an advancer settings section which allows far more script's 
 feedbacks customization per user.
If it scares you or you don't need such features, just left those fields
 blank or untouched.
In that case, you may want to skip this part of the readme and go to
 next part, dedicated to TTS (Text to Speech).

About this `Customize per user` setting section...  
The base logic is that you list a series of texts (greeting messages),
 audio file paths and TTS (texts to be read by TTS) and so put them at
 your own disposition to further customize scrips feedbacks.  
Every element will be surrounded by quotes.
The script will index such lists by element's position, starting by 1.

For instance, if `Audio custom greetings collection` is like:
```
"AFile.mp3""Another.mp3""StillListed.mp3"
```
Then they'll referred such index 1 for AFile.mp3, index 2 for Another.mp3
 and index 3 for StillListed.mp3 .

Note:  
 If audio files are not located into script's audio subfolder or
  script's folder itself, please use their absolute paths.

Note:  
 TTS will work only if you activate TTS in its dedicated settings'
  section.

#### How To Set

So, as said, in these `Customize per user` settings section the first
 3 fields are there to let you list your own custom chat greeting
 messages, custom audio to be played and custom text to be read by TTS.
Each of these listed elements have to be surrounded by quotes, and
 they'll be indexed.

The fourth field will let you relate those indexed elements, from those
 lists, to customize your script's feedback to some particular users.
This relation is made this way:
```
"UserNickName:GreetIndex:AudioIndex:TTSindex"
```

Such as `"UserNickName:1:1:1"` would assign first custom greeing message,
 first custom audio file and first TTS text to user named UserNickName.

#### Omit Customizations

If you want to omit some customization, you can:
- put zero (0 = no customization) as index where it's corresponding
- totally omit colon and indexes if they came after.

For instance:
- if you want to set only a custom greetings text, you can use:
 `"UserNickName:1"`, this omits custom audio and custom TTS
- if you want to set no TTS but just greeting text and audio, you use:
 `"UserNickName:1:1"`
- if you want to set only TTS, but no custom greeting and audio:
 `"UserNickName:0:0:1"`
- if you want to set only custom audio and TTS, you'd use this:
 `"UserNickName:0:1:1"`

And so on, like `"UserNickName:1:0:1"` if you don't want customized audio.

#### Special Chars

You can dynamically put user's account's nickname, or his/her setted
 alias, into elements (even file names for audio), by using
 following characters sequence:
  - {0} will add his alias, if any setted, otherwise his user's nickname
  - {1} will always be his/her user's nickname, aka:
    Twitch or Youtube username

So if you setted the following alias `FooNickname:JohnDoe` , in `General`
 settings section, it'd mean `FooNickName` (Twitch or Youtube user)
 will be referred with `JohnDoe` alias.

Then `{0}` into elements would be dynamically replaced with `JohnDoe`
 and `{1}` would be replace with `FooNickname`.

#### Examples

We now create a complete settings case, and then we'll foresee its
 effects when involved users will join the chat for the first time in
 current session:

If `Text custom greetings collection` field is:  
```
"Hi {0}, are you incognito?""No {1}! Not you again!""{0} is here again!"
```

If `Audio custom greetings collection` field is:
```
"Claps.mp3""{1}.mp3"
```
Note:  
 We're assuming that such files are located into script's `audio` folder.

If `TTS custom greetings collection` field is:
```
"And his name is {0}!!!"
```
Note:  
 We're assuming that TTS is enabled in `TTS Configuration` section.

If `Users assignment to custom greetings` field is:
```
"FooNickname:1:2""WeakOne:3:1:1""SmeelyJoe:2:2""GreatCookie:0:2"
```

Let's also assume the field `Alias to apply to users`, in `General`
 setting section, is setted like this:
```
FooNickname:John Doe;WeakOne:John Cena;SmeelyJoe:The smelly one
```

Here's what will happen when...

> User `FooNickname` (Twitch or Youtube username) will join the chat
 writing his/her first message for the current session:

- Will be greeted with this text message in chat:  
`Hi John Doe, are you incognito?`  
 Because index `1` is corresponding to `"Hi {0}, are you incognito?"` and
  `{0}` is replaced with his/her alias `John Doe`.

- This audio will be played:  
`FooNickname.mp3`  
 Because index `2` is corresponding to `"{1}.mp3"` and `{1}` is replaced
  with the username `FooNickname`.

- TTS will just spell his alias `John Doe`, because no particular
 TTS customization was setted for `FooNickname`, and so by default TTS
 spells user's alias, if he/her have one, otherwise the username.

> User `WeakOne` (Twitch or Youtube username) will join the chat
 writing his/her first message for the current session:

- Will be greeted with this text message in chat:  
`John Cena is here again!`  
 Because index 3 is corresponding to `"{0} is here again!"` and `{0}` is
  replaced with the alias "John Cena".

- This audio will played:  
`Claps.mp3`  
 Because index 1 is corresponding to `"Claps.mp3"`.

- TTS will spell this sentence:  
`And his name is John Cena!!!`  
 Because index `1` is corresponding to `"And his name is {0}!!!"` and `{0}`
  is replaced with the alias `John Cena`.

> User `SmeelyJoe` (Twitch or Youtube username) will join the chat
 writing his/her first message for the current session:

- Will be greeted with this text message in chat:  
`No SmeelyJoe! Not you again!`  
 Because index `2` is corresponding to `"No {1}! Not you again!"` and
  `{1}` is replaced with the username `"SmeelyJoe"` (not the alias!).

- This audio will played:  
`SmeelyJoe.mp3`  
 Because index `2` is corresponding to `"{1}.mp3"` and `{1}` is replaced
  with the username `SmeelyJoe`.

- TTS will just spell his alias `The smelly one`, because no particular
 TTS customization was setted for `SmeelyJoe`, and so by default TTS
 spells user's alias, if he/her have one, otherwise the username.

> User `GreatCookie` (Twitch or Youtube username) will join the chat
 writing his/her first message for the current session:

- Will be greeted with the role's message or with default message if
 he/her has no particular role, as for settings in `General` section.  
 This is because index `0` means that no particular text greetings
 customization was setted for `GreatCookie`.

- This audio will played:  
`GreatCookie.mp3`  
 Because index `2` is corresponding to `"{1}.mp3"` and `{1}` is replaced
  with the username `GreatCookie`.

- TTS will just spell the username `GreatCookie`, because no particular
 TTS customization was setted for `GreatCookie`, and also no particular
 alias was set for `GreatCookie` into `General` settings section.
 So by default TTS will spells his/her username.

### TTS: Text To Speach

Note:  
 This function, into THIS script, DOESN'T read users' messages!  
 This just read their nicknames (or their alias, if any setted) on their
 very first message in chat, if messages are not skipped by
 `Starting by` and `Blacklist` settings in `General` settings section.

TTS can be enabled or not.
By default it uses `Google translate` free TTS service, so you can
 chose the languange, but not the voice gender, because Google only
 provides one gender per language.

Note that into next section, you can set a customized TTS webservice,
 if you have any at your disposition.

You can alter volume, pitch and speed of TTS.
(You could want to disable these functions, removing checks, if you
 run a custom TTS webservice and these function could alter TTS voices
 even on `neutral` values.)

You can force it to read lowercase (which usually means less chance
 it could interprets an username as an acronym) or uppercase (somehow
 more chance that it reads usernames as acronyms).

If the bot seems to have any kind of odd pronunciacion on a nickname of
 abitual viewers of yours, you can try to force him to replace some
 particular characters series with a different series of characters.

For instance:  
 My nickname is Patcha, which should be spelled like patch.
 But my bot setted as Italian spells it odd, so I set to replace "atcha"
 with "accia" which is something in italian we spell much more similar
 to how "atcha" would be spelled in English.

Note that this setting is very "invasive": be sure you don't end up
 replacing a series of characters which are commonly used in your
 language, or you'd create some oddity on other unexpected nicknames.

Usernames can often use some odd punctuation which the bot could name
 letterally. For instance the underscore.
So there's an option which allows you to replace a series of characters
 each one with a space, so that the TTS wouldn't try to name them
 litterally, but still it would separate as two different words.


#### Custom TTS

The following section can be used if you can reach a webservice of your
 own, so you can have a more punctual control on your TTS.

Apart the Webservice link itself (by defaul is Google Translator, even
 if you left the field empty) and the returned audio format
 (the file extension), you can even preset some parameters which
 will be added to the webservice address.

Parameters field is not mandatory, you can also add them directly into
 Webservice's address.
But if you feel it comfortable, you can use this field to reach and
 change them faster.

Parameters are a series of texts, surrounded each by quotes.
They'll be replaced into Webservice's address where you'll write {2},
 {3}, {4} and so on, so they're indexed starting from 2.
This is because {0} is already the text to be read by TTS, so in our
 script it's users's username or aliases (or customized TTS greetings).
While {1} is the "language" code you can set in the previous settings
 section (the drop down menu).
Note that very often lang codes for languages don't fit between a TTS
 webservice and another. In that case, don't use {1}, but set your own
 parameter for your language on your own webservice link.

Note:  
 I'm not sure on how many audio formats are supported.
 If it seems not to work, try to set your TTS webservice to generate a
  different audio format. For now I just tested .mp3 and .wav formats.
