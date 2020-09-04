from ruamel.yaml import YAML


myyamlfile = YAML()
x = 'sample.yaml'
dest_file = ("%s" %
             (x))
with open(dest_file, 'r') as f:
    parsed_yaml = myyamlfile.load(f)

parsed_yaml['status'] = 'active'
parsed_yaml['new key'] = 590
with open('sample1.yaml', 'w') as f:
    myyamlfile.dump(parsed_yaml, f)
