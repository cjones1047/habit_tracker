import os
import dotenv
import requests

dotenv.load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

pixela_user_token = os.getenv("PIXELA_USER_TOKEN")

user_params = {
    "token": pixela_user_token,
    "username": "cjones1047",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
