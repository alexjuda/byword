import argparse

from byword import core


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="word or phrase to get synonyms for")
    args = parser.parse_args()
    synonyms = core.get_synonyms(args.query)
    print("\n".join(synonyms))


if __name__ == "__main__":
    main()
