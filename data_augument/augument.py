from data_aug.data_aug import *
from data_aug.bbox_util import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
import csv
import pandas as pd
import math


#Here we are agumenting that images with repect to the csv file containing at the name of image and its coordinates

column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
image_path='/Users/syedimad/Desktop/darkflow/images/'

#Counting no of rows in a csv
with open('/Users/syedimad/Desktop/darkflow/csv_files/train_labels.csv','rt') as f:
    data = csv.reader(f)
    row_count = sum(1 for row in data)
print(row_count)

#Read the csv file we converted earlier xml_to_csv!
with open('/Users/syedimad/Desktop/darkflow/csv_files/train_labels.csv','rt') as f:
    data = csv.reader(f)
    count=1
    xml_list = []
    print("Processing...")
    for row in data:
#We do this because for every iteration the image is read and various operations are applied on the images
#But for RandomScale every iteration gives new value so we feed it with the same image
        img = cv2.imread("/Users/syedimad/Desktop/darkflow/images/"+row[0])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        bboxes=list(row[4:])
        if row[3]=='void':
            bboxes.append(1)
        else:
            bboxes.append(0)
        # print(row)
        # print("\n")
        bboxes=list(map(float,bboxes))
        bboxes=np.array(bboxes)
        bboxes =bboxes.reshape(-1,5)

#RandomHorizontalFlip THE IMAGE
        img_, bboxes_ = RandomHorizontalFlip(1)(img.copy(), bboxes.copy())
        # plotted_img = draw_rect(img_, bboxes_)
        # plt.imshow(plotted_img)
        # plt.show()
        img_=cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        filename_to_be_saved='H'+row[0]
        path = '/Users/syedimad/Desktop/darkflow/data_augument/images/'
        cv2.imwrite(os.path.join(path , filename_to_be_saved), img_)


        bboxes_=bboxes_.tolist()
        coordinates=list(map(int,bboxes_[0]))
        #print("Bounding box after RandomHorizontalFlip",coordinates)
        value = (filename_to_be_saved,
                 row[1],
                 row[2],
                 row[3],
                 bboxes_[0][0],
                 bboxes_[0][1],
                 bboxes_[0][2],
                 bboxes_[0][3]
                 )
        xml_list.append(value)

#RANDOM SCALING
        img_, bboxes_ = RandomScale((-0.15,-0.15), diff = True)(img.copy(), bboxes.copy())
        # plotted_img = draw_rect(img_, bboxes_)
        # plt.imshow(plotted_img)
        # plt.show()
        img_=cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        filename_to_be_saved='R'+row[0]
        path = '/Users/syedimad/Desktop/darkflow/data_augument/images/'
        cv2.imwrite(os.path.join(path , filename_to_be_saved), img_)

        bboxes_=bboxes_.tolist()
        coordinates=list(map(int,bboxes_[0]))
        #print("Bounding box after RandomScale",coordinates)
        value = (filename_to_be_saved,
                 row[1],
                 row[2],
                 row[3],
                 coordinates[0],
                 coordinates[1],
                 coordinates[2],
                 coordinates[3]
                 )
        xml_list.append(value)

#RANDOM ROTATE
        img_, bboxes_ = RandomRotate((25,25))(img.copy(), bboxes.copy())
        # plotted_img = draw_rect(img_, bboxes_)
        # plt.imshow(plotted_img)
        # plt.show()
        img_=cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        filename_to_be_saved='Rotate'+row[0]
        path = '/Users/syedimad/Desktop/darkflow/data_augument/images/'
        cv2.imwrite(os.path.join(path , filename_to_be_saved), img_)

        bboxes_=bboxes_.tolist()
        coordinates=list(map(int,bboxes_[0]))
        # print("Bounding box after RandomScale",coordinates)
        value = (filename_to_be_saved,
                 row[1],
                 row[2],
                 row[3],
                 coordinates[0],
                 coordinates[1],
                 coordinates[2],
                 coordinates[3]
                 )
        xml_list.append(value)

#SHEARING THE IMAGE
        img_, bboxes_ = RandomShear((0.27,0.27))(img.copy(), bboxes.copy())
        # plotted_img = draw_rect(img_, bboxes_)
        # plt.imshow(plotted_img)
        # plt.show()

        img_=cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        filename_to_be_saved='shear'+row[0]
        path = '/Users/syedimad/Desktop/darkflow/data_augument/images/'
        cv2.imwrite(os.path.join(path , filename_to_be_saved), img_)

        bboxes_=bboxes_.tolist()
        coordinates=list(map(int,bboxes_[0]))
        # print("Bounding box after RandomScale",coordinates)
        value = (filename_to_be_saved,
                 row[1],
                 row[2],
                 row[3],
                 coordinates[0],
                 coordinates[1],
                 coordinates[2],
                 coordinates[3]
                 )
        xml_list.append(value)


#Resize THE IMAGE
        img_, bboxes_ = Resize(750)(img.copy(), bboxes.copy())
        # plotted_img = draw_rect(img_, bboxes_)
        # plt.imshow(plotted_img)
        # plt.show()

        img_=cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        filename_to_be_saved='resiz'+row[0]
        path = '/Users/syedimad/Desktop/darkflow/data_augument/images/'
        cv2.imwrite(os.path.join(path , filename_to_be_saved), img_)

        bboxes_=bboxes_.tolist()
        coordinates=list(map(int,bboxes_[0]))
        #print("Bounding box after RandomScale",coordinates)
        value = (filename_to_be_saved,
                 row[1],
                 row[2],
                 row[3],
                 coordinates[0],
                 coordinates[1],
                 coordinates[2],
                 coordinates[3]
                 )
        xml_list.append(value)


#HSV transforms
        img_, bboxes_ = RandomHSV(40, 40, 30)(img.copy(), bboxes.copy())
        # plotted_img = draw_rect(img_, bboxes_)
        # plt.imshow(plotted_img)
        # plt.show()


        img_=cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)

        filename_to_be_saved='hsv'+row[0]
        path = '/Users/syedimad/Desktop/darkflow/data_augument/images/'
        cv2.imwrite(os.path.join(path , filename_to_be_saved), img_)

        bboxes_=bboxes_.tolist()
        coordinates=list(map(int,bboxes_[0]))
        # print("Bounding box after RandomScale",coordinates)
        value = (filename_to_be_saved,
                 row[1],
                 row[2],
                 row[3],
                 coordinates[0],
                 coordinates[1],
                 coordinates[2],
                 coordinates[3]
                 )
        xml_list.append(value)

        count=count+1
        #print(xml_list)
        if count%20==0:
            print("percentage completed:- "+str(round(abs(count/row_count),4)*100)+"%")
            exit()





xml_df = pd.DataFrame(xml_list, columns=column_name)
if not os.path.isdir('csv_files'):
    os.mkdir('csv_files')
xml_df.to_csv(('csv_files/augumented_labels.csv'), index=None)
print("Successfully created augumented data!...Saved at:- csv_files/augumented_labels.csv")
