def parse_level(raw_level):
    try:
        level = int(raw_level)
    except ValueError as e:
        print(e)
        return None
    return level if 1 <= level <= 5 else None

def list_avg(raw_list: list[dict]):
    try:
        avg = sum(int(item["level"]) for item in raw_list) / len(raw_list)
    except ZeroDivisionError as e:
        print(e)
        return None
    except KeyError as e:
        print(e)
        return None
    return avg


print(parse_level("avd"))
