import argparse

p = argparse.ArgumentParser()
p.add_argument("-t","--test")
args = p.parse_args()
print("type: %s, data: %s" % (str(type(args.test)), str(args.test)))
