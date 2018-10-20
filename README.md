# Yet Another WhatsApp Client

## Why another one?

- None of them can do automation at the moment
- Hard to setup
- Unintuitive commands

## Requirements

- [Firefox version 61.0](https://download-installer.cdn.mozilla.net/pub/firefox/releases/61.0.2/linux-x86_64/en-US/firefox-61.0.2.tar.bz2)

- Python 3

- GeckoDriver 
  - `sudo pacman -S geckodriver` on Arch Linux

## Installation

- This project uses [WhatsApp-Wrapper](https://github.com/mukulhase/WebWhatsapp-Wrapper) API so it needs to be cloned *recursively*:

```
git clone --recursive https://github.com/mvrozanti/yawc \
  cd yawc/WebWhatsapp-Wrapper \
  pip3 install --user -r requirements.txt \
  pip3 install --user . \
  cd .. \
  !-3
```

- Make sure you have geckodriver and Firefox 61 installed:
  - `geckodriver -v; firefox -v`

## Usage

```
usage: yawc [-h] (-c | -C | -m | -s MESSAGE | -B MESSAGE | -b MESSAGE)
            [-t [CONTACT|CHAT]] [-v] [-p LOCATION] [-l LOCATION]

Interface for WebWhatsapp-Wrapper API

optional arguments:
  -h, --help            show this help message and exit
  -c, --chats           show chats
  -C, --contacts        show all contacts ever seen by this account
  -m, --my-contacts     show my contacts (added to address book)
  -s MESSAGE, --send MESSAGE
                        send message (requires --to flag)
  -B MESSAGE, --broadcast MESSAGE
                        send message to all chats
  -b MESSAGE, --broadcast-contacts MESSAGE
                        send message to all contacts
  -t [CONTACT|CHAT], --to [CONTACT|CHAT]
                        apply command to this CONTACT or CHAT
  -v, --verbose         verbose logging
  -p LOCATION, --profile LOCATION
                        use firefox profile contained in LOCATION (defaults to
                        ~/.mozilla/firefox/*.default)
  -l LOCATION, --log LOCATION
                        log to LOCATION
```

## TODO

- Support unicode
- More flags
- Support images
- Use `-` as stdin reference in order to enable piping from shell
