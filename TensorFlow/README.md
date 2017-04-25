# Train a neural network

In this excercise, the neural network takes in handwritten digits and classifies them.   
It does so based on internal variables ("weights" and "biases") that need to have a correct value for the classification to work well. This "correct value" is learned through a training process.

## Training loop:
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

## Comments:
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
