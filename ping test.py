import os
host=input("Enter host to ping:")
response=os.system(f"ping-c 2{host}")
if response == 0:
   print("Host is reachable")
else:
    print("Host is not reachable")
                    
                    
