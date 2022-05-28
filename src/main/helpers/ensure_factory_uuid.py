from src.main.helpers.factory_uuid import factoryUuid


def ensureFactoryUuid(id):
    if (type(id) is str):
        return id
    return factoryUuid()
