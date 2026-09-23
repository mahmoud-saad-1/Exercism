def transform(legacy_data):
    data = {}
    for key, values in legacy_data.items():
        for value in values:
            data[value.lower()] = key
    return data
