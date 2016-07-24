import datetime
import os
import json
import requests


def get_local_time(latitude, longitude, timestamp):

    url = "https://maps.googleapis.com/maps/api/timezone/json?location={latitude_data},\
            {longitude_data}&timestamp={timestamp_data}&key={api_key}".format(
        latitude_data=latitude,
        longitude_data=longitude,
        timestamp_data=timestamp,
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
    return timestamp_data.get("status")
