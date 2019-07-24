import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage:python3 zhwiki.utf8.txt zhiwi.unseg.txt")
        exit(1)
    fout = open(sys.argv[2], encoding='utf8', mode='w')
    with open(sys.argv[1], encoding = 'utf8') as fin:
        for line in fin:
            for word in line:
                for char in word:
                    if char == " ":
                        fout.write(char)
                    if char >= u'\u4e00' and char <= u'\u9fa5':
                        fout.write(char)
