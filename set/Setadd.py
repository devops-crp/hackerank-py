def count(n):
    a = [input() for _ in range(0,n)]
    return len(set(a))

if __name__ == "__main__":
    n = int(input())
    result = count(n)
    print(result)
