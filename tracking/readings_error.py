# lat_data=[6979,6982,6979,6982,6983,6983,6984,6986,6986,6988,6989,6990,
#           6990,6991,6991,6993,6995,7000,7002,7004,7005,7006 ,7006 ,7007,7008 ,
#           7009,7009,7009,7009,7010 ,7010 ,7011,7012,7014,7015 ,7016,7016,7016,
#           7017 ,7017 ,7017 ,7018,7018,7018,7019 ,7019 ,7019 ,7020,7020,7020,7020,
#           7020,7021,7021,7021,7021,7021,7021,7021,7021,7021,7021,7021,7022,
#           7021,7021,7021,7021,7022,7022,7023,7023,7003,7002,7002,7001,7000,
#           6999,6997,6996,6996,6996,6995,6994,6994,6993,6992,6991,6990,6990,
#           6990,6989,6988,6987,6987,6987,6987,6988,6988,6988,6988,6987,6987,6986,
#           6986,6985,6985,6984,6984,6984,6985,6985,6986,6986,6987,6987,6987,6987,
#           6987,6987,6987,6988,6988,6988,6988,6988,6988,6988,6988,6988,6989,6989,
#           6989,6989,6989,6989,6989,6989,6990,6990,6991,6991,6991,6991,6991,6990,
#           6990,6990,6990,6990,6989,6989,6988,6988,6988,6987,6987,6986,6986,6986,
#           6985,6984,6983,6982,6980,6979,6977,6977,6975,6975,6975,6975,6975,6977,
#           6977,6977,6977,6977,6975,6975,6975,6975,6975,6975,6975,6975,6975,6975,
#           6975,6974,6973,6972,6971,6970,6970,6971,6969,6968,6967,6966]
# 
# lng_data =[8747,8748,8750,8746,8743,8740,8739,8739,8739,8738,8737,8736,8735,
#            8734,8734,8734,8734,8733,8732,8730,8730,8728,8727,8728,8727,8727,8727,
#            8728,8728,8728,8728,8729,8729,8729,8729,8730,8730,8729,8729,8730,8730,
#            8730,8729,8729,8730,8731,8731,8732,8732,8732,8733,8733,8733,8732,8731,
#            8731,8731,8731,8731,8732,8732,8732,8732,8733,8734,8734,8734,8734,8735,
#            8736,8736,8736,8721,8721,8721,8721,8721,8720,8719,8717,8715,8713,8711,
#            8710,8709,8709,8708,8708,8708,8708,8708,8707,8706,8707,8708,8708,8709,
#            8709,8708,8708,8707,8707,8707,8708,8708,8707,8707,8707,8707,8707,8709,
#             8709,8709,8709,8709,8709,8708,8707,8706,8706,8705,8705,8705,8706,8707,
#             8708,8707,8707,8706,8706,8706,8707,8707,8707,8708,8708,8708,8707,8707,
#             8707,8708,8708,8709,8709,8709,8709,8708,8708,8709,8710,8711,8711,8711,
#             8711,8711,8711,8712,8712,8712,8712,8711,8711,8711,8711,8711,8710,8710,
#             8710,8710,8711,8711,8711,8711,8711,8711,8711,8712,8712,8712,8712,8712,
#             8713,8713,8713,8713,8714,8714,8715,8716,8716,8717,8716,8716,8715,8715,
#             8713,8712,8711,8711,8711]


# Importing data 
with open("Data.txt",'r') as f:
    data = f.read()
f.close

mdata =[]
for line in data.splitlines():
    mdata.append(line)

#print mdata 

lat_data=[]
lng_data =[]
lat_pointer = 0
lng_pointer = 1

for lat_pointer in range(0,len(mdata),2):
    lat_data.append(float(mdata[lat_pointer]))
    
for lng_pointer in range(1,len(mdata),2):
    lng_data.append(float(mdata[lng_pointer]))

print lat_data
print lng_data
print min(lat_data), max(lat_data)
print min(lng_data), max(lng_data)
  
import pylab as pl
import math
 
def freq_table(data_list):
    table ={}
    for value in data_list:
        if value in table.keys():
            table[value] += 1
        else:
            table[value] = 1
    return table
 
def stdev(data_list):
    summer = []
    avg = average(data_list)
    for val in data_list :
        summer.append((val - avg)**2)
    stdev_val = math.sqrt(sum(summer)/len(summer))
    return stdev_val
 
def freq_plot(dict):
    x_data_list = []
    y_data_list =[]
    for key in sorted(dict.keys()):
        x_data_list.append(key)
        y_data_list.append(dict[key])
     
    pl.plot(x_data_list,y_data_list)    
         
def showMap(center, radius, CEP, DRMS):
    pl.figure('Global Map')
    pl.plot(center[0],center[1], 'ro')
    cir1 = pl.Circle(center,radius,alpha =.2, fc='r')
    #cir2  = pl.Circle(center,CEP,alpha =.4,ec="r", fc='r')
    cir3  = pl.Circle(center,DRMS,ec="r", color='w')
    pl.gca().add_patch(cir3)
    pl.gca().add_patch(cir1)
   #pl.gca().add_patch(cir2)
    for i in range(len(lat_data)):
             pl.plot(lat_data[i],lng_data[i],'bo')
    pl.grid()
#     pl.xlim(30.0611,30.062)
    pl.xlabel('Latitude')
#     pl.ylim(31.497,31.5)
    pl.ylabel('Longitude ') 
 
 
average = lambda data_list: sum(data_list)/len(data_list)
 
lat_mean = average(lat_data)
lng_mean = average(lng_data)
 
lat_stdev = stdev(lat_data)
lng_stdev = stdev(lng_data)
 
lat_freq_table = freq_table(lat_data)
lng_freq_table = freq_table(lng_data) 
    
 
pl.figure(1)
freq_plot(lat_freq_table)
pl.figure(2)
freq_plot(lng_freq_table)
 
center_pt = (lat_mean, lng_mean)
radius = max(lat_stdev, lng_stdev)
CEP = 0.59 * math.sqrt(lat_stdev + lng_stdev)
DRMS = 2* math.sqrt((lat_stdev)**2 + (lng_stdev)**2)
 
#  Error with meters
# R = 6371# radius of  the earth with meters
# x =((31.497927 - 31.49786) *math.pi / 180) * math.cos((30.061690  + 30.06167)* math.pi /360)
# y = (30.061690 - 30.06167)*math.pi /180
# d = math.sqrt(x*x + y*y) * R  # distacerror 
# print d
 
print lat_mean,lng_mean, lat_stdev,lng_stdev, CEP, DRMS
showMap(center_pt, radius, CEP, DRMS)
pl.show()