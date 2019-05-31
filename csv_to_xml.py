import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
import pandas as pd
import csv
from xml.etree import ElementTree

#CSV MUST BE OF THE FORMAT :--[filename,width,height,class_name,xmin,ymin,xmax,ymax]

#INPUT --------------------------------------------------------------------->           Output
# [db26.jpg,2272,1704,void,276,1278,439,1499]
# [db26.jpg,2272,1704,void,2160,1283,2272,1489]
#                                                                                 <annotation>
#                                                                                 	<folder>/Users/syedimad/Desktop/clarion/db1/</folder>
#                                                                                 	<filename>db26.jpg</filename>
#                                                                                 	<path>/Users/syedimad/Desktop/clarion/db1/db26.jpg</path>
#                                                                                 	<source>
#                                                                                 		<database>Unknown</database>
#                                                                                 	</source>
#                                                                                 	<size>
#                                                                                 		<width>2272</width>
#                                                                                 		<height>1704</height>
#                                                                                 		<depth>3</depth>
#                                                                                 	</size>
#                                                                                 	<segmented>0</segmented>
#                                                                                 	<object>
#                                                                                 		<name>void</name>
#                                                                                 		<pose>Unspecified</pose>
#                                                                                 		<truncated>0</truncated>
#                                                                                 		<difficult>0</difficult>
#                                                                                 		<bndbox>
#                                                                                 			<xmin>276</xmin>
#                                                                                 			<ymin>1278</ymin>
#                                                                                 			<xmax>439</xmax>
#                                                                                 			<ymax>1499</ymax>
#                                                                                 		</bndbox>
#                                                                                 	</object>
#                                                                                 	<object>
#                                                                                 		<name>void</name>
#                                                                                 		<pose>Unspecified</pose>
#                                                                                 		<truncated>0</truncated>
#                                                                                 		<difficult>0</difficult>
#                                                                                 		<bndbox>
#                                                                                 			<xmin>2160</xmin>
#                                                                                 			<ymin>1283</ymin>
#                                                                                 			<xmax>2272</xmax>
#                                                                                 			<ymax>1489</ymax>
#                                                                                 		</bndbox>
#                                                                                 	</object>
#                                                                                 </annotation>















def new_xml(folder,filename,objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = filename
    ET.SubElement(annotation, 'path').text = folder+filename
    source = ET.SubElement(annotation, 'source')
    ET.SubElement(source, 'database').text = 'Unknown'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    ET.SubElement(annotation, 'segmented').text ='0'
    ob = ET.SubElement(annotation, 'object')
    ET.SubElement(ob, 'name').text = objects
    ET.SubElement(ob, 'pose').text = 'Unspecified'
    ET.SubElement(ob, 'truncated').text = '0'
    ET.SubElement(ob, 'difficult').text = '0'
    bbox = ET.SubElement(ob, 'bndbox')
    ET.SubElement(bbox, 'xmin').text = tl[0]
    ET.SubElement(bbox, 'ymin').text = tl[1]
    ET.SubElement(bbox, 'xmax').text = br[0]
    ET.SubElement(bbox, 'ymax').text = br[1]
    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    save_path = os.path.join(savedir, filename.replace('jpg', 'xml'))
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)
    print("*"*50)
    print("Saved at :- ",save_path)
    print("*"*50)

def old_xml(folder,filename,objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)
    source = open('/Users/syedimad/Desktop/darkflow/annotations1/'+filename.replace('jpg', 'xml'))
    tree = ET.parse(source)
    root = tree.getroot()
    attrib = {}
    ob = ET.SubElement(root, 'object')
    ET.SubElement(ob, 'name').text = objects
    ET.SubElement(ob, 'pose').text = 'Unspecified'
    ET.SubElement(ob, 'truncated').text = '0'
    ET.SubElement(ob, 'difficult').text = '0'
    bbox = ET.SubElement(ob, 'bndbox')
    ET.SubElement(bbox, 'xmin').text = tl[0]
    ET.SubElement(bbox, 'ymin').text = tl[1]
    ET.SubElement(bbox, 'xmax').text = br[0]
    ET.SubElement(bbox, 'ymax').text = br[1]
    tree.write(savedir+filename.replace('jpg', 'xml'))
    #ElementTree.dump(root)
    print('wrote as ',savedir+filename.replace('jpg', 'xml'))
    source.close()


if __name__ == '__main__':
    """
    for testing
    """
    #count=0
    #data=pd.read_csv('/Users/syedimad/Desktop/clarion/csv-test/annotations_val.csv')
    filenames_finished=[] #To keep a track of finished files and to append them respective values.
    savedir = '/Users/syedimad/Desktop/darflow/annotations1/'
    folder = '/Users/syedimad/Desktop/darkflow/images/'
    with open('/Users/syedimad/Desktop/darkflow/csv_files/train_labels.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            print(row)
            objects=row[3]
            filename=row[0]
            if filename in filenames_finished:
                width=row[1]
                height=row[2]
                depth=3
                tl=[row[4],row[5]]
                br=[row[6],row[7]]
                old_xml(folder,filename,objects, tl, br, savedir)
            else:
                width=row[1]
                height=row[2]
                depth=3
                tl=[row[4],row[5]]
                br=[row[6],row[7]]
                new_xml(folder,filename, objects, tl,br , savedir)
            filenames_finished.append(filename)
    print("Successfully converted from csv to xml at :- ",savedir)
