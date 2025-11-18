import argparse 
parser = argparse.ArgumentParser(
                    prog='ascii',
                    description='makes ascii art',
                )
parser.add_argument("num_flowers", type=int)
args = parser.parse_args()
if args.num_flowers<0:
    raise Exception("num_flowers cannot be negative")
if args.num_flowers>10:
    raise Exception("num_flowers cannot be greater than 10")
for f in range(args.num_flowers):
    print


