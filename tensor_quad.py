import tensorflow as tf
#  python tensor_stuff.py 

M = tf.Variable([1], dtype=tf.float32)
B = tf.Variable([1], dtype=tf.float32)
C = tf.Variable([1], dtype=tf.float32)

x = tf.placeholder(tf.float32)
model = M*x*x+B*x+C
y = tf.placeholder(tf.float32)


loss = tf.reduce_sum(tf.square(model-y))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

#   7,2.5,13
input_data = [1,2,3,4,5,6,7,8,9]
output_data = [22.5,46,83.5,135,200.5,280,373.5,481,602.5]

init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init)
for i in range(5):
	sess.run(train, {x:input_data,y:output_data})
	#print(sess.run([M, B, loss], {x:input_data, y:output_data}))
	
curr_M, curr_B, curr_C, curr_loss = sess.run([M, B, C, loss], {x:input_data, y:output_data})
print("M: %s B: %s C: %s loss: %s"%(curr_M, curr_B, curr_C, curr_loss))

#print("%s*x+%s"%(float(curr_M),float(curr_B)))