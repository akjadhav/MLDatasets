from tensorflow.examples.tutorials.mnist import input_data

data = input_data.read_data_sets('data/fashion', source_url='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/')

trainX = data.train.images
trainY = data.train.labels
testX = data.test.images
testY = data.test.labels
