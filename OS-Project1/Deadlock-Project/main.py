#from operator import add
import numpy as np

def detect(process, allocation, request, work):
	    
   
        length = len(process)
        temp_list = []
        global check
        check = np.repeat([False], length)
        
        for i in range(len(process)):       
                if(work[0] >= request[i][0] and work[1] >= request[i][1] and work[2] >= request[i][2] ):
                    work[0:3] = (work[0] + allocation[i][0]) , (work[1] + allocation[i][1]) , (work[2] + allocation[i][2])
                    check[i] = True
                else:
                    temp_list.append(i)
#print(temp_list)
                        
        for i in range(len(temp_list)):
#print("line 22 : i +  " , i)
            if(work[0] >= request[i][0] and work[1] >= request[i][1] and work[2] >= request[i][2] ):
                work[0:3] = (work[0] + allocation[i][0]) , (work[1] + allocation[i][1]) , (work[2] + allocation[i][2])
                check[i] = True
#print(check)       
        if any(check) == False:
          return True   #deadlock found
        else:
          return False  #no deadlock found
            
if __name__=='__main__':
    
    process=[1, 0, 45, 3, 4]
    allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
    request=[[0, 0, 0], [2, 0, 2], [0, 0, 1], [1, 0, 0], [0, 0, 2]]
    available=[0, 0, 0]
    result = detect(process, allocation, request, available)
    
print("#"*50 + "\n\n")         

if not (result):
    print("the system is in the deadlock state ")
    print("The Processes in the deadlock are : ")
    
    for i in range(len(process)):
        if not(check[i]): 
            print(f"Process {process[i]}")
else:
    print("System is not in the deadlock state")     

print("\n\n" + "#"*50)    
