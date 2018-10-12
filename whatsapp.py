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
import code
import glob
import os

DEBUG = False
LOG = sys.stdout

def main():
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
    parser.add_argument('-t', '--to',                   metavar='[CONTACT|CHAT]',   help='apply command only to this CONTACT or CHAT', required='-s' in sys.argv)
    args = parser.parse_args()
    if args.verbose: DEBUG = True
    if args.log: LOG=args.log
    if not args.profile: args.profile = glob.glob(os.path.expanduser('~/.mozilla/firefox/*.default'))[0]
    if not os.path.exists(args.profile): 
        if DEBUG: print('Profile not found %s' % args.profile)
        sys.exit(1)
    DEBUG and print('Starting driver with profile at %s' % args.profile, file=LOG)
    DRIVER = WhatsAPIDriver(profile=args.profile)
    DEBUG and print('Profile loaded. Waiting for login...', file=LOG)
    DRIVER.wait_for_login()
    DEBUG and print('Logged in', file=LOG)
    log_json = lambda d: print(json.dumps(d, indent=4))
    if args.chats: log_json({'chats' : [c.name for c in DRIVER.get_all_chats()]})
    elif args.my_contacts: log_json({'my_contacts': [c.name for c in DRIVER.get_my_contacts()]})
    elif args.contacts: log_json({'all_contacts': [c.name for c in DRIVER.get_contacts()]})
    DRIVER.close()

if __name__ == '__main__': main()
