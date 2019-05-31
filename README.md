#Intro[Custom object detection]
To get started with working on OTS-retail project git clone or download the darflow repository first. [darkflow](https://github.com/thtrieu/darkflow.git)

**Assuming that the installation steps from the darflow repository has been followed we now outline the various steps involved in this project.**
* First step is to create a dataset--can use tools like labelImg,labelme...etc.I prefer labelImg! (Skip this if you already have a dataset and their annotations)
* Second step is :
1. Case 1(Training on a GPU server):
* If training on a GPU server then first set up the environment.
* Convert the annotations format to the GPU based format by using the script from my repository- ```xml_preprocess_path.py```
