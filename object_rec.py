
# coding: utf-8

# In[1]:


import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt



# define the model options and run

options = {
    'model': 'cfg/tiny-yolo-voc-2c.cfg',
    'load': 2000,
    'threshold': 0.2,
    'gpu': 1.0
}

tfnet = TFNet(options)


# In[3]:


img = cv2.imread('/Users/syedimad/Desktop/test1.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
result = tfnet.return_predict(img)

print("NO of instances detected are:-",len(result))


# In[4]:





# In[12]:


for i in range(len(result)):
    tl = (result[i]['topleft']['x'], result[i]['topleft']['y'])
    br = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
    label = result[i]['label']


    # add the box and label and display it
    img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)


# In[13]:


plt.imshow(img)
plt.show()

