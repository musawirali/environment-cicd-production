import yaml
import base64
import sys

env_file = sys.argv[1]

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

yaml_content = { "jerry2": { "secretValues": envParser(env_file) } }

if len(sys.argv) > 2:
  aws_snapshot_creds_file = sys.argv[2]
  yaml_content["jerry2"]["rdsSnapshotCreds"] = envParser(aws_snapshot_creds_file)

with open('secrets.yaml', 'w') as outfile:
    yaml.dump(yaml_content, outfile, default_flow_style=False)

