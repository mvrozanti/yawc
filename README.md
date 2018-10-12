# Yet Another WhatsApp Client

## Why another one?

- None of them can do automation at the moment
- Hard to setup
- Unintuitive commands

## Requirements

- Firefox version 61.0

- Python 3

- GeckoDriver 
  - `sudo pacman -S geckodriver` on Arch Linux

## Installation

- This project uses [WhatsApp-Wrapper](https://github.com/mukulhase/WebWhatsapp-Wrapper) API so it needs to be cloned *recursively*:

```
git clone --recursive https://github.com/mvrozanti/yawc \
  cd yawc/WebWhatsapp-Wrapper \
  pip3 install --user -r requirements.txt \
  pip3 install --user .
```

- Make sure you have geckodriver and Firefox 61 installed:
  - `geckodriver -v; firefox -v`

## Usage

```
usage: whatsapp.py [-h] [-c] [-C] [-v] [-m] [-s MESSAGE] [-B MESSAGE]
                   [-b MESSAGE] [-p LOCATION] [-l LOCATION]
                   [-t [CONTACT|CHAT]]

optional arguments:
  -h, --help            show this help message and exit
  -c, --chats           show chats
  -C, --contacts        show all contacts ever seen by this account
  -v, --verbose         verbose logging
  -m, --my-contacts     show my contacts (added to address book)
  -s MESSAGE, --send MESSAGE
                        send message (requires --to flag)
  -B MESSAGE, --broadcast MESSAGE
                        send message to all chats
  -b MESSAGE, --broadcast-contacts MESSAGE
                        send message to all contacts
  -p LOCATION, --profile LOCATION
                        use firefox profile contained in LOCATION
  -l LOCATION, --log LOCATION
                        log to LOCATION
  -t [CONTACT|CHAT], --to [CONTACT|CHAT]
                        apply command only to this CONTACT or CHAT
```
