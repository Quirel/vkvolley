import json

from django.test import TestCase

from vk_wrapper.wrapper import VkWrapper


class VkWrapperTests(TestCase):
    def setUp(self):
        pass

    def test_base_functional(self):
        from datetime import datetime as dt
        vk = VkWrapper()
        comment_created = vk.comment_message('message for test, time: {}'.format(dt.today()))
        self.assertEqual(True, comment_created)

