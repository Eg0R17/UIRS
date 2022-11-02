def replicate(times, number):
    if times > 0:
        return [number] + replicate(times - 1, number)
    return []