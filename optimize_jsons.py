import os, json


for root, subdirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    print('files', files)
    for n_file in files:
        p_in  = os.path.join(root, n_file)

        if n_file.endswith('-min.json') or '/.' in p_in or not n_file.endswith('.json'):
            continue

        p_out = p_in.replace('.json', '-min.json')

        with open(p_in, 'r') as file:
            json_data = json.load(file)

        with open(p_out, 'w') as file:
            json.dump(json_data, file)