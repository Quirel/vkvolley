import json

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
        self.message = None

    def get_wall(self):
        """
        :return: vk wall
        """
        return self.vk.wall.get(owner_id=self.vk_data['VK_GROUP_ID'])

    def get_message(self):
        """
        :return: specified message from wall
        """
        messages = self.get_wall()['items']
        message = [m for m in messages if not m.get('is_pinned', 0)][0]
        self.message = message
        return message

    def comment_message(self, msg):
        """
        Write specified comment to message
        Do nothing, if no message specified
        :param msg: string. Text of comment
        """
        if self.message:
            self.vk.wall.createComment(owner_id=self.vk_data['VK_GROUP_ID'], post_id=self.message['id'], message=msg)
        else:
            pass
