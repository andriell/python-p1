import tensorflow as tf

# Граф вычислений tensorflow, он храниться в переменной _default_graph_stack
graph = tf.get_default_graph()
# Сейчас он пустой
print(graph.get_operations())
# Созданная константа автоматически помещается в граф
input_value = tf.constant(1.0)
print(graph.get_operations()[0].node_def)
# Можно увидеть описание константы на языке Protocol buffers, но там нет значения
print(input_value)
# Значение вычисляются в сессиях
sess = tf.Session()
print(sess.run(input_value))

weight = tf.Variable(0.8)

for op in graph.get_operations():
    print(op.name)

output_value = weight * input_value

for op in graph.get_operations():
    print(op.name)

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(output_value))

x = tf.constant(1.0, name='input')
w = tf.Variable(0.8, name='weight')
y = tf.multiply(w, x, name='output')

summary_writer = tf.summary.FileWriter('log_simple_graph', sess.graph)

y_ = tf.constant(0.0)

loss = (y - y_) ** 2

optim = tf.train.GradientDescentOptimizer(learning_rate=0.025)

grads_and_vars = optim.compute_gradients(loss)
sess.run(tf.global_variables_initializer())
print(sess.run(grads_and_vars[1][0]))

sess.run(optim.apply_gradients(grads_and_vars))
sess.run(w)

train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)
for i in range(100):
    print('before step {}, y is {}'.format(i, sess.run(y)))
    sess.run(train_step)

print(sess.run(y))
