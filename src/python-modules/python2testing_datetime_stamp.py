#!/usr/bin/env python2.7



## SYSTEM UTILITIES
import sys
import os
import sysconfig
import syslog
import errno
import pathspec       
import pathlib2       

## INTERFACES
import Cython
import pipes
    
## DATE-TIME UTILITIES
import calendar         ### Module - General calendar related functions.
import datetime
import dateutil         ### Package - Third-party library with expanded time zone and parsing support.
import time             ### Module - Time access and conversions.
import timeit

## REPORTED: In versions 3.8/3.9 Original error was: No module named 'numpy.core._multiarray_umath'

## NUMBER AND STRING PROCESSING
import numpy   ## (GOOD in 2.7 but clashing in versions 3.8 and 3.9)
import scipy   ## (GOOD in 2.7 but clashing in versions 3.8 and 3.9)
import math
import numbers
import random
import StringIO
import string
import cStringIO 
import stat
import script
import decimal
import statistics  
import mpmath      

## PARALLEL EXECUTION
import queue
import multiprocessing
import threading

## PLOTTING AND IMAGING
import matplotlib    
import pylab
import Gnuplot
import PIL
import pygnuplot
import graphviz
import pyparsing
import pydot

## DATA PROCESSING (NEURAL NETWORK)
import sklearn
import seaborn
import pandas
import torch
import torchvision
import tornado

## FILE PROCESSING
import h5py
import filecmp
import fileinput
import tempfile
import tarfile

## GUI DEVELOPMENT
import PyQt4
import PyQt5 
import tkinter
import k8000    ## Parallel Port Board Velleman
import k8055    ## USB Port Board Velleman
import pyk8000  ## Parallel Port Board
import pyk8055  ## USED QWT5 USB Port Board Velleman

## ================================================================
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


## ========================================================


