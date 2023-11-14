import requests

TOKEN = ",mblvsdionhoivdsipoj"
USERNAME = "brakomister"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Gym Habit",
    "unit": "minutes",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

endpoint = "https://pixe.la/v1/users/brakomister/graphs/graph1"
params = {
    "date": "20230323",
    "quantity": "60",
}
response = requests.post(url=endpoint, json=params, headers=headers)
print(response.text)