from src.main.helpers.ensure_factory_uuid import ensureFactoryUuid


class User:
    def __init__(self, dataRaw, id) -> None:
        self.id = ensureFactoryUuid(id)
        self.name = dataRaw['name']
        self.email = dataRaw['email']
        self.meta = dataRaw['meta']
