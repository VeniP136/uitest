import requests
import config
import methods
domen = config.domen
chapter = "providers"
Get_to = "name"





def Post(bug_treker):
    payloadPost = {
        "name": "я люблю bananas",
        "logo": "я люблю bananas"
    }
    return methods.funPost(bug_treker, chapter, payloadPost)


def IdPatch(bug_treker, data):
    payloadPatch = {
        "name": "я люблю персики",
        "logo": "я люблю персики"
    }
    methods.funIdPatch(bug_treker, data, chapter, payloadPatch)


def Get(bug_treker, data, param=""):
    methods.funGet(bug_treker, data, chapter, Get_to, param)


def IdDelete(bug_treker, data, param=""):
    methods.funIdDelete(bug_treker, data, chapter, param)
