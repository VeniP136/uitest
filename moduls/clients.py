import requests
import config
import methods
domen = config.domen
chapter = "clients"
Get_to = "name"


def Post(bug_tracker):
    payloadPost = {
        "name": config.test_create,
        "fullName": "string",
        "email": "string",
        "telephone": "string",
        "contactFace": "string",
        "address": "string",
        "legalAddress": "string",
        "description": "string",
        "status": methods.Getparam("statuses"),
        "explanation": "string",
        "passport": "string",
        "INN": "string",
        "KPP": "string",
        "OGRN": "string",
        "OGRNIP": "string",
        "OKPO": "string",
        "BIK": "string",
        "correspondentAccount": "string",
        "bankName": "string",
        "checkingAccount": "string",
    }
    return methods.funPost(bug_tracker, chapter, payloadPost)


def IdPatch(bug_tracker, data):
    payloadPatch = {
        "name": config.test_change
    }
    methods.funIdPatch(bug_tracker, data, chapter, payloadPatch)


def IdGet(bug_tracker, data):
    methods.funIdGet(bug_tracker, data, chapter)


def Get(bug_tracker, data, param=""):
    methods.funGet(bug_tracker, data, chapter, Get_to, param)


def IdDelete(bug_tracker, data, param=""):
    methods.funIdDelete(bug_tracker, data, chapter, param)
