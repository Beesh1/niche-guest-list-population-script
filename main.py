import requests
import json

BASE_URL = "https://api.reservation.nichemagazine.me"
# BASE_URL = "http://127.0.0.1:8090"
ADMIN_EMAIL = "admin@progressiosolutions.com"
ADMIN_PASSWORD = "aiYai1Ooheoph2Ph"


def get_admin_token():
    auth_url = f"{BASE_URL}/api/admins/auth-with-password"
    response = requests.post(auth_url, json={
        "identity": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    })
    if response.status_code == 200:
        return response.json().get("token")
    else:
        print("Failed to authenticate. Status:", response.status_code)
        print("Response:", response.text)  # Print detailed error
        return None


def fetch_guests_with_invitations(token):
    custom_endpoint_url = f"{BASE_URL}/api/custom/guests_with_invitations"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(custom_endpoint_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)  # Print status code and error details
        print("Error details:", response.text)
        return None


def save_to_file(data, filename="result.txt"):
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))
    print(f"Data saved to {filename}")


def main():
    token = get_admin_token()
    if token:
        print(f"Token: {token}")
        data = fetch_guests_with_invitations(token)
        if data:
            save_to_file(data)
    else:
        print("Failed to retrieve admin token.")


if __name__ == "__main__":
    main()
