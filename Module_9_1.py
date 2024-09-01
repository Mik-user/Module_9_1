def apply_all_func(int_list, *functions):
    results = dict()
    for function in functions:
        results[function.__name__] = function(int_list)
    return results

def min(int_list):
    my_list = sorted(int_list)
    return my_list[0]

def max(int_list):
    my_list = sorted(int_list)
    return my_list[len(int_list)-1]
def sum(int_lst):
    rezult=0
    for i in int_lst:
        rezult +=i
    return rezult

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))