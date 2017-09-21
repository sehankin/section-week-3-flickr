import json

# instead of f = open("sample_diction.json", "r"),
# which requires you to later include f.close(),
# you can do the following:
with open("sample_diction.json", "r") as f:
    json_text = f.read()
    flickr_dct = json.loads(json_text)

class Photo(object):
    def __init__(self, photo_dct):
        self.title = photo_dct["title"]["_content"]
        self.user = photo_dct["owner"]["username"]
        self.date = photo_dct["dates"]["taken"][:10]
        self.tags = []
        for tag in photo_dct["tags"]["tag"]:
            self.tags.append(tag["_content"])
        self.id = photo_dct["id"]
        self.url = photo_dct["urls"]["url"][0]["_content"]
        self.license = photo_dct["license"]

    def __str__(self):
        title_part = "A photo titled {}, ".format(self.title)
        user_part = "taken by user {} ".format(self.user)
        date_part = "on date {}, ".format(self.date)
        tags_part = "with tags {}".format(self.tags)
        all_parts = title_part + user_part + date_part + tags_part
        return all_parts

    def __repr__(self):
        return "ID: {}, URL: {}".format(self.id, self.url)

    def __contains__(self, input_str):
        return input_str in self.tags or input_str in self.title

# in sample_diction.json, the value of the key "photo"
# is the dictionary that we actually want
photo = Photo(flickr_dct["photo"])
print(photo)
print("YOLO" in photo)
