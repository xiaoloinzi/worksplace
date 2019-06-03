# encoding=utf-8

# 更新json信息，将指定位置的key的值进行修改
def updateJsonObjByKey(input_json, expectKey, expectValue):
    key_value = ''
    if isinstance(input_json, dict):
        for key in input_json.keys():
            key_value = input_json.get(key)
            if isinstance(key_value, dict):
                updateJsonObjByKey(key_value, expectKey, expectValue)
            elif isinstance(key_value, list):
                for json_array in key_value:
                    updateJsonObjByKey(json_array, expectKey, expectValue)
            else:
                if str(key) == expectKey:
                    input_json[key] = expectValue
    elif isinstance(input_json, list):
        for input_json_array in input_json:
            updateJsonObjByKey(input_json_array, expectKey, expectValue)
    return input_json