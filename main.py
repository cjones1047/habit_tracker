import os
import dotenv
import requests
import datetime

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

pixela_headers = {
    "X-USER-TOKEN": pixela_user_token
}

create_graph_json = {
    "id": "cycling1",
    "name": "Cycling",
    "unit": "miles",
    "type": "float",
    "color": "sora"
}

# create_graph_response = requests.post(url=graph_endpoint, headers=pixela_headers, json=create_graph_json)
# print(create_graph_response.text)

create_pixel_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs/{create_graph_json['id']}"

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

create_pixel_json = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "15"
}

# create_pixel_response = requests.post(url=create_pixel_endpoint, headers=pixela_headers, json=create_pixel_json)
# print(create_pixel_response.text)

update_pixel_endpoint = f"{create_pixel_endpoint}/{yesterday.strftime('%Y%m%d')}"

update_pixel_json = {
    "quantity": "5"
}

# update_pixel_response = requests.put(url=update_pixel_endpoint, headers=pixela_headers, json=update_pixel_json)
# print(update_pixel_response.text)

delete_pixel_response = requests.delete(url=update_pixel_endpoint, headers=pixela_headers)
print(delete_pixel_response.text)
