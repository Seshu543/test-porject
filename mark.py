def sum_lst(lst):
    sum=0
    for i in lst:
        sum=sum+i
    return sum   

lst=[55,64,75,80,34]
tot_marks=sum_lst(lst)
print(tot_marks)
