import datetime
import os
import json
import requests


def get_local_time(latitude, longitude, timestamp):

    url = "https://maps.googleapis.com/maps/api/timezone/json?location={latitude},\
            {longitude}&timestamp={timestamp}&key={api_key}".format(
        latitude=latitude,
        longitude=longitude,
        timestamp=timestamp,
        api_key=os.environ.get("GOOGLE_API_KEY"),
    )

    response = requests.get(url)

    timestamp_data = json.loads(response.text)

    if timestamp_data.get("status") == "OK":
        rawOffset = timestamp_data.get("rawOffset")
        dstOffset = timestamp_data.get("dstOffset")

        result_timestamp = rawOffset + dstOffset + float(timestamp)

        result_date = datetime.datetime.fromtimestamp(result_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        return result_date
