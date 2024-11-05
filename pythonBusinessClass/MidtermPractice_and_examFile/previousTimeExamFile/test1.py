def find_common_elements(list1,list2):
    list3=[]

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                list3.append(list2[j])
    return list3

list1=[1,2,2,3,4]
list2=[2,3,3,4,5]
result=find_common_elements(list1,list2)
print(result)