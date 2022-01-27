# -*- coding: utf-8 -*-
"""
Created on Thu JAN 27 19:29:54 2022
@author: saqibullah
@email: saqibullah@gmail.com

"""

import smtplib , ssl
import yaml

def config_sections():
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    for section in cfg:
        print(section)

def get_configuration():
    with open("config.yml","r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg

def email(cfg, receiver_email):
    # Create a secure SSL context
    context = ssl.create_default_context()

    message = """\
        Subject: Hi there

        This message is sent from Python."""

    # Try to log in to server and send email
    try:
        sender_email = cfg['smtp_server']['user']
        sender_pass = cfg['smtp_server']['passwd']
        server = smtplib.SMTP_SSL(cfg['smtp_server']['host'], cfg['smtp_server']['port'])
        server.ehlo() # Can be omitted, To identify yourself to the server
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted, To identify yourself to the server
        server.login(sender_email, sender_pass)
        print("Yes Login ...")
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print("error :- ",e)
    finally:
        server.quit() 


# Call email function
cfg = get_configuration()
receiver_email = 'saqib@abc.com.pk'
email(cfg, receiver_email)

