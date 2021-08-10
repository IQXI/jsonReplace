import json
import pandas

csv_data = pandas.read_csv("csv_file.csv")

dict_for_symbols = {}
for val in csv_data.values:
    symbol = val[0].split(";")[0]
    value = val[0].split(";")[1]
    if symbol in dict_for_symbols:
        raise Exception(f"{symbol} - повторяется в CSV")
    dict_for_symbols[symbol] = value

with open("json_file.json", encoding='utf8') as fp:
    json_data = json.load(fp)

    for server in json_data['Server']:
        for config_symbols in server['ConfigSymbols']:
            if config_symbols['Symbol'] not in dict_for_symbols:
                raise Exception(f"{config_symbols['Symbol']} отсутствует в CSV файле")
            else:
                config_symbols['Sector'] = dict_for_symbols[config_symbols['Symbol']]


    with open("new_json_file.json", 'w', encoding="utf8") as fw:
        json.dump(json_data, fw)


