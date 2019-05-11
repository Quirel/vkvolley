import json

import vk_api

with open('vkauth.json', 'r') as f:
    VK_DATA = json.load(f)


vk_session = vk_api.VkApi(token=VK_DATA["VK_USER_ACCESS_TOKEN"])
vk = vk_session.get_api()

# Get current user ID
user_id = vk.users.get()[0]['id']

# get wall of croup
wall = vk.wall.get(owner_id=VK_DATA['VK_GROUP_ID'])
messages = wall['items']
# get last not pinned message
msg = [m for m in messages if not m.get('is_pinned', 0)][0]
# create comment on specified wall message
# vk.wall.createComment(owner_id=msg['owner_id'], post_id=msg['id'], message='test comment')

