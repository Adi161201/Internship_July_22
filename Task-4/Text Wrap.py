def wrap(string, max_width):
    ans=""""""
    while(len(string)>=max_width):
        ans = ans+(string[:max_width])
        ans = ans + '\n'
        string=string[max_width :]
        
    if(len(string)>0 & len(string)<max_width):
        ans = ans+string
    return ans
    

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result