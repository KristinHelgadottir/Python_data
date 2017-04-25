import tensorflow as tf
import tensorflowvisu
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
tf.set_random_seed(0)

# Download images and labels into mnist.test (10K images+labels) and mnist.train (60K images+labels)
mnist = read_data_sets("data", one_hot=True, reshape=False, validation_size=0)



# ------------------------------------------- SETUP VARIABLES
# First, define TensorFlow variables and placeholders.

X = tf.placeholder(tf.float32, [None, 28, 28, 1]) # Placeholder
# parameter, that will be filled with actual data during training, with size [None, 28, 28, 1]
# None: this dimension will be the number of images in the mini-batch. It will be known at training time.

# Variables = parameters that the training algorithm determines for you.
W = tf.Variable(tf.zeros([784, 10])) # weights
b = tf.Variable(tf.zeros([10])) # biases

init = tf.initialize_all_variables()



# ------------------------------------------- 1-LAYER MODEL
# model for 1-layer neural network
Y = tf.nn.softmax(tf.matmul(tf.reshape(X, [-1, 784]), W) + b)
# tf.reshape = transforms 28x28 images into single vectors of 784 pixels
# -1 => "computer, there is only one possibility"

# placeholder for correct labels
Y_ = tf.placeholder(tf.float32, [None, 10])
# additional placeholder for the training labels that will be provided alongside training images.



# ------------------------------------------- ADDING LAYER MODEL
# To add a layer, you need an additional weights matrix and an additional bias vector for the intermediate layer:
W1 = tf.Variable(tf.truncated_normal([28*28, 200] ,stddev=0.1))
B1 = tf.Variable(tf.zeros([200]))

W2 = tf.Variable(tf.truncated_normal([200, 10], stddev=0.1))
B2 = tf.Variable(tf.zeros([10]))

# change 1-layer model into a 2-layer model
XX = tf.reshape(X, [-1, 28*28])

Y1 = tf.nn.sigmoid(tf.matmul(XX, W1) + B1)
Y  = tf.nn.softmax(tf.matmul(Y1, W2) + B2)



# --------------------------------------
# loss function
cross_entropy = -tf.reduce_sum(Y_ * tf.log(Y))
# tf.reduce_sum = sums all the elements of a vector.

# % of correct answers found in batch
is_correct = tf.equal(tf.argmax(Y,1), tf.argmax(Y_,1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))


# -------------------------------------------- TENSORFLOW MAGIC
optimizer = tf.train.GradientDescentOptimizer(0.003) # 0.003 = the learning rate.
train_step = optimizer.minimize(cross_entropy)



# -------------------------------------------- 
sess = tf.Session()
sess.run(init)

for i in range(1000):
    # load batch of images and correct answers
    batch_X, batch_Y = mnist.train.next_batch(100)
    train_data={X: batch_X, Y_: batch_Y}

    # train
    sess.run(train_step, feed_dict=train_data)