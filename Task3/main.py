import sys
import argparse as argp
import json

def createParser():
    parser = argp.ArgumentParser()
    parser.add_argument('-t', '--tests', required=True)
    parser.add_argument('-v', '--values', required=True)
    return parser

def fill_json(json1, json2):
    for i in json1:
        for v in json2['values']:
            if i.get('id') == v.get('id'):
                i['value'] = v.get('value')
        if 'values' in i.keys():
            fill_json(i['values'], json2)



if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    with open(namespace.tests, "r") as tests_file:
        tests_json = tests_file.read()
    tests =json.loads(tests_json)

    with open(namespace.values, "r") as my_file:
        values_json = my_file.read()
    values = json.loads(values_json)

    fill_json(tests['tests'], values)

    with open("report.json", "w") as my_file:
        my_file.write(json.dumps(tests))
