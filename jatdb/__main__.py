import sys

def main(args=None):
    print("jatdb {}".format(' '.join(args)))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
