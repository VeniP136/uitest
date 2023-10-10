import requests
import config
import methods
domen = config.domen
chapter = "pricesSections"
Get_to = "title"


def Post(bug_tracker):
    payloadPost = {
        "title": config.test_create,
        "description": config.test_create
    }
    return methods.funPost(bug_tracker, chapter, payloadPost)


def IdPatch(bug_tracker, data):
    payloadPatch = {
        "title": config.test_change,
        "description": config.test_change
    }
    methods.funIdPatch(bug_tracker, data, chapter, payloadPatch)


def IdGet(bug_tracker, data):
    methods.funIdGet(bug_tracker, data, chapter)


def Get(bug_tracker, data, param=""):
    methods.funGet(bug_tracker, data, chapter, Get_to, param)


def IdDelete(bug_tracker, data, param=""):
    methods.funIdDelete(bug_tracker, data, chapter, param)
