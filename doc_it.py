import argparse

def main(args):
    # Your code goes here
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="The name to greet")
    args = parser.parse_args()

    main(args)
