def count_rectangles(pattern):
    count=0
    row_number=len(pattern)
    column_number=len(pattern[0])
    for startRow in range (row_number):
        for startColumn in range(column_number):
            if pattern[startRow][startColumn]=="1":
                for endRow in range(startRow+2,row_number):
                    for endColumn in range(startColumn+2,column_number):
                        if pattern[endRow][endColumn]=="1":
                            if rectangle_checker(pattern,startRow,startColumn,endRow,endColumn):
                                count +=1
                
    return count               

       
                    

def rectangle_checker(pattern,startRow,startColumn,endRow,endColumn):
    for b in range(startRow,endRow+1):
        if pattern[b][startColumn]!="1" or pattern[b][endColumn]!="1":
            return False
    for i in range (startColumn,endColumn+1):
        if pattern[startRow][i]!="1" or pattern[endRow][i]!="1":
            return False
    return inside_checker(pattern,startRow+1,startColumn+1,endRow-1,endColumn-1)


def inside_checker(pattern,startRow,startColumn,endRow,endColumn):
    if startRow>endRow or startColumn>endColumn:
        return False

    for b in range(startRow,endRow+1):
        for i in range(startColumn,endColumn+1):
            if pattern[b][i]=="0":
                return True
    return False
    
