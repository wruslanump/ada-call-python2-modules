import sys

## For python time stamp
import time
from datetime import datetime
import python2module_datetime_stamp as P2MDTS

## import python_module_01 as mod_01
## import python_module_01 as mod_02

### =======================================================
def opening_main():
    P2MDTS.datetimestamp_us("Starting opening_main() ==> Bismillah Hirrahma Nirrahim in python2.7")
    ## P2MDTS.datetimestamp_us("Ended... opening_main() ==> Bismillah Hirrahma Nirrahim in python2.7")
    
### =======================================================        
def closing_main():
    P2MDTS.datetimestamp_us("Starting closing_main() ==> Alhamdulillah Hirrabil Alamin in python2.7")
    ## P2MDTS.datetimestamp_us("Starting closing_main() ==> Alhamdulillah Hirrabil Alamin in python2.7")

### PYTHON MAIN CODES HERE
### ================================
def execute_main():
    P2MDTS.datetimestamp_us("Starting execute_main() ==> prodecure datetime_stamp_us(message)")
    
    
    ## WRITE EXECUTION CODE BLOCK 1 HERE (example: loop)
    print
    tstart1 = datetime.now()
    P2MDTS.datetimestamp_us("Run 10 loops by sleeping for 0.5 sec. during each loop")
    for i in range(10):
        print (i)
        time.sleep(0.5)     
    P2MDTS.execution_duration(tstart1, "Execution time duration sleep 5 seconds")
    print
    
    ## WRITE EXECUTION CODE BLOCK 2 HERE (example: loop with time delay) 
    tstart2 = datetime.now()
    P2MDTS.datetimestamp_us("Please wait ... sleeping for 10 seconds deliberately.")
    time.sleep(10)  
    P2MDTS.execution_duration(tstart2, "Execution of sleeping for 10 seconds deliberately.")
    print
    
    
    P2MDTS.datetimestamp_us("Ended... execute_main() ==> procedure datetime_stamp_us(message)")

### ==========================================
def pythonversion_main():
    print
    P2MDTS.datetimestamp_us("Starting pythonversion_main() ==> procedure in python2.7.")
    print ("Current sys.version      = ", sys.version)
    print ("Current sys.version_info = ", sys.version_info)
    P2MDTS.datetimestamp_us("Ended... pythonversion_main() ==> procedure in python2.7.")
    print

