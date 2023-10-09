import requests
import config
import methods

domen = config.domen


def Getparam(type):
    url = f'{domen}/{type}'
    params = {}
    response = requests.get(url, params=params)
    response = response.json()
    # print(response)
    try:
        return response[0]["_id"]
    except:
        return response["data"][0]["_id"]


def funPost(bug_tracker, chapter, payloadPost):
    url = f'{domen}/{chapter}'
    headers = {}
    payload = payloadPost
    # print(payload)
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    try:
        data = data[0]
    except:
        data = data
    print(data)
    if response.status_code == 201:
        print(
            f"{f'Post'.ljust(10)}{ f'Success {chapter}'.ljust(40)} {methods.timer(response)}")
    else:
        bug_tracker.x = bug_tracker.x + f"{chapter}Post "
        print(
            f"{f'Post'.ljust(10)}{f'{chapter} не работает'.ljust(40)} {methods.timer(response)}")
    return data


def funIdGet(bug_tracker, data, chapter):
    url = f'{domen}/{chapter}/{data["_id"]}'
    response = requests.get(url, params={})
    data = response.json()
    if response.status_code == 200:
        print(
            f"{f'Get'.ljust(10)}{f'Success {chapter}'.ljust(40)} {methods.timer(response)}")
    else:
        bug_tracker.x = bug_tracker.x + f"{chapter}IdGet "
        print(
            f"{f'Get'.ljust(10)}{f'{chapter}Id не работает'.ljust(40)} {methods.timer(response)}")


def funIdPatch(bug_tracker, data, chapter, payloadPatch):
    # print(data)
    url = f'{domen}/{chapter}/{data["_id"]}'
    headers = {}
    payload = payloadPatch
    response = requests.patch(url, headers=headers, json=payload)
    data = response.json()
    if response.status_code == 200:
        print(
            f"{f'Patch'.ljust(10)}{f'Success {chapter}Id'.ljust(40)} {methods.timer(response)}")
    else:
        bug_tracker.x = bug_tracker.x + f"{chapter}IdPatch "
        print(
            f"{f'Patch'.ljust(10)}{f'{chapter}Id не работает'.ljust(40)} {methods.timer(response)}")


def funGet(bug_tracker, data, chapter, Get_to, param=""):
    url = f'{domen}/{chapter}'
    response = requests.get(url, params={})
    data = response.json()
    # print(data)
    try:
        data = data["data"]
    except:
        data = data
    found = any(item[Get_to] == param for item in data)
    if param == "":
        if found:
            bug_tracker.x = bug_tracker.x + f"{chapter}Get "
            print(
                f"{f'Get'.ljust(10)}{f'{chapter}IdDelete не удалил'.ljust(40)} {methods.timer(response)}")
        else:
            print(
                f"{f'Get'.ljust(10)}{f'Success {chapter}'.ljust(40)} {methods.timer(response)}")
    else:
        if found:
            print(
                f"{f'Get'.ljust(10)}{f'Success {chapter}'.ljust(40)} {methods.timer(response)}")
        else:
            bug_tracker.x = bug_tracker.x + f"{chapter}Get "
            print(
                f"{f'Get'.ljust(10)}{f'{chapter} не работает'.ljust(40)} {methods.timer(response)}")


def funIdDelete(bug_tracker, data, chapter, param=""):
    url = f'{domen}/{chapter}/{data["_id"]}'
    params = ""
    response = requests.delete(url, params=params)
    data = response.json()
    # print(response)
    if response.status_code == 200:
        if ((data["deletedCount"] == 0) and (param != "удаление 0 записей")):
            bug_tracker.x = bug_tracker.x + f"{chapter}IdDelete "
            print(
                f"{f'Delete'.ljust(10)}{f'{chapter}Id ничего не удалил'.ljust(40)} {methods.timer(response)}")
        else:
            print(
                f"{f'Delete'.ljust(10)}{f'Success {chapter}Id'.ljust(40)} {methods.timer(response)}")
    else:
        bug_tracker.x = bug_tracker.x + f"{chapter}IdDelete "
        print(
            f"{f'Delete'.ljust(10)}{f'{chapter}Id не работает'.ljust(40)} {methods.timer(response)}")


def timer(response):
    return (f" тест занял {response.elapsed.total_seconds():0.2f} секунд")
