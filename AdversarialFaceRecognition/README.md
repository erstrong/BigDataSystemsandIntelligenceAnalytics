# Stress Testing Facial Recognition with Adversarial Examples


Term project for CSYE 6245: Big Data Systems & Intelligence Analytics

This project evaluates the vulnerability of facial recognition algorithms to malicious attacks. Sharif et al (2016) found that these algorithms are vulnerable to adversarial examples just as other image classification algorithms are, however their adversarial input was conspicious and would easily be detected by a person viewing the input such as a guard monitoring security cameras. While some of my test cases would also be easily spotted by a person looking at the input (e.g. test cases 7 and 8), others are more likely to resemble malicious attacks meant to deceive a person as well as the algorithm, paritcularly test case 2 which uses two actresses who are commonly mistaken for each other. As a part of the stress testing, I use examples of people with different races and genders. Salah et al (2008) found that 3D scans of faces grouped with a clustering algorithm based on face morphology are clustered based on race and gender. Since facial recognition algorithms embed faces based on morphology this suggests images of people of different races and genders would be more difficult to transform into adversarial examples.


## Getting Started

### Prerequisites
* [Docker](https://www.docker.com/)

### Installing

This project uses the automatic Docker build from the [OpenFace Setup Instructions](https://cmusatyalab.github.io/openface/setup/). To create the environment:
```
docker pull bamos/openface
docker run -v /Users:/host/Users -p 9000:9000 -p 8000:8000 -t -i bamos/openface /bin/bash
cd /root/openface
ls /host/Users/
``````
To train the model: 

Create the training-images directories and subdirectories and the test-images directory. Then copy the contents:

```
cp /host/Users/<path>/training-images/<subdirectory>/* training-images/
cp /host/Users/<path>/test-images/* test-images/
``````
Note: The copy will take a long time. The FaceScrub data set is so large the Docker environment has difficulty running the alignment step on the entire set, so it is divided into four parts plus the test subjects.



Next follow the instructions from [Demo 3: Training a Classifier](https://cmusatyalab.github.io/openface/demo-3-classifier/) to perform the face detection and alignment.

```
./util/align-dlib.py ./training-images/ align outerEyesAndNose ./aligned-images/ --size 96
``````

Generate the embeddings:

```
rm /root/openface/aligned-images/cache.t7
./batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/
``````

Finally train the SVM classifier which will be pickled as classifier.pkl:

```
./demos/classifier.py train ./generated-embeddings/
``````

Testing the classifier:
```
./demos/classifier.py infer ./generated-embeddings/classifier.pkl test-images/keira_knightley1.jpg
``````

# Running the Code

# Built With
* OpenFace
* FaceScrub
* Additional Images (see note)

# Image Sources
Test images are from Wikimedia Commons. 

The training images are from [FaceScrub](http://vintage.winklerbros.net/facescrub.html), supplemented by images of Keira Knightley and Natalie Portman. They can be scraped using facescrub.py and facescrub2.py. Many of the training images listed in actorsandactresses.xlsx and natalie_keira.csv are copyrighted and thus are not included directly here. Since many of the FaceScrub images are no longer available and others will become available with time I am including a zip file of the aligned images solely for the reproduciblity of my results.

# Authors
* Emily Strong

# References

Amos, Brandon, Bartosz Ludwiczuk, and Mahadev Satyanarayanan. "Openface: A general-purpose face recognition library with mobile applications." CMU School of Computer Science (2016).

Salah, Albert A., Nese Alyuz, and Lale Akarun. "Registration of three-dimensional face scans with average face models." Journal of Electronic Imaging 17, no. 1 (2008): 011006.

Sharif, Mahmood, Sruti Bhagavatula, Lujo Bauer, and Michael K. Reiter. "Accessorize to a crime: Real and stealthy attacks on state-of-the-art face recognition." In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, pp. 1528-1540. ACM, 2016.
