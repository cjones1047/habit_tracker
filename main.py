import os
import dotenv
import requests

dotenv.load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

pixela_user_token = os.getenv("PIXELA_USER_TOKEN")

pixela_username = "cjones1047"

user_params = {
    "token": pixela_user_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs"

create_graph_headers = {
    "X-USER-TOKEN": pixela_user_token
}

create_graph_json = {
    "id": "cycling1",
    "name": "Cycling",
    "unit": "miles",
    "type": "float",
    "color": "sora"
}

create_graph_response = requests.post(url=graph_endpoint, headers=create_graph_headers, json=create_graph_json)
print(create_graph_response.text)
