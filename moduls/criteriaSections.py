import requests, config, methods
domen = config.domen
chapter = "criteriaSections"
Get_to = "title"
  
payloadPost ={
    "title": "я люблю bananas",
    "description": "я люблю bananas"
}
payloadPatch ={
    "title": "я люблю персики",
    "description": "я люблю персики"
}

def Post(bug_treker):
    return methods.funPost(bug_treker, chapter, payloadPost)

def IdPatch(bug_treker, data):
    methods.funIdPatch(bug_treker, data, chapter, payloadPatch)
    
def Get(bug_treker, data, param=""):
    methods.funGet(bug_treker, data, chapter, Get_to, param)
    
def IdDelete(bug_treker, data, param=""):
    methods.funIdDelete(bug_treker, data, chapter, param)