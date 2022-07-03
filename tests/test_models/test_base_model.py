#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class Test_Base_Model(unittest.TestCase):

    def test_types(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.time)
        self.assertIsInstance(model.updated_at, datetime.time)

    def test_id(self):
        model = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model.id, model2.id)
        self.assertEqual(len(model.id), 36)

    def test_time(self):
        model = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model.created_at, model2.created_at)
        self.assertNotEqual(model.updated_at, model2.updated_at)
