def split_and_join(line):
    # write your code here
    ans = line.split(" ")
    ans="-".join(ans)
    return ans

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result