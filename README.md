[![development status | 7 - Inactive](https://img.shields.io/badge/Development_Status-7_--_Inactive-orange)](https://pypi.org/classifiers/)
[![code style: pep-008](https://img.shields.io/badge/code_style-pep--0008-FFF8FF)](https://peps.python.org/pep-0008/)
![license](https://img.shields.io/badge/license-MIT-green)
![release](https://img.shields.io/github/v/release/PatchaIT/greetings)
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
  * [Warning Note](#warning-note)
* [In Shorts](#in-shorts)
* [Changelog](#changelog)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Vip, Subscriber, Moderator Message](#vip-subscriber-moderator-message)
  * [Do Not Greet](#do-not-greet)
  * [Ignore Starting By](#ignore-starting-by)
  * [Greetings Audio](#greetings-audio)
    * [New Message Audio](#new-message-audio)

## About The Project

Hi all,
 this script is mainly created for early streamers with low chat activity.

It just produces a sound and writes a greetings message when somebody sends his
 first message in chat, for current session.

Additionally, it can also reproduce another sound each time somebody writes
 again in chat.

Anyway you can disable one or all sounds, so it would only greet textually
 for first message in chat.

Enjoy.

### Warning Note

If you're updating for a previous versions, after loading Chatbot and
 all scripts, do as follows:
1. if you can't find `Greetings` anymore, go to script folder (right click
 on a script + click `Open Script Folder` + open `Greetings` folder) and
 backup/delete/rename these files: `settings.js` and `settings.json`
 (they are your current config files)
2. click refresh script buttons (two cicle arros icon, the first on top
 right), click on Greetings script and save again settings (even if you
 didnt' change them). This would recreate `settings.js` and `settings.json`
 files with new options included.
3. I suggest to refresh scripts again.

## In Shorts

- Script: Greetings
- Version: 1.5.2
- Description: Produces a greetings sound and message when somebody write first
 time in a session. It can reproduce another sound each time somebody writes
 again in chat. Sounds can still be disabled, to just greet textually for first
 message in chat.
Change: Fixed volume setting for sounds.
- Services: Twitch, Youtube
- Overlays: None
- Made By: @Patcha_it
- Update Date: 2022/08/05

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
  - Now you can set a different sentence for VIP, subriscribers and moderators
- 2021/12/06 v1.4.1
  - Now you can filter nicknames to not check their messages and play no sound
    (aka: your own bots)
- 2021/12/06 v1.4.2
  - Fixed youtube name showing
- 2021/12/06 v1.4.3
  - Hidden the whole text to speach setting stuff, looking for a new working TTS server
- 2021/12/08 v1.4.4
  - Hotfixes thank to Castorr91
- 2022/02/09 v1.5.0
  - Now you can filter message by starting characters or words
    (i.e.: ! for chat commands)
- 2022/02/16 v1.5.1
  - Fixed typo on "Ignore messages starting by" splitter character
    (was comma, have to be space)
- 2022/08/05 v1.5.2
  - Fixed volume setting for sounds

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

You can personalize that message distinguishing between moderators, VIPs
 and subscribers.

Note: priority levels are `moderator -> subscriber -> VIP -> everyone`.  
 Which means if your moderator is also subscriber, he'll still have moderator
 message; or if your subscriber is also VIP, he'll still have subscriber
 message, and so on.

### Do Not Greet
  <sup>(Users not to greet)</sup>

If you have bots or other users you don't want to greet on chat, just list
 their nick separated by commas, into `Users not to greet` field.

If you also want to filter them for `New message audio` function, just list
 them the same way into the `Users not to check messages` field.

### Ignore Starting By
  <sup>(Don't greet messages starting by)</sup>

If your chat uses often messages starting by some characters or words,
 like chat minigames, commands or emotes, you can filter those message,
 by listing sequences of characters, and seaparte each sequence with a space.

If you also want to filter them for `New message audio` function, just list
 them the same way into the `Ignore messages starting by` field.

Note: spaces cannot be set into character sequences, because they're used
 as separators.

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
