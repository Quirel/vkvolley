import json

import vk_api

with open('vkauth.json', 'r') as f:
    VK_KEYS = json.load(f)


vk_session = vk_api.VkApi(token=VK_KEYS["VK_USER_ACCESS_TOKEN"])
vk = vk_session.get_api()

# vk_session_service = vk_api.VkApi(app_id=int(VK_KEYS["VK_APP_ID"]), token=VK_KEYS["VK_APP_SERVICE"])
# vk_service = vk_session_service.get_api()

# Get current user ID
user_id = vk.users.get()[0]['id']

# wall = vk.wall.get(domain='volley19')
# print(wall)

# msg = vk_service.notifications.sendMessage(user_ids=user_id, message="test msg")
# print(msg)


