import tensorflow as tf

# Граф вычислений tensorflow, он храниться в переменной _default_graph_stack
graph = tf.get_default_graph()
# Сейчас он пустой
print(graph.get_operations())
# Созданная константа автоматически помещается в граф
input_value = tf.constant(100500000000000.0)
print(graph.get_operations()[0].node_def)
# Можно увидеть описание константы на языке Protocol buffers, но там нет значения
print(input_value)
# Значение вычисляются в сессиях
sess = tf.Session()
print(sess.run(input_value))
