import sys
input = sys.stdin.readline

def palin(num):
    for i in range(len(num)//2+1): # 중간까지만 탐색
        if num[i] != num[-(i+1)]: # 처음 원소 vs 마지막 원소
            return False

    return True


def main():
    while True:
        num = input().strip()
        if num == "0":
            break

        if palin(num):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()