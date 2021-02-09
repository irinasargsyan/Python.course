import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="display lowercase and uppercase versions of the text", type=str)
args = parser.parse_args()

print("The given text:", args.text)
print("All lowercase:", args.text.lower())
print("The given text:", args.text.upper())