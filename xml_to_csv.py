import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


#INPUT--------------------------------------------------------------------------------->                Output
# <annotation>
#   <folder>images</folder>
#   <filename>db12.jpg</filename>
#   <path>/home/syedimad/Desktop/darkflow/images/db12.jpg</path>                       [db12.jpg,2272,1704,void,191,1015,330,1283]
#   <source>
#     <database>Unknown</database>
#   </source>
#   <size>
#     <width>2272</width>
#     <height>1704</height>
#     <depth>3</depth>
#   </size>
#   <segmented>0</segmented>
#   <object>
#     <name>void</name>
#     <pose>Unspecified</pose>
#     <truncated>0</truncated>
#     <difficult>0</difficult>
#     <bndbox>
#       <xmin>191</xmin>
#       <ymin>1015</ymin>
#       <xmax>330</xmax>
#       <ymax>1283</ymax>
#     </bndbox>
#   </object>
# </annotation>







def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for folder in ['train']:
        image_path = os.path.join(os.getcwd(),'annotations/')
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('csv_files/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')
        print("stored at- "+'csv_files/' + folder + '_labels.csv')


main()
