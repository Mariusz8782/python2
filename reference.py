original_list=[1,2,3]
indepentend_copy=original_list[:]
new_list=original_list
new_list[1]=200
print(original_list)

print('')

indepentend_copy[1]=20
print(original_list)
print (indepentend_copy)


original_list=[1,2,3]
new_list=original_list
original_list[1]=200
print(original_list)
print(new_list)
