

import requests

response = requests.get("https://gist.githubusercontent.com/p0ubelle/f3484841df07f230c4b4f2fed50ceba5/raw/2bc9fe7454ff00be8eef1d39a36d441fb529397b/rcheat_version.txt")
latest_version = response.text.strip()

print(latest_version)