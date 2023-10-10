from moduls import materialsSections, materials, pricesSections, pricesTypes, prices, measures, criteriaSections, criteria, providers, objects, estimates, clients, statuses
import methods
import config
import requests
import json
domen = config.domen


class bug_tracker:
    x = ""


def funmaterialsSections():
    try:
        data = materialsSections.Post(bug_tracker)
        materialsSections.IdGet(bug_tracker, data)
        materialsSections.Get(bug_tracker, data, config.test_create)
        materialsSections.IdPatch(bug_tracker, data)
        materialsSections.Get(bug_tracker, data, config.test_change)
        materialsSections.IdDelete(bug_tracker, data)
        materialsSections.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка.
        materialsSections.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "materialsSections попытался крашнуть"
        print("materialsSections попытался крашнуть")


def funmaterials():
    try:
        data = materials.Post(bug_tracker)
        materials.IdGet(bug_tracker, data)
        materials.Get(bug_tracker, data, config.test_create)
        materials.IdPatch(bug_tracker, data)
        materials.Get(bug_tracker, data, config.test_change)
        materials.IdDelete(bug_tracker, data)
        materials.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        materials.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "materials попытался крашнуть"
        print("materials попытался крашнуть")


def funpricesSections():
    try:
        data = pricesSections.Post(bug_tracker)
        pricesSections.IdGet(bug_tracker, data)
        pricesSections.Get(bug_tracker, data, config.test_create)
        pricesSections.IdPatch(bug_tracker, data)
        pricesSections.Get(bug_tracker, data, config.test_change)
        pricesSections.IdDelete(bug_tracker, data)
        pricesSections.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        pricesSections.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "pricesSections попытался крашнуть"
        print("pricesSections попытался крашнуть")


def funpricesTypes():
    try:
        data = pricesTypes.Post(bug_tracker)
        pricesTypes.IdGet(bug_tracker, data)
        pricesTypes.Get(bug_tracker, data, config.test_create)
        pricesTypes.IdPatch(bug_tracker, data)
        pricesTypes.Get(bug_tracker, data, config.test_change)
        pricesTypes.IdDelete(bug_tracker, data)
        pricesTypes.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        pricesTypes.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "pricesTypes попытался крашнуть"
        print("pricesTypes попытался крашнуть")


def funprices():
    try:
        data = prices.Post(bug_tracker)
        prices.IdGet(bug_tracker, data)
        prices.Get(bug_tracker, data, config.test_create)
        prices.IdPatch(bug_tracker, data)
        prices.Get(bug_tracker, data, config.test_change)
        prices.IdDelete(bug_tracker, data)
        prices.Get(bug_tracker, data)
        # prices.IdDelete(bug_tracker, data, "удаление 0 записей") #"удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "prices попытался крашнуть"
        print("prices попытался крашнуть")


def funmeasures():
    try:
        data = measures.Post(bug_tracker)
        measures.IdGet(bug_tracker, data)
        measures.Get(bug_tracker, data, config.test_create)
        measures.IdPatch(bug_tracker, data)
        measures.Get(bug_tracker, data, config.test_change)
        measures.IdDelete(bug_tracker, data)
        measures.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        measures.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "measures попытался крашнуть"
        print("measures попытался крашнуть")


def funcriteriaSections():
    try:
        data = criteriaSections.Post(bug_tracker)
        criteriaSections.IdGet(bug_tracker, data)
        criteriaSections.Get(bug_tracker, data, config.test_create)
        criteriaSections.IdPatch(bug_tracker, data)
        criteriaSections.Get(bug_tracker, data, config.test_change)
        criteriaSections.IdDelete(bug_tracker, data)
        criteriaSections.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        criteriaSections.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "criteriaSections попытался крашнуть"
        print("criteriaSections попытался крашнуть")


def funcriteria():
    try:
        data = criteria.Post(bug_tracker)
        criteria.IdGet(bug_tracker, data)
        criteria.Get(bug_tracker, data, config.test_create)
        criteria.IdPatch(bug_tracker, data)
        criteria.Get(bug_tracker, data, config.test_change)
        criteria.IdDelete(bug_tracker, data)
        criteria.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        criteria.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "criteria попытался крашнуть"
        print("criteria попытался крашнуть")


