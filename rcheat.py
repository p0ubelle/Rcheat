

import os
import requests
import subprocess



# Fetch user info from Flask server
def fetch_discord_user_info():
    try:
        response = requests.get("http://localhost:5000/get_user_info")
        if response.status_code == 200:
            user_info = response.json()
            return user_info
        else:
            print("Failed to get user info:", response.status_code)
    except Exception as e:
        print("Error fetching user info:", e)


user_info = fetch_discord_user_info()
if user_info:
    print("Discord Username:", user_info.get("username"))
    print("Discord ID:", user_info.get("id"))
    print("Discord Avatar:", user_info.get("avatar"))
    
    os.environ['USER_NAME'] = user_info.get("username")
    os.environ['USER_ID'] = user_info.get("id")
    os.environ['AVATAR_ID'] = user_info.get("avatar")


    subprocess.run(['python', 'main.py'])



"""
id': '403244404350910465', 'username': 'p0ubelle', 
'avatar': 'a_004f827f56cdaf09d3135f40956a71da', 'discriminator': '0', 
'public_flags': 256, 'flags': 256, 'banner': 'a_506617764414be61c00a3685e5f16fa5', 
'accent_color': 16777215, 'global_name': 'p0ubelle', 'avatar_decoration_data': None, 
'banner_color': '#ffffff', 'clan': None, 'mfa_enabled': True, 'locale': 'fr', 'premium_type': 2, 
'email': 'user@gmai.com', 'verified': True
"""
