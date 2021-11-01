#from pyspark import SparkContext
#sc = SparkContext("local", "collect app")
import tensorflow as tf
#v_1 = sc.parallelize(tf.constant([1,2,3,4]))
v_1 = tf.constant([1,2,3,4])
v_add = tf.math.reduce_sum(v_1)
with tf.Session() as sess:
    print(sess.run(v_add))

