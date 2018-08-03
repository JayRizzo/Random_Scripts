#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jeromie Kirchoff
# Created Date: Mon Aug 02 17:46:00 PDT 2018
# =============================================================================
# Answer for: https://stackoverflow.com/q/10147455/1896134
# =============================================================================
"""The Module Has Been Build for Sending Emails from your Gmail Account.

This is a full working example, just fill out the variables and
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
YOU MUST CREATE AND USE AN APP PASSWORD!!!!
https://support.google.com/accounts/answer/185833?hl=en
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

Otherwise when you run
jkirchoff$ python3 sendgmail.py

You get the message
Error: (535, b'5.7.8 Username and Password not accepted. Learn more at
5.7.8  https://support.google.com/mail/?p=BadCredentials
z90-h3zf2215251alemzk.85 - gsmtp')!

But if you have the correct Application password

jkirchoff$ python3 sendgmail.py
Email sent!

"""

# =============================================================================
# Imports
# =============================================================================
import smtplib

# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
gmail_user = 'THEFROM@gmail.com'
gmail_app_password = 'YOUR-GOOGLE-APPLICATION-PASSWORD!!!!'

# =============================================================================
# SET THE INFO ABOUT THE SAID EMAIL
# =============================================================================
sent_from = gmail_user
sent_to = ['THE-TO@gmail.com', 'THE-TO@gmail.com']
sent_subject = "Where are all my Robot Women at?"
sent_body = ("Hey, what's up? friend!\n\n"
             "I hope you have been well!\n"
             "\n"
             "Cheers,\n"
             "Jay\n")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

# =============================================================================
# SEND EMAIL OR DIE TRYING!!!
# Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
