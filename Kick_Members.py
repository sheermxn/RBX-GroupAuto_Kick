# made by ironside#2823
# put your .ROBLOSECURITY cookie in variable "cookie"

import requests
from os import system
from time import sleep

cookie = {
    ".ROBLOSECURITY": ''
}

header = {
    "X-CSRF-TOKEN": ""
}

def Delete_All_Members():
    your_group_id = int(input('Group ID --> '))
    rolelist = {}
    try:
        roles = requests.get(f'https://groups.roblox.com/v1/groups/{your_group_id}/roles').json()
        for v in roles['roles']:
            roleid = v['id']
            rolename = v['name']
            if rolename != 'Guest':
                rolelist[rolename] = roleid
    except:
        system('clear')
        print(f'Error - Status Code: {roles.status_code}')
        Delete_All_Members()
    system('clear')
    for key in rolelist:
        print(f'{key} = {rolelist[key]}')
    roleselect = int(input('\nRole ID: '))
    if not header["X-CSRF-TOKEN"]:
        r = requests.post(f"https://auth.roblox.com/v2/logout", cookies=cookie)
        header["X-CSRF-TOKEN"] = r.headers['x-csrf-token']
    #
    users = requests.get(f'https://groups.roblox.com/v1/groups/{your_group_id}/roles/{roleselect}/users?limit=50')
    table = users.json()

    try:
        for v in table["data"]:
            sleep(1.5)
            name = v["username"]
            userid = v["userId"]
            r = requests.delete(
                f"https://groups.roblox.com/v1/groups/{your_group_id}/users/{int(userid)}",
                cookies=cookie,
                headers=header
            )
            if r.status_code == 200:
                print(f'{name} kicked.')
            else:
                print(f'Error - Status Code: {r.status_code}')
    except:
        system('clear')
        print('Error.')
        Delete_All_Members()

if __name__ == '__main__':
    Delete_All_Members()
