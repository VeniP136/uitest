import requests
import config
import methods
domen = config.domen
chapter = "materialsSections"
Get_to = "title"





def Post(bug_treker):
    payloadPost = {
        "title": "я люблю bananas",
        "description": "я люблю bananas",
        "group": methods.Getparam("materials")
    }
    return methods.funPost(bug_treker, chapter, payloadPost)


def IdPatch(bug_treker, data):
    payloadPatch = {
        "title": "я люблю персики",
        "description": "я люблю персики",
        "group": methods.Getparam("materials")
    }
    methods.funIdPatch(bug_treker, data, chapter, payloadPatch)


def Get(bug_treker, data, param=""):
    methods.funGet(bug_treker, data, chapter, Get_to, param)


def IdDelete(bug_treker, data, param=""):
    methods.funIdDelete(bug_treker, data, chapter, param)