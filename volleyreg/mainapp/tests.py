from django.test import TestCase

from mainapp.models import Player


class PlayerTests(TestCase):
    def setUp(self):
        Player.objects.create(name="Ilia", register_4=True)
        Player.objects.create(name="Alexandra", register_6=True)

    def test_name_content(self):
        player = Player.objects.get(id=1)
        self.assertEqual('Ilia', player.name)

    def test_register_4_content(self):
        player = Player.objects.get(id=1)
        self.assertEqual(True, player.register_4)
        player = Player.objects.get(id=2)
        self.assertEqual(False, player.register_4)

    def test_register_6_content(self):
        player = Player.objects.get(id=1)
        self.assertEqual(False, player.register_6)
        player = Player.objects.get(id=2)
        self.assertEqual(True, player.register_6)

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
