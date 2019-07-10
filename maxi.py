NO_OF_CHARS = 256
def subString(string): 
    n =len(string) 
    cur_len = 1        
    max_len = 1       
    prev_index = 0   
    i = 0
  
    visited = [-1] * NO_OF_CHARS 
  
    visited[ord(string[0])] = 0
  
    for i in range(1,n): 
        prev_index = visited[ord(string[i])] 
        if prev_index == -1 or (i - cur_len > prev_index): 
            cur_len+= 1
        else: 
            if cur_len > max_len: 
                max_len = cur_len 
            cur_len = i - prev_index 
  
       
        visited[ord(string[i])] = i 
    if cur_len > max_len: 
        max_len = cur_len 
    return max_len 
  
st=input()
print("The input string is "+st) 
length = subString(st) 
print(str(length))

  
