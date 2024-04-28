import requests

def authenticate():
    url = 'http://www.auth.shafinahmed.me/authenticate'
    token = '123456' 

    headers = {'Authorization': token}
    response = requests.post(url, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        if data['success']:
            print("Authentication successful for user:", data['user_id'])
        else:
            print("Authentication failed:", data['message'])
    else:
        print("Error:", response.status_code)

if __name__ == '__main__':
    authenticate()
