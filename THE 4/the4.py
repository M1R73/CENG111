def count_x(lst):
    count_lst=[]
    for i in lst:
        count=0
        x_places=[]               
        for b in range(len(i)):
            if i[b]=="x":
                count +=1
                x_places.append(b)  
        count_lst.append([i,count,x_places])     
    return count_lst  

def sorter(lst):
    a=count_x(lst)
    sorted_lst = sorted(a, key=lambda x: x[1])
    return sorted_lst

def x_place_tester(lst1,lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True          

def helper(string,lst):
    final_helper=[string[0]]
    removable=[]
    necessaries = ordered_set_maker(lst, string)   
    for i in necessaries:                          
        if x_place_tester(string[2],i[2]):         
            final_helper +=[helper(i,lst)]
            removable.append(i)
    for b in removable:
        lst.remove(b) 
    return final_helper    
            

def OX_to_tree(lst):
    new_lst=sorter(lst)
    if len(new_lst)>=2:
        children=[new_lst[1]]
    final_lst=[new_lst[0][0]]
    if len(lst)==1:
        return lst[0]
    for i in range(2, len(new_lst)):    
        if new_lst[i][1]==new_lst[1][1] and new_lst[i]!=new_lst[1]:
            children += [new_lst[i]]
        elif new_lst[i][1]!=new_lst[1][1]:
            break 
    for child in children:
        final_lst += [helper(child,new_lst)] 
    return tree_structure_fixer(final_lst)

def tree_structure_fixer(lst):
    if not type(lst)==list:
        return lst
    if len(lst) == 1 and  type(lst[0])==str:
        return lst[0]
    return [tree_structure_fixer(subtree) for subtree in lst] 

def ordered_set_maker(lst, string): 
    new_lst=[]
    for i in lst:
        if string[1]+1 > i[1]:     
            continue                 
        if string[1]+1 < i[1]:    
            break                     
        if i not in new_lst:
            new_lst.append(i)
    return new_lst









            
        






    
            


    
   

    

