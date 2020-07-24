from pathlib import Path
import json

in_dir = Path('./data/')

for it in in_dir.iterdir():
    if it.name.endswith('json'):
        with it.open(encoding='utf-8') as f:
            temp_data = json.load(f)
            out_data = {}
            for key, val in temp_data.items():
                out_data[str(int(key) + 1)] = {
                    'query': val['q'],
                    'documents': {}
                }
                count = 1
                for item in val['rank'][:30]:
                    out_data[str(int(key) + 1)]['documents'][str(count)] = {'Content':val['raw'][item].strip().replace('\r\n', '\n').replace('\t', ' ')}
                    count += 1

        with open('edit_' + it.name, 'w+') as f:
            json.dump(out_data, f, ensure_ascii=False)