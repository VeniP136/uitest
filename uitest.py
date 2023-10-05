from moduls import materialsSections, materials, pricesSections, pricesTypes, prices, measures, criteriaSections, criteria, providers
import methods
import config
import requests
import json
domen = config.domen


class bug_treker:
    x = ""


def funmaterialsSections():
    try:
        data = materialsSections.Post(bug_treker)
        materialsSections.Get(bug_treker, data, "я люблю bananas")
        materialsSections.IdPatch(bug_treker, data)
        materialsSections.Get(bug_treker, data, "я люблю персики")
        materialsSections.IdDelete(bug_treker, data)
        materialsSections.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        materialsSections.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funmaterialsSections попытался крашнуть")


def funmaterials():
    try:
        data = materials.Post(bug_treker)
        materials.Get(bug_treker, data, "я люблю bananas")
        materials.IdPatch(bug_treker, data)
        materials.Get(bug_treker, data, "я люблю персики")
        materials.IdDelete(bug_treker, data)
        materials.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        materials.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funmaterials попытался крашнуть")


def funpricesSections():
    try:
        data = pricesSections.Post(bug_treker)
        pricesSections.Get(bug_treker, data, "я люблю bananas")
        pricesSections.IdPatch(bug_treker, data)
        pricesSections.Get(bug_treker, data, "я люблю персики")
        pricesSections.IdDelete(bug_treker, data)
        pricesSections.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        pricesSections.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funpricesSections попытался крашнуть")


def funpricesTypes():
    try:
        data = pricesTypes.Post(bug_treker)
        pricesTypes.Get(bug_treker, data, "я люблю bananas")
        pricesTypes.IdPatch(bug_treker, data)
        pricesTypes.Get(bug_treker, data, "я люблю персики")
        pricesTypes.IdDelete(bug_treker, data)
        pricesTypes.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        pricesTypes.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funpricesTypes попытался крашнуть")


def funprices():
    try:
        data = prices.Post(bug_treker)
        prices.Get(bug_treker, data, "я люблю bananas")
        prices.IdPatch(bug_treker, data)
        prices.Get(bug_treker, data, "я люблю персики")
        prices.IdDelete(bug_treker, data)
        prices.Get(bug_treker, data)
        # prices.IdDelete(bug_treker, data, "удаление 0 записей") #"удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        print("")
        print("")
        print("")
    except:
        print("funprices попытался крашнуть")


def funmeasures():
    try:
        data = measures.Post(bug_treker)
        measures.Get(bug_treker, data, "я люблю bananas")
        measures.IdPatch(bug_treker, data)
        measures.Get(bug_treker, data, "я люблю персики")
        measures.IdDelete(bug_treker, data)
        measures.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        measures.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funmeasures попытался крашнуть")


def funcriteriaSections():
    try:
        data = criteriaSections.Post(bug_treker)
        criteriaSections.Get(bug_treker, data, "я люблю bananas")
        criteriaSections.IdPatch(bug_treker, data)
        criteriaSections.Get(bug_treker, data, "я люблю персики")
        criteriaSections.IdDelete(bug_treker, data)
        criteriaSections.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        criteriaSections.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funcriteriaSections попытался крашнуть")


def funcriteria():
    try:
        data = criteria.Post(bug_treker)
        criteria.Get(bug_treker, data, "я люблю bananas")
        criteria.IdPatch(bug_treker, data)
        criteria.Get(bug_treker, data, "я люблю персики")
        criteria.IdDelete(bug_treker, data)
        criteria.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        criteria.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funcriteriaSections попытался крашнуть")


def funproviders():
    try:
        data = providers.Post(bug_treker)
        providers.Get(bug_treker, data, "я люблю bananas")
        providers.IdPatch(bug_treker, data)
        providers.Get(bug_treker, data, "я люблю персики")
        providers.IdDelete(bug_treker, data)
        providers.Get(bug_treker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        providers.IdDelete(bug_treker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        print("funcriteriaSections попытался крашнуть")


print("хотите проверить все эндпоинты? y/n")
question = input()
if question == "y":
    funmaterialsSections()
    funmaterials()
    funpricesSections()
    funpricesTypes()
    funprices()
    funmeasures()
    funcriteriaSections()
    funcriteria()
    funproviders()
elif question == "n":
    print("введите блоки которые хотите проверить(например 1236)\n")
    print("1 - materialsSections")
    print("2 - funmaterials")
    print("3 - funpricesTypes")
    print("4 - funpricesTypes")
    print("5 - funprices")
    print("6 - funmeasures")
    print("7 - funcriteriaSections")
    print("8 - funcriteria")
    print("9 - funproviders")
    question = input()
    if "1" in question:
        funmaterialsSections()
    if "2" in question:
        funmaterials()
    if "3" in question:
        funpricesSections()
    if "4" in question:
        funpricesTypes()
    if "5" in question:
        funprices()
    if "6" in question:
        funmeasures()
    if "7" in question:
        funcriteriaSections()
    if "8" in question:
        funcriteria()
    if "9" in question:
        funproviders()
else:
    print("некорректный ввод")

if bug_treker.x == "":
    print("Success")
else:
    print("ошибки в " + bug_treker.x)
input()
