import email
import imaplib
import os
import sys
import time
from settings import app

# Account name and Google App Token
userName = 'jpisano99@gmail.com'
my_token = app['GMAIL_TOKEN']

# Authenticate and Create the email object
gmail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

# Login
status, accountDetails = gmail.login(userName, my_token)
print(status, accountDetails[0].decode('utf-8'))

# Select and Inbox to read
num_of_emails = gmail.select("Netgear_Logfiles")




print (status, accountDetails[0].decode('utf-8'))





# print (num_of_emails[0], str(num_of_emails[1].decode("utf-8")))


exit()
# gmail.select("Inbox")
typ, data = gmail.search(None, 'ALL')

print (typ, 'Num of emails: ', len(data[0].split()))
print('Data: ', len(data))
print('Data 0: ', data[0])

for msgId in data[0].split():
    typ, messageParts = gmail.fetch(msgId, '(RFC822)')
    emailBody = messageParts[0][1]
    print(msgId)

    mail = email.message_from_bytes(emailBody)

    headers = mail.items()
    header_dict = dict(headers)
    date = header_dict['Date']
    try:
        subject = header_dict['Subject']
    except:
        subject = 'None'

    payload = mail.get_payload()

    print('subject: ',subject)
    print('date: ',date)
    print('payload: ',payload)
    # print('payload: ',payload.split('\n'))

    for line in payload.split():
        if '[Admin login]'  in line:
            print (line)
        elif '[LAN access from remote]' in line:
            print(line)
        elif '[DoS attack: ACK Scan]' in line:
            print(line)
        elif '[DoS attack: FIN Scan]' in line:
            print(line)
        elif '[Illegal Login]' in line:
            print(line)
        elif '[WLAN access rejected: incorrect security]' in line:
            print(line)
        elif '[Admin login failure]' in line:
            print(line)

gmail.close()
gmail.logout()

# try:
#     imapSession = imaplib.IMAP4_SSL('imap.gmail.com',993)
#     typ, accountDetails = imapSession.login(userName, passwd)
#     if typ != 'OK':
#         print ('Not able to sign in!')
#         raise
#
#     imapSession.select('Inbox')
#     typ, data = imapSession.search(None, 'ALL')
#     if typ != 'OK':
#         print ('Error searching Inbox.')
#         raise
#
#     # Iterating over all emails
#     for msgId in data[0].split():
#         typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
#
#         if typ != 'OK':
#             print ('Error fetching mail.')
#             raise
#
#         #print(type(emailBody))
#         emailBody = messageParts[0][1]
#         #mail = email.message_from_string(emailBody)
#         mail = email.message_from_bytes(emailBody)
#
#         for part in mail.walk():
#             #print (part)
#             if part.get_content_maintype() == 'multipart':
#                 # print part.as_string()
#                 continue
#             if part.get('Content-Disposition') is None:
#                 # print part.as_string()
#                 continue
#
#             fileName = part.get_filename()
#
#             if bool(fileName):
#                 filePath = os.path.join(detach_dir, 'attachments', fileName)
#                 if not os.path.isfile(filePath) :
#                     print (fileName)
#                     fp = open(filePath, 'wb')
#                     fp.write(part.get_payload(decode=True))
#                     fp.close()
#
#     imapSession.close()
#     imapSession.logout()
#
# except :
#     print ('Not able to download all attachments.')
#     time.sleep(3)