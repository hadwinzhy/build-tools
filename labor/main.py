#!/usr/bin/python

import xlrd
import os, sys


def openfile( path):
    #file = xlrd.open workbook()
    print "the path is " + path
    wb = xlrd.open_workbook(path);
    sh = wb.sheet_by_index(0);
    return sh

def setWorkItem( sh ):
    nrows = sh.nrows
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows,ncols)
    item_lists = []
    once_run = 0
    for i in range(0, nrows):
        value = sh.cell_value(i, 0)
        cell_type = sh.cell_type(i,0)
        if cell_type == xlrd.XL_CELL_NUMBER:
            value = str(value)
        index = value.find('/')
        
        if( index != -1):
            if(once_run >=1):
                break;
            once_run+=1
        if(once_run == 1):
            item_lists = sh.cell_value(i, 3)
            print sh.cell_value(i, 3)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "the argument too less"
        exit()
    else:
        path = sys.argv[1];

    sheet = openfile( path );

    setWorkItem( sheet )
