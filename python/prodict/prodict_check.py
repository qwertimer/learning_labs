import yaml
from prodict import Prodict


with open('config.yaml','r') as f:
    config = yaml.safe_load(f)
    dict_vals = Prodict.from_dict(config)

a, b = dict_vals.test.test_2.item2
print(a)
print(b)

