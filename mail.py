#!/usr/bin/python
#print("hey")

import imaplib

M = imaplib.IMAP4_SSL("SERVER",PORT)
M.login("EMAIL","PASSWORD")
M.select('INBOX', True)
#M.recent()
typ, data = M.search(None, 'NEW')
if data[0].split():
    num = data[0].split()[0]
    typ, data = M.fetch(num, '(RFC822)')
    #print("Mail:"+ data[0][1].decode().split("\nSubject:", 1)[1].splitlines()[0] + "From:" + data[0][1].decode().split("\nFrom:", 1)[1].splitlines()[0])
    print('Mail:%s (From:%s)' % (data[0][1].decode().split("\nSubject:", 1)[1].splitlines()[0], data[0][1].decode().split("\nFrom:", 1)[1].splitlines()[0]))
M.close()
M.logout()

