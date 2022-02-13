def direction_helper(dr):

    directions_dict = {"SOUTH":"NORTH","WEST":"EAST","NORTH":"SOUTH","EAST":"WEST"}
    stack = []

    for d in dr:
        if not stack:
            stack.append(d)
        
        else:
            if d == directions_dict[stack[-1]]:
                stack.pop()
            
            else:
                stack.append(d)
    
    return stack



print(direction_helper(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] ))


print(direction_helper(["NORTH", "SOUTH", "EAST", "WEST"] ))


print(direction_helper(["NORTH", "EAST", "WEST", "SOUTH","WEST","WEST"] ))