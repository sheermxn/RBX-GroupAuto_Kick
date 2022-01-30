# made by ironside#2823
# put your .ROBLOSECURITY cookie in variable "cookie"

import requests
from os import system
from time import sleep

cookie = {
    ".ROBLOSECURITY": '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A50CEFEB46E7806D3638A9D5CBF94BA5440C96F9A0CD74C99DB157E8695F6C3C383A7BECA7F2E7A19B2DB243A79FE6281EBA00A42C1933193A7EAA8BF17B3035C173DA96CB8A9BD4076CE158ECFB6EEF8077286EF1D016B87777298CFF2071EC3EF85249BFB3056A44E5DE929AA6A3C8D74F6792A4537D9801D9332390A51E9B3BB6AB36A233F96848F33BE4C8EA5862D625A9E44730C73B69789F1BF41BDC0FF2D602BD52F04F016EAFB2394C840F3864BEB06146876138462A574B1B1EA61C68966D41CC16BA6776DF0A0276333B4544D21F67579FBA838AC495A875FDA399D926589A281F5ABEA776BD8636F0B6F4A407396F9CAEAE7B6EF30EDB2A66E4FA44BA2A13A4DECFAC9CFB1182A7A4D33DB7CF60984C7A6F8FD538BB3A3DC125C52791E7692D74684C267EABD4B09A8C2862A994BA87FA8D3BE89C059D98FB43CFEC2F603F'
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