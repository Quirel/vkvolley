from datetime import datetime as dt

from django.core.management import call_command
from django.test import TestCase

from mainapp.models import Player


class PlayerTests(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        Player.objects.create(name="Ilia", date=dt.today().date())

    def test_name_content(self):
        player = Player.objects.get(id=1)
        self.assertEqual('Ilia', player.name)

    def test_get_registered(self):
        player = Player.objects.get(id=1)
        self.assertEqual(False, player.registered)
        player.toggle_registered()
        self.assertEqual(True, player.registered)
        player.toggle_registered()
        self.assertEqual(False, player.registered)

    def test_str(self):
        player = Player.objects.get(id=1)
        self.assertEqual(player.name, player.__str__())
