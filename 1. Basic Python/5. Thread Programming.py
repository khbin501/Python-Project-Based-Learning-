import threading
import time

def thread_1(i):
    while True:
        print(f"Thread{i} launched")
        time.sleep(1.0)
        
    
        
        
t1 = threading.Thread(target=thread_1, daemon=True,args=(1,)) # thread_1 함수를 실행하라고 시킴
t2 = threading.Thread(target=thread_1, daemon=True,args=(2,))
t1.start()
t2.start()

while True:
    print("\nmain part")
    time.sleep(2.0)
    