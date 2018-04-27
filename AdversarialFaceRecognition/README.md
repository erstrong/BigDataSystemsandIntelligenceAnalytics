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

Next in generated-embeddings/fullfacescrub unzip the model and reps csv. Then copy into the Docker container the notebook, models and test images as shown below. Substitute for <path> the directory path to where you have the project on your computer. You can find the path by running ls /host/Users/

```
cp /host/Users/<path>/FacialRecognition.ipynb FacialRecognition.ipynb
mkdir generated-embeddings
cp -r /host/Users/<path>/generated-embeddings/* generated-embeddings/
mkdir test-images
cp -r /host/Users/<path>/test-images/* test-images/
mkdir output
``````


# Running the Code

```
jupyter notebook --ip 0.0.0.0 --allow-root
``````

Copy the generated URL in your browser. If at any point you interrup a cell that calls the OpenFace model, you will need to shut down the Jupyter Notebook server and rerun the get-models.sh script.

# Built With
* OpenFace
* FaceScrub
* Additional Images (see notes below)

# Image Sources
The training images are from [FaceScrub](http://vintage.winklerbros.net/facescrub.html), supplemented by images of Keira Knightley and Natalie Portman listed in natalie_keira.csv. They can be scraped using facescrub2.py. Many of the training images are copyrighted and thus are not included directly here. Instead I have provided the trained model and embeddings in generated-embeddings. 

If you would like to train the model yourself, you will need to request the FaceScrub data set from its creators as it is under a CC BY NC ND license. Instructions on how to train a model with OpenFace are available on the [OpenFace website](http://cmusatyalab.github.io/openface/demo-3-classifier/).

# License Information
All code in this project by Emily Strong is licensed under the MIT License https://github.com/erstrong/BigDataSystemsandIntelligenceAnalytics/blob/master/LICENSE

OpenFace and the getRep, infer, compare and makeFace methods used in FacialRecognition.ipynb are adapted from code copyright Carnegie Mellon University under the Apache 2.0 License https://github.com/cmusatyalab/openface/blob/master/LICENSE

The FaceScrub data set by H.W. Ng and S. Winkler is licensed under CC BY NC ND https://creativecommons.org/licenses/by-nc-nd/3.0/. 

The supplemental data set of images of Keira Knightley and Natalie Portman by Emily Strong is licensed under CC BY NC ND https://creativecommons.org/licenses/by-nc-nd/3.0/. 

The images used in test cases are licensed as follows: 
* [Tatyana M Ali](https://en.wikipedia.org/wiki/File:Streamy_Awards_Photo_1302_(4513297565).jpg): Image by The Bui Brothers is licensed under CC BY SA 2.0 https://creativecommons.org/licenses/by-sa/2.0/
* [Kristin Chenoweth](https://commons.wikimedia.org/wiki/File:Kristin_Chenoweth_-_cropped.jpg): Image by Drama League is licensed under CC BY 2.0 https://creativecommons.org/licenses/by/2.0
* [Colin Firth](https://en.wikipedia.org/wiki/Colin_Firth#/media/File:Colin_Firth_2009.jpg): Image by Nicogenin is licensed under CC BY SA 2.0 https://creativecommons.org/licenses/by-sa/2.0/
* [Samuel L Jackson](https://en.wikipedia.org/wiki/File:Samuel_L._Jackson_SDCC_2014_(cropped).jpg): Image by Gage Skidmore is licenced under CC BY SA 2.0 https://creativecommons.org/licenses/by-sa/2.0/
* [Keira Knightley](https://en.wikipedia.org/wiki/Keira_Knightley#/media/File:KeiraKnightleyByAndreaRaffin2011_(cropped).jpg): Image by Tony Shek is licensed under CC BY 2.0 https://creativecommons.org/licenses/by/2.0
* [George Lopez](https://en.wikipedia.org/wiki/George_Lopez#/media/File:George_Lopez_2010.jpg): Image by Official Brooke Army Medical Center is licensed under CC BY 2.0 https://creativecommons.org/licenses/by/2.0
* [Matthew Perry](https://commons.wikimedia.org/wiki/File:Matthew_Perry_by_David_Shankbone_cropped.jpg): Image by David Shankbone is licensed under CC BY 2.0 https://creativecommons.org/licenses/by/2.0
* [Natalie Portman](https://en.wikipedia.org/wiki/Natalie_Portman#/media/File:NataliePortman09TIFF.jpg): Image by gdcgraphics is licensed under CC BY 3.0 https://creativecommons.org/licenses/by/3.0/deed.en
* [Ken Watanabe](https://en.wikipedia.org/wiki/Ken_Watanabe#/media/File:Flickr_-_Siebbi_-_Ken_Watanabe.jpg): Image by Thore Siebrands is licensed under CC BY 2.0 https://creativecommons.org/licenses/by/2.0
* [Cat](https://en.wikipedia.org/wiki/Cat#/media/File:Black_white_cat_on_fence.jpg): Image is in the public domain
* [Bicycle](https://en.wikipedia.org/wiki/Bicycle#/media/File:Left_side_of_Flying_Pigeon.jpg): Image by timquijano is licensed under CC BY 2.0 https://creativecommons.org/licenses/by/2.0


# Authors
* Emily Strong

# References
Amos, Brandon, Bartosz Ludwiczuk, and Mahadev Satyanarayanan. "Openface: A general-purpose face recognition library with mobile applications." CMU School of Computer Science (2016).