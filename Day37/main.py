import requests

USERNAME = "negar"
TOKEN = "xxxxxxxxxx"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user account:
# response = requests.post(url=pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Habit Tracker",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create Graph:
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data= {
    "date": "20231022",
    "quantity": "60"
}

response =requests.post(url=pixel_creation_endpoint, json= pixel_data, headers=headers)
print(response.text)