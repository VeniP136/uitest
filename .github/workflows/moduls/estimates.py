import requests
import config
import methods
domen = config.domen
chapter = "estimates"
Get_to = "name"


def Post(bug_tracker):
    payloadPost = {
        "name": "я люблю bananas",
        "number": 0,
        "objectId": methods.Getparam("objects"),
        "prices": [
            methods.Getparam("prices")
        ]
    }
    return methods.funPost(bug_tracker, chapter, payloadPost)


def IdPatch(bug_tracker, data):
    payloadPatch = {
        "name": "я люблю персики"
    }
    methods.funIdPatch(bug_tracker, data, chapter, payloadPatch)


def IdGet(bug_tracker, data):
    methods.funIdGet(bug_tracker, data, chapter)


def Get(bug_tracker, data, param=""):
    methods.funGet(bug_tracker, data, chapter, Get_to, param)


def IdDelete(bug_tracker, data, param=""):
    methods.funIdDelete(bug_tracker, data, chapter, param)
