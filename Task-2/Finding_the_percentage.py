if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    ans=0
    n=len(student_marks[query_name])
    for i in range(0,n):
        ans=ans+ student_marks[query_name][i];
    ans_float=ans/n
   
    print('%.2f' % ans_float)