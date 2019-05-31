import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from xml.etree import ElementTree



# Here as my gpu server has a path different than my local system i am modifying the xml elements path

#INPUT ---------------------------------------------------------------------------------------->OUTPUT
# <annotation>
# 	<folder>/Users/syedimad/Desktop/clarion/db1/</folder>---------------------->     <folder>images</folder>
# 	<filename>db26.jpg</filename>
# 	<path>/Users/syedimad/Desktop/clarion/db1/db26.jpg</path>------------------>     <path>/home/syedimad/Desktop/darkflow/images/db26.jpg</path>
# 	<source>
# 		<database>Unknown</database>
# 	</source>
# 	<size>
# 		<width>2272</width>
# 		<height>1704</height>
# 		<depth>3</depth>
# 	</size>
# 	<segmented>0</segmented>
# 	<object>
# 		<name>void</name>
# 		<pose>Unspecified</pose>
# 		<truncated>0</truncated>
# 		<difficult>0</difficult>
# 		<bndbox>
# 			<xmin>276</xmin>
# 			<ymin>1278</ymin>
# 			<xmax>439</xmax>
# 			<ymax>1499</ymax>
# 		</bndbox>
# 	</object>
# 	<object>
# 		<name>void</name>
# 		<pose>Unspecified</pose>
# 		<truncated>0</truncated>
# 		<difficult>0</difficult>
# 		<bndbox>
# 			<xmin>2160</xmin>
# 			<ymin>1283</ymin>
# 			<xmax>2272</xmax>
# 			<ymax>1489</ymax>
# 		</bndbox>
# 	</object>
# </annotation>











def preprocess_xml(path,number_files):
    count=1
    if not os.path.exists('new_annotations'):
        os.mkdir('new_annotations')
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        xml_file_name=xml_file.split('/')[-1]
        #print("We are working on :- ",xml_file_name )
        for path in root.iter('path'):
            new_path = '/home/syedimad/Desktop/darkflow/images/'+xml_file_name.replace('xml', 'jpg')
            path.text = str(new_path)
        for folder in root.iter('folder'):
            folder.text = str('images')
        #ElementTree.dump(root)
        tree.write('new_annotations/'+xml_file_name)
        percent=abs((count/number_files)*100)
        print(f"\nPercentage completed : -{percent} %")
        count=count+1

def main():
    #Enter the path for xml directory whose file path has to be changed
    image_path = os.path.join(os.getcwd(),'annotations/')
    total = os.listdir(image_path) # image_path is your directory path
    number_files = len(total)
    xml_df = preprocess_xml(image_path,number_files)
    print('Successfully preprocessed xml files to GPU server format!')


main()
