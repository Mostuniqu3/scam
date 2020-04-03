import requests
import os
import random
import string
import json
import random
import math

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://dofus-event.com/france/dofus/MMORPG/temporis/connexion.php'

names = json.loads(open('names.json').read())
emails = ["google.com","orange.fr","free.fr","yahoo.com","gmail.com","outlook.fr","hotmail.com"]

while True :
    for name in names:
        for email in emails:
            name_extra = ''.join(random.choice(string.digits))
            username = name.lower() + name_extra + '@' + email
            x = math.floor(random.uniform(4,25))
            password = ''.join(random.choice(chars) for i in range(x))

            requests.post(url, allow_redirects=False, data={
                'pseudo': username,
                'mdp': password
            })

            print ('Sending username ' + username + ' and password ' + password)
