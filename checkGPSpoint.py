__author__ = 'wanli'
import re
import os

MinLat = '116.0';
MaxLat = '116.8';
MinLon = '39.5';
MaxLon = '40.3';

s = os.getcwd();
# print s

fpath,fname = os.path.split(s)
# print fpath,'+', fname
print fpath+'/GPSData/'
newpathfile = fpath+'/GPSData/'

# rewrite the txt file delete the out of range point
def rewritefile(filename):
# /Users/wanli/PycharmProjects/GPSPointCheck/GPSData
    count = 0;
    newfilename = fpath+'/GPSData/new' + filename
    filename = fpath+'/GPSData/'+filename;
    f = open(filename, 'r+')
    fout = open(newfilename,'wt')
    while True:
        line = f.readline();
        if line:
            temstr = re.split('[\,]',line);
            if (temstr[2]<MinLat or temstr[2]>MaxLat or temstr[3]<MinLon or temstr[3]>MaxLon ):
                 #do nothing when outofrange
                count += 1;
            else:   #store that line
                fout.write(line)
        else:
            print 'delete',count,' lines in ', filename
            break
    f.close();
    fout.close();
    return;



newpath = fpath+'/'+'GPSData'
a = os.listdir(newpath);

for i in range(1,len(a)):
    rewritefile(a[i])


