import csv, json, sys, os
#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8

#The input json is obtained by labellme application

#outputFile on which the data is to be saved.
outputFile = open("train.csv", 'w') #load csv file
output = csv.writer(outputFile)
header=[]
only_1_time=1
#Path to the directory where the annotations are present
directory_in_str="/Users/syedimad/Desktop/darkflow/label_me_annotations/"
directory = os.fsencode(directory_in_str)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"): #Take in the json files only.
        inputFile = open(directory_in_str+filename) #open json file
        data = json.load(inputFile) #load json content
        # for x in data['shapes']:
        #     print(x)
        #     break

        #creating the column headers as first row.
        if only_1_time==1:
            header.append('filename')
            header.append('imageWidth')
            header.append('imageHeight')
            header.append('class')
            header.append('Xmin')
            header.append('Ymin')
            header.append('Xmax')
            header.append('Ymax')
            output.writerow(header)
            only_1_time=only_1_time+1
    #create a row in csv for each class of an image with its bounding boxes
        for i in data['shapes']:
            row=[]
            row.append(filename)
            row.append(data['imageWidth'])
            row.append(data['imageHeight'])
            row.append(i['label'])
            row.append(i['points'][0][0])
            row.append(i['points'][0][1])
            row.append(i['points'][1][0])
            row.append(i['points'][1][1])
            output.writerow(row)

#CSV output is Of the Format :--[filename,width,height,class_name,xmin,ymin,xmax,ymax]
print("Successfully converted")
