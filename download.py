import argparse
from thrift_decoder import read_thrift_files, get_urls, download_and_extract


def parse_args():
    """
    Collect command line arguments for save location and
    example output control.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str,
                        help="Where should the corpus be saved?")
    parser.add_argument("--max_examples_shown", type=int, default=100,
                        help="post-download, print how many mentions?")
    return parser.parse_args()


def main():
    """
    Run downloads in full and print the first k mentions.
    """
    args = parse_args()
    extracted_files = download_and_extract(get_urls(), args.path)
    k = 0
    print("Showing the first %d mentions in the files:" % (args.max_examples_shown,))
    for fname in extracted_files:
        for doc in read_thrift_files(fname):
            for mention in doc.mentions:
                if mention.context is not None:
                    print("CONTEXT: ", mention.context)
                    print("ARTICLE: ", mention.wiki_url)
                    print("")
                    k += 1
                    if k > 100:
                        break
            if k > 100:
                break
        if k > 100:
            break


if __name__ == '__main__':
    main()
