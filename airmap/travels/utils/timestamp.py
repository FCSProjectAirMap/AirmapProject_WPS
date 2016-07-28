import datetime


def get_local_time(timestamp):

    result_date = datetime.datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

    return result_date
