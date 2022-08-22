from unittest import TestCase

from kiosk.domain.entities.base_entity import BaseEntity


class BaseEntityTests(TestCase):
    def test_base_entity(self):
        base_entity = BaseEntity(0)
        self.assertEqual(base_entity.entity_id, 0)

    def test_base_entity_invalid_id(self):
        with self.assertRaises(TypeError):
            BaseEntity("")
