import http.client
import json
from PIL import Image
from io import BytesIO

class Mojang:

    def getUUID(username):
        conn = http.client.HTTPSConnection("api.mojang.com")
        payload = json.dumps([str(username)])
        print(payload)
        headers = {
            'Content-Type': "application/json"
            }
        conn.request("POST", "/profiles/minecraft", payload, headers)

        res = conn.getresponse()
        data = res.read()
        if 200 <= res.getcode() < 300:
            obj = json.loads(data.decode("utf-8"))
            return (obj, None)
        else: return (None, res.getcode())

    def getSkin(uuid):
        conn = http.client.HTTPSConnection("crafatar.com")
        conn.request("GET", "/skins/{}".format(uuid))

        res = conn.getresponse()
        data = res.read()

        im = Image.open(BytesIO(data))
        return im

def main():
    (uuid,err) = Mojang.getUUID("notch")
    print(uuid)
    im = Mojang.getSkin(uuid[0]['id'])
    print(im)

if __name__ == '__main__':
    main()
