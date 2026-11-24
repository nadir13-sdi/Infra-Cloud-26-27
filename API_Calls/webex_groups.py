import requests

access_token = "PLAK_HIER_JE_TOKEN"
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
url_rooms = "https://webexapis.com/v1/rooms"
url_members = "https://webexapis.com/v1/memberships"

groups_struc = {
    "groups": [
        {"group": {"group_id": "G1", "group_name": "GROUP_NADIR_A",
                   "members": [{"person_id": "P-1", "person_name": "Lid 1", "email": "lid1@student.be"},
                               {"person_id": "P-2", "person_name": "Lid 2", "email": "lid2@student.be"}]}},
        {"group": {"group_id": "G2", "group_name": "GROUP_NADIR_B",
                   "members": [{"person_id": "P-3", "person_name": "Lid 3", "email": "lid3@student.be"},
                               {"person_id": "P-4", "person_name": "Lid 4", "email": "lid4@student.be"}]}},
    ]
}

for rec in groups_struc["groups"]:
    naam = rec["group"]["group_name"]
    print("Creating ... " + naam)
    res_space = requests.post(url_rooms, headers=headers, json={"title": naam})
    if res_space.status_code < 300:
        room_id = res_space.json()["id"]
        for mbr in rec["group"]["members"]:
            payload = {"roomId": room_id, "personEmail": mbr["email"]}
            res_member = requests.post(url_members, headers=headers, json=payload)
            print("   lid", mbr["email"], "status", res_member.status_code)
    else:
        print("   space niet gemaakt:", res_space.status_code, res_space.text)
