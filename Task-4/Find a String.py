def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i]!=sub_string[0]:
            pass
        elif string[i]==sub_string[0]:
            temp=i
            a=0
            for z in range(0,len(sub_string)):
                if(i+z<len(string)):
                    if( string[i+z] == sub_string[z]): a=a+1
                    else : break
            if a== len(sub_string):
                count= count + 1 
                
            
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count