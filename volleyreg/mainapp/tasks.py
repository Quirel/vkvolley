from datetime import datetime as dt
# from django.db.models import Q
from background_task import background
from mainapp.models import Player
from vkapi_wrapper.wrapper import VkWrapper
from vkapi_wrapper.models import Keys


@background()
def register_player(key_id):
    """
    TODO: full rework
    if message today and string im message.text
    loop through players -> comment to message with player name
    """
    current_time = dt.today().time()
    print('------------------------------')
    print('------------------------------')
    print('Task running: {}'.format(current_time))
    # players = Player.objects.filter(Q(register_4=True) | Q(register_6=True))
    players = Player.objects.all()
    # if dt.today().weekday() == 2:
    #     players = Player.objects.filter(register_4=True).filter(registered=False)
    #     print(len(players), 'players need register')
    # elif dt.today().weekday() == 4:
    #     players = Player.objects.filter(register_6=True).filter(registered=False)
    #     print(len(players), 'players need register')

    # if players:
    vk = VkWrapper(Keys.objects.get(id=key_id))
    # id=1 for testing, id=2 - real group
    msg = vk.get_message()
    if 'Запись на' in msg['text'] and 'Время игры' in msg['text'] and dt.today().date() == msg['date']:
        for player in players:
            if not player.registered:
                vk.comment_message('+ {}'.format(player.name))
                player.toggle_registered()
                print(player, 'registered')
            else:
                print(player, 'already registered')

        # TODO: stop task from repeat today
    else:
        print('{}: no message found'.format(current_time))
    # else:
    #     print('{}: no players want to register or wrong day'.format(current_time))
