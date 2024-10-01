
import os
import requests
from flask import Flask, redirect, request, jsonify

app = Flask(__name__)

CLIENT_ID = "693242086207520878"
CLIENT_SECRET = "ubti1la3F4LNnPDp-LUsu4an0dXmJaXM"
REDIRECT_URI = "http://localhost:5000/callback"
DISCORD_API_URL = "https://discord.com/api"
TOKEN_URL = f"{DISCORD_API_URL}/oauth2/token"
USER_INFO_URL = f"{DISCORD_API_URL}/users/@me"

user_data = {}  # Store user data globally

@app.route('/')
def home():
    return redirect(f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify")

@app.route('/callback')
def callback():
    code = request.args.get('code')

    # Step 1: Exchange code for access token
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(TOKEN_URL, data=data, headers=headers)
    
    # Step 2: Get the access token from the response
    token_json = response.json()
    access_token = token_json.get('access_token')

    if access_token:
        # Step 3: Use the access token to fetch user information
        headers = {'Authorization': f'Bearer {access_token}'}
        user_info_response = requests.get(USER_INFO_URL, headers=headers)
        global user_data
        user_data = user_info_response.json()  # Store user data globally
        
        print("User Info:", user_data)  # Print the user info in the console

        return "Authorization successful. You can now launch Rcheat app."
    else:
        return "Error getting access token."

@app.route('/get_user_info')
def get_user_info():
    # Return user data as JSON
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True)
