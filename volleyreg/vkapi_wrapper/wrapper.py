import json
from datetime import datetime as dt

import vk_api


class VkWrapper:
    def __init__(self, app_keys):
        self.access_token = app_keys.access_token
        self.app_id = app_keys.app_id
        self.group_id = app_keys.group_id
        self.vk_session = vk_api.VkApi(token=self.access_token)
        self.vk = self.vk_session.get_api()
        self.user_id = self.vk.users.get()[0]['id']
        self.wall = None
        self.message = {}

    def get_wall(self):
        """
        :return: vk wall
        """
        self.wall = self.vk.wall.get(owner_id=self.group_id)

    def get_message(self):
        """
        :return: last not pinned message from wall
        """
        if not self.wall:
            self.get_wall()
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
        TODO: Do nothing, if nomessage specified or return error code
        :param msg: string. Text of comment
        """
        if not self.message:
            self.get_message()
        self.vk.wall.createComment(owner_id=self.message['owner_id'], post_id=self.message['id'], message=msg)
        return True
