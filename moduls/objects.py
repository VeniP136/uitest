import requests
import config
import methods
domen = config.domen
chapter = "objects"
Get_to = "name"


def Post(bug_tracker):
    payloadPost = {
        "name": "я люблю bananas",
        "description": "я люблю bananas",
        "number": 4,
        "date": "2019-10-09T06:20:48.126Z",
        "address": "я люблю bananas",
        "client": methods.Getparam("clients")
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
