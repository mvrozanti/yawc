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

- This project uses [WebWhatsApp-Wrapper](https://github.com/mukulhase/WebWhatsapp-Wrapper) API so it needs to be cloned *recursively*:

```
git clone --recursive https://github.com/mvrozanti/yawc \
  cd yawc/WebWhatsapp \
  pip3 install --user -r requirements.txt \
  cd .. \
  !-2
```

- Make sure you have geckodriver and Firefox 61 installed:
  - `geckodriver -v; firefox -v`

## Usage

```
usage: yawc [-h]
            (-c | -C | -m | -s MESSAGE | -B MESSAGE | -b MESSAGE | -e [DURATION])
            [-t [CONTACT|CHAT]] -D PATH [-v] [-p LOCATION] [-l LOCATION]

Interface for WebWhatsapp-Wrapper API

optional arguments:
  -h, --help            show this help message and exit
  -c, --chats           show chats
  -C, --contacts        show all contacts ever seen by this account
  -m, --my-contacts     show my contacts (added to address book)
  -s MESSAGE, --send MESSAGE
                        send message. If MESSAGE equals '-', read from stdin.
                        Requires --to flag
  -B MESSAGE, --broadcast MESSAGE
                        send message to all chats
  -b MESSAGE, --broadcast-contacts MESSAGE
                        send message to all contacts
  -e [DURATION], --events [DURATION]
                        watch events (default duration=30)
  -t [CONTACT|CHAT], --to [CONTACT|CHAT]
                        apply command to this CONTACT or CHAT
  -D PATH, --save-directory PATH
                        specify directory where to safe multimedia
  -v, --verbose         verbose logging
  -p LOCATION, --profile LOCATION
                        use firefox profile contained in LOCATION (defaults to
                        ~/.mozilla/firefox/*.default)
  -l LOCATION, --log LOCATION
                        log to LOCATION
```

## TODO

- [ ] Support unicode
- [ ] Send message --to [exact name of contact instead of just c.id]
- [ ] Send/Download images
- [ ] Read messages continously in an optionally set format
- [ ] Add user to group
- [ ] Frequency reports
- [ ] Implement event logging (online logs, typing status and more)
