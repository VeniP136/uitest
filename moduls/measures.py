import requests
import config
import methods
domen = config.domen
chapter = "measures"
Get_to = "fullName"





def Post(bug_treker):
    payloadPost = {
        "name": "bananas",
        "fullName": "я люблю bananas"
    }
    return methods.funPost(bug_treker, chapter, payloadPost)


def IdPatch(bug_treker, data):
    payloadPatch = {
        "name": "персики",
        "fullName": "я люблю персики"
    }
    methods.funIdPatch(bug_treker, data, chapter, payloadPatch)


def Get(bug_treker, data, param=""):
    methods.funGet(bug_treker, data, chapter, Get_to, param)


def IdDelete(bug_treker, data, param=""):
    methods.funIdDelete(bug_treker, data, chapter, param)
