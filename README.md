[![development status | 7 - Inactive](https://img.shields.io/badge/Development_Status-7_--_Inactive-orange)](https://pypi.org/classifiers/)
[![code style: pep-008](https://img.shields.io/badge/code_style-pep--0008-FFF8FF)](https://peps.python.org/pep-0008/)
![license](https://img.shields.io/badge/license-MIT-green)
![version](https://img.shields.io/github/v/tag/PatchaIT/greetings)
___
<h1 align="center">
Greetings
</h1>
<p align="center">
<sup>
(On your Streamlabs Chatbot) Produces a sound and writes a greetings message when somebody sends his first message in chat, for current session.
</sup>
</p>

## Table of Contents

* [About the Project](#about-the-project)
* [In Shorts](#in-shorts)
* [Changelog](#changelog)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Greetings Audio](#greetings-audio)
  * [New Message Audio](#new-message-audio)
* [TTS BOT Install And Settings](#tts-bot-install-and-settings)
  * [TTS BOT Install](#tts-bot-install)
  * [TTS BOT Settings](#tts-bot-settings)

## About The Project

Hi all,
 this script is mainly created for early streamers with low chat activity.

It just produces a sound and writes a greetings message when somebody sends his
 first message in chat, for current session.

Additionally, it can also reproduce another sound each time somebody writes
 again in chat.
Or even read viewer's name with a TTS Bot (Text To Speach), after greetings
 for its first message.

Anyway you can disable one or all sounds, so it would only greet textually
 for first message in chat.

Enjoy.

## In Shorts

- Script: Greetings
- Version: 1.2.1
- Description: Produces a sound and writes a greetings message when somebody sends his first message in chat, for current session. It can also reproduce another sound each time somebody write again in chat, or even read username with TTS. Anyway you can disable each sound. It could also just greet textually for first message in chat.
- Changes: Added Text To Speach feature to read writer's nickname.
- Services: Twitch, Mixer, Youtube
- Overlays: Only TTS Bot
- Made By: @Patcha_it

## Changelog

- 2018/05/01 v1.0
  - Initial Release
- 2018/05/01 v1.1
  - Fixed compatibility with Mixer and Youtube
- 2018/10/05 v1.2
  - Added Text To Speach feature to read writer's nickname.
- 2018/14/12 v1.2.1
  - Now TTS nick "black list filter" is case-insensitive

PS:
Thanks @Castorr91 for some fixes suggestion and sharing on Discord. ;)

## Getting Started

### Prerequisites

Have an installation of Streamlabs Chatbot, already logged in to your accounts.
* [Download Streamlabs Chatbot](https://streamlabs.com/desktop-chatbot)

Follow this tutorial to prepare your Streamlabs Chatbot installation to accept scripts.
* [[Streamlabs Chatbot] Scripts Explained by Castorr91](https://www.youtube.com/watch?v=l3FBpY-0880&t=3s)

### Installation

1. Download the latest version of the script.
2. If you haven't already, open your Streamlabs Chatbot and log in to your Streamer and Bot accounts.
3. On the left side, wait for the `Scripts` tab to pop up and click it.
4. On the top right corner of the window, next to the reload button is an import script button (Arrow pointing right to a box) and select the script downloaded before.
5. You will receive a message box confirming the import, accept it.
6. The window will update and show the `Greetings` script.
7. Click on the `Greetings` name to see the configuration pane.

## Usage

### Greetings Audio

You can disable audio by writing no file name (empty field) on `Greeting audio`
 or set `Volume greeting audio` to zero.

You can also personalize your sounds to play a different file, by editing
 `Greeting audio` field. If file is not located into script's folder,
 please use an absolute path.

Audio files have to be in `mp3` format.

#### New Message Audio
  <sup>(After First Message)</sup>

It works same identical way as greeing audio, except it's file path field
 is named `New message audio` and it's volume is `Volume new message audio`.

### TTS BOT Install And Settings
  <sup>(Text To Speach Bot)</sup>

Note 1: TSS Bot will automatically attempt to read the message writer's nickname.  
Keep in mind that result will easily be more different than expected in most
 cases, because very often nicknames are not exactly meaningful words.  
So for the most it can be intended as a "fun" feature.

Note 2: TTS Bot configuration fields are divided into 3 different subcategories.  
 During this guide, fields name could be anticipated by it's subcategory name.

#### TTS BOT Install

The Text To Speach service is given by a web page, that you'll have to
 configure as websource into your streaming software (i.e: OBS).
The link between your bot and that webpage is given by a particular generated key.
To generate a key, you need to provide a referral nickname.
By default this script will use your personal channel name, but you can
 configure a different nickname, if you wish, by filling the field named
 `TTSBot User -> Custom user (optional)`.

To get the aforesaid key you'll have to press button
 `TTSBot User -> GET BROWSER SOURCE URL`.
This button will both:
  - make your bot account send you a whisper (if applicable) to your streamer account.
 The whispered message will contain your Browser Source URL and key to be set on your stream.
  - open a web page in your default browser on your Browser Source URL.

To get your key:
  - into whisper message, you get the key as last thing wrote into that message
  - into your browser, from the webpage url, your key is the second last part,
 between slashes. The url will be formatted this way:
  http://tts.warp.world:5500/tts/< your key here >/< referral nickname >

Now you have to take this key and set it into field
 `TTSBot User -> Generated Key`.
Note: if you don't set a key, TTSBot will not work.

You don't need to generate a new key for each stream. But if your key get stolen
 and somebody starts sending TTS messages with your url, you can still generate
 a new key with same referral nickname, by reclicking the button. And then
 configure the new key on your bot and a the new URL on your streaming software.

 
#### TTS BOT Settings

`TTSBot` category: here you can actually customize your voicebot.

- `Turn ON TTS Bot` visa let you quickly turn on and off TSS Bot.
  Obviously it have to be checked to make TSS Bot work, but also remember
   that your bot key must be correctly setted up, too (see installation).

- `Audio Volume` lets you set up TTS Bot voice volume.

- `Black listed words` with this field you can prevent TSS Bot to vocally
   read inopportune words were a nickname could contain them.  
  Note: please report me if it works, I had no way to actually test it.

  You can split word series with commas, and consolidate them by plus.  
  This means, for instance, if you put "Man, Bad+Woman", this script will
   filter all names containing "Man", and also those containing BOTH
   "Woman" and "Bad". But not names containing ONLY "Woman" or ONLY "Bad".

- `Bot Language` will let you decide which cadency will TSS Bot use.

  If you ever "played" with Google Translator's TTS service, you'll know
   that accent and pronunciation needs to be different between languages.
  This field will let you choice between principal languages.  
  I'm sorry if any of your languages could be missing.


`TTSBot User` category: we already talked about this into "Installation"
  tutorial. Anyway here another short explanation about fields.

- `Generated Key` is where you have to put your TTS Bot bot private key.
  (See installation instructions.)

- `Custom user (optional)`, fill this with a different nickname, if you
   don't want to use your channel name.  
  If your private key get stolen, by setting this field differently than
   your channel name, it will makes harder to use the stolen key.

- `GET BROWSER SOURCE URL` is the button which lets you generate a new
    key, if you still have none or if you fear somebody stolen it to you.


`TTSBot Overlay Style` category: don't ask me why, but TSS Bot web
  source is not just about audio, there's also an overlay which writes
  the message itself (in this case, writer's nickname).

  If you don't wanna see it, just place it on your scene where cannot be
   seen. In case, I suggest you to put green background and use chromakey.  
  Alternatively, just set it's size to 0 length and 0 width.

  Anyway, into this category you can personalize font and colors.

- `Overlay Google font` let you set a font for your overlay.

  TTS Bot uses Google fonts. Actually you could set any font, but I prefered
   to put just top 15 used fonts into a dropdown selection.

- `Overlay font size` is litterally the size of text.

- `Overlay font color` is the color of the text itself.

- `Overlay border color` is the color of a border to put around text.

- `Overlay background color` as said before, text is wrote into an "area"
   and this area is coloured. Here you can choose the color, but I suggest
   to put green and use chroma key to make it trasparent.

   Note: colors interface let you set also alpha channel, aka transparency,
    but this parameter is actually IGNORED, because not supported by TTS Bot.
