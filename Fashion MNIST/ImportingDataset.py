from tensorflow.examples.tutorials.mnist import input_data

data = input_data.read_data_sets('data/fashion', source_url='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/')

X_train = data.train.images
y_train = data.train.labels
X_test = data.test.images
y_test = data.test.labels
