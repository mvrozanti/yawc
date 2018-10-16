#!/usr/bin/env python3
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message,MMSMessage
import code
import json
from datetime import datetime
import argparse
import numpy as np
import sys
import matplotlib.pyplot as plt
import time
import sqlite3
import glob
import os
import os.path as op
import atexit
import psutil
import readline

LOG = sys.stdout
DRIVER = None
class MyCompleter(object):
    def __init__(self, options): self.options = sorted(options)
    def complete(self, text, state):
        if state == 0:
            if text: self.matches = [s for s in self.options if s and s.startswith(text)]
            else: self.matches = self.options[:]
        try: return self.matches[state]
        except IndexError: return None

def exit_gracefully():
    DRIVER.close()
    try: 
        for proc in psutil.process_iter():
            if proc.name() == 'geckodriver': proc.kill()
    except Exception as e: code.interact(local=locals())
    finally: sys.exit(0)

def main(args):
    DEBUG = args.verbose
    if args.log: 
        global LOG
        try: LOG = open(args.log, 'w') 
        except Exception as e: print(e) and sys.exit(0)
    if not args.profile: args.profile = glob.glob(op.expanduser('~/.mozilla/firefox/*.default'))[0]
    if not op.exists(args.profile): 
        DEBUG and print('Profile not found %s' % args.profile)
        sys.exit(1)
    DEBUG and print('Starting driver with profile at %s' % args.profile, file=LOG)
    global DRIVER
    DRIVER = WhatsAPIDriver(profile=args.profile)
    atexit.register(exit_gracefully)
    DEBUG and print('Profile loaded. Waiting for login...', file=LOG)
    DRIVER.wait_for_login()
    DEBUG and print('Logged in', file=LOG)
    def log_json(d): 
        global LOG
        print(json.dumps(d, indent=4), file=LOG)
    if args.chats: log_json({'chats' : [c.name for c in DRIVER.get_all_chats()]})
    elif args.my_contacts: log_json({'my_contacts': [c.name for c in DRIVER.get_my_contacts()]})
    elif args.contacts: log_json({'all_contacts': [c.name for c in DRIVER.get_contacts()]})
    elif args.send:
        if not args.to:
            contact_type = None
            if args.log: print('Cannot use -s with -l without -t', file=LOG) and exit_gracefully()
            while not contact_type:
                try: contact_type = int(input('\t1) Contact\n\t2) Recent chat\nSend to: '))
                except: pass
            if contact_type == 1: 
                contacts = DRIVER.get_contacts()
                prompt = ''
                code.interact(local=locals())
                prompt += '\n'.join([str(i) + ') ' + c.name + ': ' + c.id for i, c in enumerate(contacts) if c.name])
                prompt += '\nSelect contact: '
                chosen = None
                while not chosen:
                    try: chosen = int(input(prompt))
                    except: pass
                args.to = contacts[chosen].id
            elif contact_type == 2: pass
        DRIVER.send_message_to_id(args.to, args.send)

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chats',                action='store_true',        help='show chats')
    parser.add_argument('-C', '--contacts',             action='store_true',        help='show all contacts ever seen by this account')
    parser.add_argument('-v', '--verbose',              action='store_true',        help='verbose logging')
    parser.add_argument('-m', '--my-contacts',          action='store_true',        help='show my contacts (added to address book)')
    parser.add_argument('-s', '--send',                 metavar='MESSAGE',          help='send message (requires --to flag)')
    parser.add_argument('-B', '--broadcast',            metavar='MESSAGE',          help='send message to all chats')
    parser.add_argument('-b', '--broadcast-contacts',   metavar='MESSAGE',          help='send message to all contacts')
    parser.add_argument('-p', '--profile',              metavar='LOCATION',         help='use firefox profile contained in LOCATION (defaults to ~/.mozilla/firefox/*.default)')
    parser.add_argument('-l', '--log',                  metavar='LOCATION',         help='log to LOCATION')
    parser.add_argument('-t', '--to',                   metavar='[CONTACT|CHAT]',   help='apply command only to this CONTACT or CHAT')
    args = parser.parse_args()
    main(args)
#     completer = MyCompleter([])
#     readline.set_completer(completer.complete)
#     readline.parse_and_bind('tab: complete')
