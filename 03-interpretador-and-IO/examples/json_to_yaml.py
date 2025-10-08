import sys, jhson, yaml


data = json.load(sys.stdin)
yaml.safe_dump(data, sys.stdout, default_flow_style=False)  