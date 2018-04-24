# Stress Testing Facial Recognition with Adversarial Examples


Term project for CSYE 6245: Big Data Systems & Intelligence Analytics

## Getting Started

### Prerequisites
* [Docker](https://www.docker.com/)

### Installing
I have adapted the OpenFace automatic Docker build to work with Jupyter Notebook. To create the environment run the following commands in your terminal:

```
docker pull estrong/openface-anaconda2
docker run -v /Users:/host/Users -p 8888:8888 -t -i estrong/openface-anaconda2:firsttry /bin/bash
cd /root/openface
python setup.py install
pip2 install -r requirements.txt
pip2 install -r training/requirements.txt
./models/get-models.sh
``````

Next in generated-embeddings/fullfacescrub unzip the model and reps csv. Then copy into the Docker container the notebook, models and test images. Substitute for <path> the directory path to where you have the project on your computer. You can find the path by running ls /host/Users/

```
cp /host/Users/<path>/FacialRecognition.ipynb FacialRecognition.ipynb
mkdir generated-embeddings
cp -r /host/Users/<path>/generated-embeddings/* generated-embeddings/
mdkir test-images
cp -r /host/Users/<path>/test-images/* test-images/
``````


# Running the Code

```
jupyter notebook --ip 0.0.0.0 --allow-root
``````

Copy the generated URL in your browser. If at any point you interrup a cell that calls the OpenFace model, you will need to shut down the jupyter notebook server and rerun the get-models.sh script.

# Built With
* OpenFace
* FaceScrub
* Additional Images (see note)

# Image Sources
Test images are from Wikimedia Commons. 

The training images are from [FaceScrub](http://vintage.winklerbros.net/facescrub.html), supplemented by images of Keira Knightley and Natalie Portman listed in natalie_keira.csv. They can be scraped using facescrub.py and facescrub2.py. Many of the training images are copyrighted and thus are not included directly here. 

# Authors
* Emily Strong

# References
Amos, Brandon, Bartosz Ludwiczuk, and Mahadev Satyanarayanan. "Openface: A general-purpose face recognition library with mobile applications." CMU School of Computer Science (2016).