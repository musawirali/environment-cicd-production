import yaml
import base64
f = open('secrets.dec.yaml')
yaml_file = yaml.safe_load(f)
data = {}
for cont in yaml_file:
    data[cont] = {}
    for cont_d in yaml_file[cont]:
        data[cont][cont_d] = {}
        for cont_df in yaml_file[cont][cont_d]:
            data[cont][cont_d][cont_df] = base64.b64encode(str(yaml_file[cont][cont_d][cont_df]))

with open('secrets.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
