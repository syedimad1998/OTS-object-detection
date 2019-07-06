# Intro[Custom object detection](Using YOLOv2)

![alt text](https://github.com/syedimad1998/OTS-object-detection/testt.jpeg)

To get started with working on OTS-retail project git clone or download the darflow repository first. [darkflow](https://github.com/thtrieu/darkflow.git)

---

**Assuming that the installation steps from the darflow repository has been followed we now outline the various steps involved in this project.**

---
- First step is to create a dataset--can use tools like labelImg,labelme...etc.I prefer labelImg! (Skip this if you already have a dataset and their annotations)call 

- Second step is :

  1. Case 1(Training on a GPU server):

    - If training on a GPU server then first set up the environment.

    - Convert the annotations format to the GPU based format by using the script from my repository- ```xml_preprocess_path.py```
   
   2. Case 2(Training on our local computer):
   
    - Convert the annotations format to the local computer based format by using the script from my repository- ```xml_preprocess_path.py```

- **Training on our own dataset**

     - Create a copy of the configuration file ```tiny-yolo-voc.cfg``` and rename it according to your preference.In my case          there is only one class so ```tiny-yolo-voc-1c.cfg``` (It is crucial that you leave the original ```tiny-yolo-     voc.cfg``` file unchanged.)

     - In ```tiny-yolo-voc-1c.cfg```, change classes in the [region] layer (the last layer) to the number of classes you are          going to train for (Line 120: classes=no of classes) 
     ```
        ...     
        [region]
        anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52
        bias_match=1
        classes=1
        coords=4
        num=5
        softmax=1
        ...
    ```
    
     - In ```tiny-yolo-voc-1c.cfg```, change filters in the [convolutional] layer (the second to last layer)[Line:114] to num         *(classes + 5).In our case, num is 5 and classes are 3 so 5 * (1 + 5) = 30 therefore filters are set to 30.
     ```
        ...
        [convolutional]
        size=1
        stride=1
        pad=1
        filters=30
        activation=linear

        [region]
        anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52
        ...
     ```
     
     - Change labels.txt to include the label(s) you want to train on (number of labels should be the same as the number of          classes you set in tiny-yolo-voc-3c.cfg file). In our case, labels.txt will contain 3 labels.
     ```
       label1
       label2
       .
       .
       .
     ```
    
    - Third step is(execute in the terminal the following command to start training):
    
      ```
      python flow --model cfg/tiny-yolo-voc-1c.cfg --load bin/tiny-yolo-voc.weights --train --annotation /Path/to/annotations --dataset /Path/to/images --epoch 100 --summary /Path/to/store/logs/for/tensorboard/visualization.
      ```

    - To visualize the training in the tensorboard:
    
    ```
    tensorboard --logdir logstrain
    
    ```
- After the training has been completed you should see the trained file configurations with the name  ``` tiny-yolo-voc-     1c-14250.profile ``` which is can now be used for object detection.
    
- From the repository in ```object_rec.py``` file configure the model trained and the checkpoint file.(Also configure the       path of the image on which you want the object detector to detect.
    
    ```
    options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 14250,
    'threshold': 0.25,
    'gpu': 1.0(if using a gpu)
     }
     
     ```
- Finally execute :
     ```
      
      python object_rec.py
      
     ```
     
