import requests
import config
import methods
domen = config.domen
chapter = "prices"
Get_to = "title"

payloadPost = {
    "title": "я люблю bananas",
    "measure": methods.Getparam("measures"),
    "cost": 100,
    "group": "string",
    "typeId": methods.Getparam("pricesTypes")
}
payloadPatch = {
    "title": "я люблю персики",
    "cost": 150
}


def Post(bug_treker):
    return methods.funPost(bug_treker, chapter, payloadPost)


def IdPatch(bug_treker, data):
    methods.funIdPatch(bug_treker, data, chapter, payloadPatch)


def Get(bug_treker, data, param=""):
    methods.funGet(bug_treker, data, chapter, Get_to, param)


def IdDelete(bug_treker, data, param=""):
    methods.funIdDelete(bug_treker, data, chapter, param)
