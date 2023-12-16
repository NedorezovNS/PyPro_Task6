import requests


def ya_folder_create(folder_name):
    with open('ya_token.txt', 'r') as f:
        ya_token = f.read().strip()
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': folder_name,
            'overwrite': 'true'
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': ya_token
        }
        folder = requests.put(url=url, headers=headers, params=params)
        if folder.status_code == 201:
            print(f'Folder "{folder_name}" successfully created')
        elif folder.status_code == 409:
            print(f'Folder "{folder_name}" already exist')
        return folder.status_code
