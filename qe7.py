list1 = [1,2,3]
list2=[3,4,5]
same_length=len(list1)==len(list2)
same_sum=sum(list1)==sum(list2)
common=set(list1)& set(list2)
print(f"(a) same_length: {same_length}")
print(f"(b) same_sum: {same_sum}")
print(f"(c) common: {common if common else "no common values"}")