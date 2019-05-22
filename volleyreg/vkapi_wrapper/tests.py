from django.core.management import call_command
from django.test import TestCase

from vkapi_wrapper.wrapper import VkWrapper
from vkapi_wrapper.models import Keys


class KeysModelTests(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        Keys.objects.create(app_id='id_value', access_token='token_value',
                            group_id='group_id_value')

    def test_key_creation(self):
        app_keys = Keys.objects.get(id=1)
        self.assertEqual('id_value', app_keys.app_id)
        self.assertEqual('group_id_value', app_keys.group_id)
        self.assertEqual('token_value', app_keys.access_token)

    def test_str(self):
        app_keys = Keys.objects.get(id=1)
        self.assertEqual(app_keys.__str__(), 'keys for app id: id_value')


class VkWrapperTests(TestCase):
    """
    place 'test_auth.json' inside 'vkapi_wrapper' folder for running this test
    """
    def setUp(self):
        call_command('flush', '--noinput')
        import json
        with open('vkapi_wrapper/test_auth.json', 'r') as f:
            self.data = json.load(f)
        Keys.objects.create(app_id=self.data['VK_APP_ID'], access_token=self.data['VK_USER_ACCESS_TOKEN'],
                            group_id=self.data['VK_GROUP_ID_TEST'])

    def test_base_functional(self):
        from datetime import datetime as dt
        app_keys = Keys.objects.all().first()
        vk = VkWrapper(app_keys)
        comment_created = vk.comment_message('message for test, time: {}'.format(dt.today()))
        self.assertEqual(True, comment_created)
