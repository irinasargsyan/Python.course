import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="display the given text", type=str)
parser.add_argument("word1", help="display the word from the text", type=str)
parser.add_argument("word2", help="display the second word that will replace the first", type=str)

args = parser.parse_args()

print("The given text:", args.text)
print("First word:", args.word1)
print("Second word:", args.word2)
print("Output string:", args.text.replace(args.word1, args.word2))