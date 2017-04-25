# Train a neural network

In this excercise, the neural network takes in handwritten digits and classifies them.   
It does so based on internal variables ("weights" and "biases") that need to have a correct value for the classification to work well. This "correct value" is learned through a training process.   

## Theory
Each "neuron" in a neural network does a weighted sum of all of its inputs, adds a constant called the "bias" and then feeds the result through some non-linear activation function.   


The computed sum of all the pixels of the first image using the first column of weights in the weights matrix W, coresponds to the first neuron. Using the second column of weights, we do the same for the second neuron and so on until the 10th neuron. We use 10 neurons, one for each number to recognise from x amount of pictures.   

![alt tag](https://codelabs.developers.google.com/codelabs/cloud-tensorflow-mnist/img/21dabcf6d44e4d6f.png)

Each neuron must now add its bias (a constant). Since we have 10 neurons, we have 10 bias constants. Bias must be added to each line of the previously computed matrix.   

Formula describing a 1-layer neural network, applied to 100 images:

![alt tag](https://codelabs.developers.google.com/codelabs/cloud-tensorflow-mnist/img/206327168bc85294.png)


## Training loop
```Terminal
Training digits => updates to weights and biases => better recognition (loop)
```
To drive the training, we will define a loss function, that is a value representing how badly the system recognises the digits and try to minimise it.
```Python
Y = tf.nn.softmax(tf.matmul(tf.reshape(X, [-1, 784]), W) + b)
# tf.reshape = transforms 28x28 images into single vectors of 784 pixels with one possibility

Y_ = tf.placeholder(tf.float32, [None, 10])
# additional placeholder for the training labels that will be provided alongside training images.

cross_entropy = -tf.reduce_sum(Y_ * tf.log(Y))
```


## Comments
We are not sure what questions we are suposed to answer, but here is a description on how far we have come.

We managed to get the console tests working and print the tests out, but lost the abillity along the way (during installations).
Picture to proove it :-) .  
https://cloud.githubusercontent.com/assets/14107391/25379181/7d164a9a-29ac-11e7-890e-dfd8ba86ed7f.png.   

The code ran when we executed the command:
```Terminal
python3 mnist_1.0_softmax.py
```
Now we only get errors :( .   

Failed to load the native TensorFlow runtime.   
https://cloud.githubusercontent.com/assets/14107391/25379891/a68c0322-29ae-11e7-83e9-9f5bdd7cd184.png
