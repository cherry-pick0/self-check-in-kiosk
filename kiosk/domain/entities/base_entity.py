class BaseEntity:
    """
    BaseEntity is a base for all other entities and states,
    that every entity needs an ID and other attributes.
    """

    _entity_id: int = 0

    def __init__(self, entity_id_value):
        self.entity_id = entity_id_value

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError

        self._entity_id = value
