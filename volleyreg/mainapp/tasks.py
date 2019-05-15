from datetime import datetime as dt
# from django.db.models import Q
from background_task import background
from mainapp.models import Player
from mainapp.vk_wrapper import VkWrapper


@background()
def register_player():
    """
    if message today and string im message.text
    loop through players -> comment to message with player name
    """
    # players = Player.objects.filter(Q(register_4=True) | Q(register_6=True))
    players = None
    current_time = dt.today().time()
    if dt.today().weekday() == 2:
        players = Player.objects.filter(register_4=True).filter(registered=False)
        print(len(players), 'players need register')
    elif dt.today().weekday() == 4:
        players = Player.objects.filter(register_6=True).filter(registered=False)
        print(len(players), 'players need register')

    if players:
        vk = VkWrapper()
        vk.get_wall()
        msg = vk.get_message()
        if 'Запись на' in msg['text'] and 'Время игры' in msg['text'] and dt.today().date() == msg['date']:
            for player in players:
                if not player.registered:
                    vk.comment_message('+ {}'.format(player.name))
                    player.toggle_registered()
                    print(Player, 'registered')
                else:
                    print(Player, 'already registered')

            # TODO: stop task from repeat today
        else:
            print('{}: no message found'.format(current_time))
    else:
        print('{}: no players want to register or wrong day'.format(current_time))
