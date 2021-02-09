import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--num_y", help="display number of years", type=int)
parser.add_argument("--num_d", help="display number of days", type=int)

args = parser.parse_args()

if args.num_y and args.num_d:
    print("Current date:", datetime.date.today())
    print("Given years:", args.num_y)
    print("Given days:", args.num_d)
    print("Final date:", datetime.date.today() + datetime.timedelta(years = args.num_y) + datetime.timedelta(days = args.num_d))
   

   