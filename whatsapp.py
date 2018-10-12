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

def main():
    print('Starting driver...')
    DRIVER = WhatsAPIDriver(profile='/home/nexor/.mozilla/firefox/794uxbrx.default')
    print('Logging in...')
    DRIVER.wait_for_login()
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chats',                action='store_true',        help='show chats')
    parser.add_argument('-C', '--contacts',             action='store_true',        help='show all contacts ever seen by this account')
    parser.add_argument('-m', '--my-contacts',          action='store_true',        help='show my contacts (added to address book)')
    parser.add_argument('-s', '--send',                 metavar='MESSAGE',          help='send message (requires --to flag)')
    parser.add_argument('-B', '--broadcast',            metavar='MESSAGE',          help='send message to all chats')
    parser.add_argument('-b', '--broadcast-contacts',   metavar='MESSAGE',          help='send message to all contacts')
    parser.add_argument('-t', '--to',                   metavar='[CONTACT|CHAT]',   help='apply command only to this CONTACT or CHAT', required='-s' in sys.argv)
    args = parser.parse_args()
    code.interact(local=locals())
    if args.chats: print(json.dumps({'chats' : [c.name for c in DRIVER.get_all_chats()]}, indent=4))
    elif args.my_contacts: print(json.dumps({'my_contacts': [c.name for c in DRIVER.get_my_contacts()]}, indent=4))
    elif args.contacts: print(json.dumps({'all_contacts': [c.name for c in DRIVER.get_contacts()]}, indent=4))
    DRIVER.close()

if __name__ == '__main__': main()
