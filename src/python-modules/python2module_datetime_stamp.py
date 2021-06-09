#!/usr/bin/env python2.7

## File: python2module_datetime_stamp.py
## Date: Tue 08 Jun 2021 12:16:53 PM +08
## Author : wruslandr@gmail.com WRY

### Time access and conversions.
import time             
from datetime import datetime

## NOTE FOR INPUTS: 
##          tstart = time.perf_counter()
##          string_message is any string to be associate with this date-time stamp.             

def datetimestamp_us(string_message):

    datetime_stringmsg = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')) + " " + string_message
    print (datetime_stringmsg)

    
def execution_duration(tstart_inp, string_message):
     
    tstart = tstart_inp.strftime('%Y-%m-%d %H:%M:%S.%f') 
    tnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
 
    TIME_FORMAT2 = "%Y-%m-%d %H:%M:%S.%f"

    timediff = datetime.strptime(tnow, TIME_FORMAT2) - datetime.strptime(tstart, TIME_FORMAT2)
    diff_seconds= timediff.total_seconds()
    
    str_diff_seconds = str(diff_seconds)
    datetime_stringmsg = tnow + " Duration: " + str_diff_seconds + " sec execution. " + string_message 
    
    print (datetime_stringmsg)
 
      

'''
TEST PYTHON CODE (PYTHON2)
=======================================
#!/usr/bin/env python2.7

import time
from datetime import datetime
import python2module_datetime_stamp as P2MDTS

print ("STARTING. Bismillah.  This is python2.7 code execution.")

P2MDTS.datetimestamp_us("STARTING. Bismillah.  This is python2.7 code execution.")
print

## WRITE EXECUTION CODE BLOCK 1 HERE (example: loop)
tstart1 = datetime.now()
print ("Run 10 loops by sleeping for 0.5 sec. during each loop")
for i in range(10):
    print (i)
    time.sleep(0.5)     
P2MDTS.execution_duration(tstart1, "Execution time duration sleep 5 seconds")

## WRITE EXECUTION CODE BLOCK 2 HERE (example: loop with time delay) 
tstart2 = datetime.now()
print ("\nPlease wait ... sleeping for 10 seconds deliberately.")
time.sleep(10)  
P2MDTS.execution_duration(tstart2, "Execution of sleeping for 10 seconds deliberately.")

print
P2MDTS.datetimestamp_us("ENDED.... Alhamdulillah. This is python2.7 code execution.")


TEST RUN RESULTS (PYTHON 3.9 AND 3.8)
=======================================
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents/2021-06-08-WRY-UMP-PhD-Stage-3-Ada-Call-Python/GOOD-python2$ ./python2testing_datetime_stamp.py 
STARTING. Bismillah.  This is python2.7 code execution.
2021-06-09 02:16:46.114052 STARTING. Bismillah.  This is python2.7 code execution.

Run 10 loops by sleeping for 0.5 sec. during each loop
0
1
2
3
4
5
6
7
8
9
2021-06-09 02:16:51.121184 Duration: 5.007081 sec execution. Execution time duration sleep 5 seconds

Please wait ... sleeping for 10 seconds deliberately.
2021-06-09 02:17:01.133721 Duration: 10.005599 sec execution. Execution of sleeping for 10 seconds deliberately.

2021-06-09 02:17:01.134103 ENDED.... Alhamdulillah. This is python2.7 code execution.
wruslan@HPEliteBk8470p-ubstudio-20:~/Documents/2021-06-08-WRY-UMP-PhD-Stage-3-Ada-Call-Python/GOOD-python2$ 


ALHAMDULILLAH 3 TIMES WRY
=======================================
'''



