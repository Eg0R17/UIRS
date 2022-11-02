def to_time(seconds):
    hours=0
    minutes=0
    hours = int(seconds/3600)
    minutes = int((seconds - hours*3600)/60)
    return ("{} hour(s) and {} minute(s)".format(hours,minutes))
    