def funproviders():
    try:
        data = providers.Post(bug_tracker)
        providers.IdGet(bug_tracker, data)
        providers.Get(bug_tracker, data, config.test_create)
        providers.IdPatch(bug_tracker, data)
        providers.Get(bug_tracker, data, config.test_change)
        providers.IdDelete(bug_tracker, data)
        providers.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка
        providers.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "providers попытался крашнуть"
        print("providers попытался крашнуть")


def funobjects():
    try:
        data = objects.Post(bug_tracker)
        objects.IdGet(bug_tracker, data)
        objects.Get(bug_tracker, data, config.test_create)
        objects.IdPatch(bug_tracker, data)
        objects.Get(bug_tracker, data, config.test_change)
        objects.IdDelete(bug_tracker, data)
        objects.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка.
        objects.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "objects попытался крашнуть"
        print("objects попытался крашнуть")


def funestimates():
    try:
        data = estimates.Post(bug_tracker)
        estimates.IdGet(bug_tracker, data)
        estimates.Get(bug_tracker, data, config.test_create)
        estimates.IdPatch(bug_tracker, data)
        estimates.Get(bug_tracker, data, config.test_change)
        estimates.IdDelete(bug_tracker, data)
        estimates.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка.
        estimates.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "estimates попытался крашнуть"
        print("estimates попытался крашнуть")


def funclients():
    try:
        data = clients.Post(bug_tracker)
        clients.IdGet(bug_tracker, data)
        clients.Get(bug_tracker, data, config.test_create)
        clients.IdPatch(bug_tracker, data)
        clients.Get(bug_tracker, data, config.test_change)
        clients.IdDelete(bug_tracker, data)
        clients.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка.
        clients.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "clients попытался крашнуть"
        print("clients попытался крашнуть")


def funstatuses():
    try:
        data = statuses.Post(bug_tracker)
        statuses.IdGet(bug_tracker, data)
        statuses.Get(bug_tracker, data, config.test_create)
        statuses.IdPatch(bug_tracker, data)
        statuses.Get(bug_tracker, data, config.test_change)
        statuses.IdDelete(bug_tracker, data)
        statuses.Get(bug_tracker, data)
        # "удаление 0 записей" не защищает от удаления, это значит что удаление 0 записей не ошибка.
        statuses.IdDelete(bug_tracker, data, "удаление 0 записей")
        print("")
        print("")
        print("")
    except:
        bug_tracker.x = bug_tracker.x + "statuses попытался крашнуть"
        print("statuses попытался крашнуть")


print("хотите проверить все эндпоинты? y/n")
question = "y"  # input()


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
    funobjects()
    funestimates()
    funclients()
elif question == "n":
    print("введите блоки которые хотите проверить(например 1236)\n")
    print("1 - materialsSections")
    print("2 - materials")
    print("3 - pricesSections")
    print("4 - pricesTypes")
    print("5 - prices")
    print("6 - measures")
    print("7 - criteriaSections")
    print("8 - criteria")
    print("9 - providers")
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

    print("введите блоки 2 группы которые хотите проверить(например 1236)\n")
    print("1 - objects")
    print("2 - estimates")
    print("3 - clients")
    # print("4 - pricesTypes")
    # print("5 - prices")
    # print("6 - measures")
    # print("7 - criteriaSections")
    # print("8 - criteria")
    # print("9 - providers")
    question = input()
    if "1" in question:
        funobjects()
    if "2" in question:
        funestimates()
    if "3" in question:
        funclients()
    # if "4" in question:
    #     funpricesTypes()
    # if "5" in question:
    #     funprices()
    # if "6" in question:
    #     funmeasures()
    # if "7" in question:
    #     funcriteriaSections()
    # if "8" in question:
    #     funcriteria()
    # if "9" in question:
    #     funproviders()
else:
    print("некорректный ввод")

if bug_tracker.x == "":
    print("Success")
else:
    print("ошибки в " + bug_tracker.x)
    input()
