import json
from datetime import datetime as dt

import vk_api


class VkWrapper:
    def __init__(self, data_path='vkauth.json'):
        """
        :param data_path: string, path to json object with vk tokens (e.g. 'vkauth.json')
        :sets vk_session: vk session authorization
        :sets user_id: vk authorized user
        :sets vk: vk api wrapper
        """
        with open(data_path, 'r') as f:
            self.vk_data = json.load(f)
        self.vk_session = vk_api.VkApi(token=self.vk_data["VK_USER_ACCESS_TOKEN"])
        self.vk = self.vk_session.get_api()
        self.user_id = self.vk.users.get()[0]['id']
        self.wall = None
        self.message = {}

    def get_wall(self, group_id=None):
        """
        :param group_id: string, vk group id
        :return: vk wall
        """
        vk_group_id = group_id if group_id else self.vk_data['VK_GROUP_ID']
        self.wall = self.vk.wall.get(owner_id=vk_group_id)

    def get_message(self):
        """
        TODO: filter TODAY message
        TODO: pass list of filter string to find message. E.g. ['Запись на субботу', 'Запись на четверг', 'Время игры']
        :return: specified message from wall
        """
        messages = self.wall['items']
        message = [m for m in messages if not m.get('is_pinned', 0)][0]
        self.message['id'] = message['id']
        self.message['owner_id'] = message['owner_id']
        self.message['text'] = message['text']
        self.message['date'] = dt.fromtimestamp(message['date']).date()
        return self.message

    def comment_message(self, msg):
        """
        Write specified comment to message
        TODO: Do nothing, if no message specified or return error code
        :param msg: string. Text of comment
        """
        if self.message:
            self.vk.wall.createComment(owner_id=self.message['owner_id'], post_id=self.message['id'], message=msg)
        else:
            pass
