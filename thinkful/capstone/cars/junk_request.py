__author__ = 'skamer'
import requests
style_id = 101421568
with open('testing_response', 'wb') as handle:
    url = 'https://api.edmunds.com/api/vehicle/v2/styles/{}/equipment?availability=standard&equipmentType=OTHER&fmt=json&api_key=b34wypjmb2fjf85asccqrv3z'.format(style_id)
    response = requests.get(url, stream=True)

    if not response.ok:
        # Something went wrong
        pass
    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)