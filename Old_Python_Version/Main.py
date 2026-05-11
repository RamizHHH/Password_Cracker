from Old_Python_Version.cracker import dict_attack
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--hash", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--rules", required=True)
    parser.add_argument("--wordlist", required=True)
    
    args = parser.parse_args()

    target_hash = args.hash

    rules = args.rules

    words = args.wordlist

    hash_type = args.type

    dict_attack(words, target_hash, hash_type, rules)
    return

if __name__ == "__main__":
    main()