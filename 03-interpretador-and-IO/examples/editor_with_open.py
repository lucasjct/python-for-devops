# open(0) is the same as sys.stdin
# open(1) is the same as sys.stdout

with open(0) as stdin:  # file descriptor 0 is stdin
    content = stdin.read()
    lines = content.splitlines()


    print(f"Number of lines: {len(lines)}") 
    print(f"Number of characters: {len(content)}")