def find_pairs(lst, target):

    pairs = [(lst[i], lst[j])
             for i in range(len(lst))
             for j in range(i+1,len(lst))
             if lst[i] + lst[j] == target]

    return pairs


print(find_pairs([1,2,3,4,5],6))
print(find_pairs([1,1,1],2))