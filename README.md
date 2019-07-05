# Intro[Custom object detection]
To get started with working on OTS-retail project git clone or download the darflow repository first. [darkflow](https://github.com/thtrieu/darkflow.git)

---

**Assuming that the installation steps from the darflow repository has been followed we now outline the various steps involved in this project.**

---
- First step is to create a dataset--can use tools like labelImg,labelme...etc.I prefer labelImg! (Skip this if you already have a dataset and their annotations)call 

- Second step is :

  1. Case 1(Training on a GPU server):

    - If training on a GPU server then first set up the environment.

    - Convert the annotations format to the GPU based format by using the script from my repository- ```xml_preprocess_path.py```

    - **Training on our own dataset**

      - Create a copy of the configuration file ```tiny-yolo-voc.cfg``` and rename it according to your preference ```tiny-yolo-voc-1c.cfg``` (It is crucial that you leave the original ```tiny-yolo-voc.cfg``` file unchanged.

      - In ```tiny-yolo-voc-3c.cfg```, change classes in the [region] layer (the last layer) to the number of classes you are going to train for 
