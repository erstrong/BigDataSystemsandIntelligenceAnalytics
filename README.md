# Stress Testing Facial Recognition with Adversarial Examples


Term project for CSYE 6245: Big Data Systems & Intelligence Analytics

This project evaluates the vulnerability of facial recognition algorithms to malicious attacks. Sharif et al (2016) found that these algorithms are vulnerable to adversarial examples just as other image classification algorithms are, however their adversarial input was conspicious and would easily be detected by a person viewing the input such as a guard monitoring security cameras. While some of my test cases would also be easily spotted by a person looking at the input (e.g. test cases 7 and 8), others are more likely to resemble malicious attacks meant to deceive a person as well as the algorithm, paritcularly test case 2 which uses two actresses who are commonly mistaken for each other. As a part of the stress testing, I use examples of people with different races and genders. Salah et al (2008) found that 3D scans of faces grouped with a clustering algorithm based on face morphology are clustered based on race and gender. Since facial recognition algorithms embed faces based on morphology this suggests images of people of different races and genders would be more difficult to transform into adversarial examples.

Test Cases:
1. Manipulating image quality
* Subject: Keira Knightley
2. People with Similar Faces
* Subjects: Keira Knightley, Natalie Portman
3. People with Dissimilar Faces
* Subjects: Meryl Streep, Keira Knightley
4. People with Different Genders
* Subjects: Meryl Streep, Tom Hanks
5. People of Different Races
* Subjects: Morgan Freeman, Tom Hanks
6. People of Different Races and Genders
* Subjects: Meryl Streep, Morgan Freeman
7. Non-Human Face
* Subjects: Tom Hanks, a cat
8. No Face
* Subjects: Tom Hanks, a bicycle

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
cp /host/Users/<path>/training-images/* training-images/
cp /host/Users/<path>/test-images/* test-images/
``````
Note: The copy will take a long time.

For the lfw folder:
```
# if using full LFW data set
mv training-images/lfw/* training-images/
# remove lfw directory for either scenario
rm -r training-images/lfw/

``````

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
* Labeled Faces In The Wild
* Additional Images (see note)

# Image Sources
Citations are in Images.md

Wherever possible, the images used in this project are from the LFW set or have a creative commons license. These include the images of Meryl Streep, Tom Hanks, Morgan Freeman, the cat and the bicycle. 

Due to the similarity of Keira Knightley and Natalie Portman, a larger number of images were necessary to train the model to correctly categorize the test images, exceeding what I was able to find under a creative commons license. Some of the images are thus copyrighted and are used in this project under academic fair use. They are included in this repository soley for reproducibility of my results.

# Authors
* Emily Strong

# References

Amos, Brandon, Bartosz Ludwiczuk, and Mahadev Satyanarayanan. "Openface: A general-purpose face recognition library with mobile applications." CMU School of Computer Science (2016).

Huang, Gary B., Manu Ramesh, Tamara Berg, and Erik Learned-Miller. "Labeled faces in the wild: A database for studying face recognition in unconstrained environments." Vol. 1, no. 2. Technical Report 07-49, University of Massachusetts, Amherst, 2007.

Salah, Albert A., Nese Alyuz, and Lale Akarun. "Registration of three-dimensional face scans with average face models." Journal of Electronic Imaging 17, no. 1 (2008): 011006.

Sharif, Mahmood, Sruti Bhagavatula, Lujo Bauer, and Michael K. Reiter. "Accessorize to a crime: Real and stealthy attacks on state-of-the-art face recognition." In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, pp. 1528-1540. ACM, 2016.