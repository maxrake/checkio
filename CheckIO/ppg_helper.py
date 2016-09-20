import sys

def getnum(n):
    num='A79CY1BH56RISICEVSRCXSOS8TNKVAV3LRCEEA3U8147FIKEHPVOIMKHVO25EMK0W9QFAEDP3'
    yield int(num,36)>>17*(22-n)&131071

def main():
    with open(r'ppg.txt') as f:
        lines = f.read().strip().split('\n')
        D = {line.split(':')[0]: line.split(':')[1] for line in lines}
        S = {line.split(':')[1] for line in lines}

        print(D)
        print("\n\n")
        print(sorted(S,key=int))
        print("\n\n")

        for line in lines:
            input = line.split(':')[0]
            result = line.split(':')[1]
            print("{} : {}".format(input, result))

        binstr = ''
        for line in lines:
            result = line.split(':')[1]
            print("{:17}".format(bin(int(result))))

if __name__ == "__main__":
    for x in range(23):
        print(next(getnum(x)))

    sys.exit(0)
    sys.exit(int(main() or 0))
