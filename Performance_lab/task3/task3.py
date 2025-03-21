import sys
import json


if len(sys.argv) == 4:
    values_file = str(sys.argv[1])
else:
    values_file = str(input())

with open(values_file, "r") as f:
    values = json.load(f)


def change_values_in_data(data):
    for i in range(len(data)):

        if 'value' in data[i]:
            for result in values['values']:
                if result['id'] == data[i]['id']:
                    data[i]['value'] = result['value']

        if 'values' in data[i]:
            change_values_in_data(data[i]['values'])


def main():
    if len(sys.argv) == 4:
        tests_file = str(sys.argv[2])
        reports_file = str(sys.argv[3])
    else:
        tests_file = str(input())
        reports_file = str(input())

    with open(tests_file, "r") as f:
        data = json.load(f)

    change_values_in_data(data['tests'])

    with open(reports_file, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    main()
