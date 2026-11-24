from webexpythonsdk import WebexAPI

access_token = "PLAK_HIER_JE_TOKEN"
api = WebexAPI(access_token=access_token)

demo_rooms = [room for room in api.rooms.list() if "GROUP_" in room.title]
for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)
