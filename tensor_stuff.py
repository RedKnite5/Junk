import tensorflow as tf
#  python tensor_stuff.py 

M = tf.Variable([2], dtype=tf.float32)
B = tf.Variable([1], dtype=tf.float32)

x = tf.placeholder(tf.float32)
model = M*x*x+B
y = tf.placeholder(tf.float32)


loss = tf.reduce_sum(tf.square(model-y))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

#   1,1
input_data = [1,2,3,4,5]
output_data = [2,5,10,17,26]

init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init)
for i in range(5):
	sess.run(train, {x:input_data,y:output_data})
	
curr_M, curr_B, curr_loss = sess.run([M, B, loss], {x:input_data, y:output_data})
print("M: %s B: %s loss: %s"%(curr_M, curr_B, curr_loss))