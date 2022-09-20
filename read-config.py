import requests

try:
    response = requests.get(url="https://127.0.0.1:8444/config",verify=False)
    config = response.json()
except:
    print("Unable to connect")
    exit(1)

config = config.get("config")
config = config.replace("~","")

file = open("kong-conf.yml","w")
file.write(config)
print("kong-conf.yml file is created.")