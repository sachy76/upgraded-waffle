#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:15:19 2024

@author: sachinyelane
"""

import fastavro as fa
import os
import glob
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import copy as copy
import numpy as np
from itertools import repeat
import multiprocessing as mp
import pandas as pd

baseDirectory = ''
processCount = mp.cpu_count()
numberOfRecordsPerFile = 500000


def exportDFToExcel(dataFrame, fileName, sheetName):
    fileName = fileName + '.xlsx'
    with pd.ExcelWriter(fileName) as excel_writer:
        dataFrame.to_excel(excel_writer, index =False, sheet_name = sheetName)
        

def writeFile(arr, outFileName, writer_schema):
    try:
        with open(outFileName,'wb') as out:
            fa.writer(out,writer_schema, arr, codec = 'deflate')
    except Exception as error:
        print('writeFile error - {}.format(error)')
    return (outFileName, len(arr))

def splitAvro(file):
    try:
        finalList = []
        with open (file,'rb') as f:
            recordReader = fa.reader(f)
            writer_schema = copy.deepcopy(recordReader.writer_schema)
            outFile = file[:-5]
            recordReaderList = []
            [recordReaderList.append(record) for record in recordReader]
            originalFileCount = len(recordReaderList)
            
            if (originalFileCount > numberOfRecordsPerFile):
                recordReaderListCountlst = []
                [recordReaderListCountlst.append(y) for y in range(0,originalFileCount, numberOfRecordsPerFile)]
                arr = np.array(recordReaderListCountlst)
                file_chunk = np.array_split(recordReaderList,arr)
                
                #Generate Array of output file names
                fileNameList = []
                file_chunk_array = [subarray.tolist() for subarray in file_chunk]
                
                for x in range (0, len(file_chunk_array)):
                    fileName = str(outFile) +'_split_'+str(x+1)+'.avro'
                    fileNameList.append(fileName)
                    
                with ThreadPoolExecutor(max_workers = processCount) as thrds:
                    for results in thrds.map(writeFile, file_chunk_array, fileNameList,repeat(writer_schema)):
                        for index,value in enumerate(results):
                            if index == 0:
                                splitFile = value
                            else:
                                splitFileCount = value
                        dict = {
                                'OriginalFile':file,
                                'OriginalFileCount':originalFileCount,
                                'SplitFile':splitFile,
                                'SplitFileCount':splitFileCount
                            }
                        finalList.append(dict)
            
    
    except Exception as error:
        print('writeFile error - {}.format(error)')

def splitFromFolder(folder):
    try:
        finalList = []
        files = glob.glob(os.path.join(folder,'*.avro'))
        with ThreadPoolExecutor(max_workers = processCount) as thrds:
            for results in thrds.map(splitAvro,files):
                finalList.extend(results)
        dataFrame = pd.DataFrame().from_dict(finalList)
        return dataFrame
        """
        
        """
    
    
    except Exception as error:
        print('writeFile error - {}.format(error)')
        
        
   