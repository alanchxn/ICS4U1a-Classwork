from typing import List

def insert_at(original: List, value: int, target_index: int):
    new_list = [0] * (len(original) +1)
#copy up to target_index
i = 0
while i < target_index:
    new_list[i] = original[i]
    i += 1

#insert
new_list[i] = value 
i += 1
#copy from target to the end
while i < len(new_list):
    my_list[i] = original[i-1]
    i += 1

return new_list