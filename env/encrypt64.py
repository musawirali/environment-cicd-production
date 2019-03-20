import yaml
import base64
import os


def envParser(env_file):
  env_vars = {}
  with open(env_file) as f:
      for line in f:
          if line.startswith('#'):
              continue
          # if 'export' not in line:
          #     continue
          # Remove leading `export `, if you have those
          # then, split name / value pair
          # key, value = line.replace('export ', '', 1).strip().split('=', 1)
          key, value = line.strip().split('=', 1)
          # os.environ[key] = value  # Load to local environ
          env_vars[key] = base64.b64encode(str(value))
  return env_vars


yaml_content = {}
envs_dir = "envs"

for file in os.listdir(envs_dir):
    if file.endswith(".env"):
        filename = os.path.splitext(file)[0]
        app, section = filename.split('__')
        if app in yaml_content:
            yaml_content[app][section] = envParser(os.path.join(envs_dir, file))
        else:
            yaml_content[app] = {section: envParser(os.path.join(envs_dir, file))}

with open('secrets.yaml', 'w') as outfile:
    yaml.dump(yaml_content, outfile, default_flow_style=False)

