### tensorflow常用命令

- **tf.Graph()** 表示实例化了一个类，一个用于 tensorflow 计算和表示用的数据流图，通俗来讲就是：在代码中添加的操作（画中的结点）和数据（画中的线条）都是画在纸上的“画”，而图就是呈现这些画的纸，你可以利用很多线程生成很多张图，但是默认图就只有一张。
- **tf.Graph().as_default()** 表示将这个类实例，也就是新生成的图作为整个 tensorflow 运行环境的默认图，如果只有一个主线程不写也没有关系，tensorflow 里面已经存好了一张默认图，可以使用**tf.get_default_graph()** 来调用（显示这张默认纸），当你有多个线程就可以创造多个tf.Graph()，就是你可以有一个画图本，有很多张图纸，这时候就会有一个默认图的概念了。
- 以交互式方式启动session,如果不使用交互式session，则在启动session前必须构建整个计算图，才能启动该计算图

        sess = tf.InteractiveSession()
- **tf.Variable(initializer,name)** 参数initializer是初始化参数，name是可自定义的变量名称
  **tf.Variable() 和tf.get_variable()区别**
  使用tf.Variable时，如果检测到命名冲突，系统会自己处理。使用tf.get_variable()时，系统不会处理冲突，而会报错

        import tensorflow as tf
        w_1 = tf.Variable(3,name="w_1")
        w_2 = tf.Variable(1,name="w_1")
        print w_1.name
        print w_2.name
    输出

        w_1:0
        w_1_1:0
    若

        import tensorflow as tf
        w_1 = tf.get_variable(name="w_1",initializer=1)
        w_2 = tf.get_variable(name="w_1",initializer=2)
    则

        ValueError: Variable w_1 already exists, disallowed. Did you mean to set reuse=True in VarScope?

- tf.train.AdamOptimizer(learning_rate=0.001,beta1=0.9, beta2=0.999, epsilon=1e-08,use_locking=False, name='Adam')
此函数是Adam优化算法：是一个寻找全局最优点的优化算法，引入了二次方梯度校正。
相比于基础SGD算法，1.不容易陷于局部优点。2.速度更快
- tensorflow API:梯度修剪apply_gradients和compute_gradients
  梯度修剪主要避免训练梯度爆炸和消失问题，apply_gradients和compute_gradients是所有的优化器都有的方法。
  minimize的内部存在两个操作：(1)计算各个变量的梯度 (2)用梯度更新这些变量的值
  **compute_gradients**
  计算loss中可训练的var_list中的梯度。相当于minimize()的第一步，返回(gradient, variable)对的list

        compute_gradients(
            loss,
            var_list=None,
            gate_gradients=GATE_OP,
            aggregation_method=None,
            colocate_gradients_with_ops=False,
            grad_loss=None
            )
 **apply_gradients**
  minimize()的第二部分，返回一个执行梯度更新的ops
  该函数的作用是将compute_gradients()返回的值作为输入参数对variable进行更新

        apply_gradients(
            grads_and_vars,
            global_step=None,
            name=None
        )

####构建计算图
通过占位符来为输入图像和目标输出类别创建节点shape参数是可选的，有了它tensorflow可以自动捕获维度不一致导致的错误
原始输入

    x = tf.placeholder("float", shape=[None, 784])
目标值

    y_ = tf.placeholder("float", shape=[None, 10])

### Activation Functions

- [tf.nn.relu(features, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html#relu)
- [tf.nn.relu6(features, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html#relu6)
- [tf.nn.softplus(features, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.dropout(x, keep_prob, noise_shape=None, seed=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.bias_add(value, bias, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.sigmoid(x, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.tanh(x, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Convolution
- [tf.nn.conv2d(input, filter, strides, padding, use_cudnn_on_gpu=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.depthwise_conv2d(input, filter, strides, padding, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.separable_conv2d(input, depthwise_filter, pointwise_filter, strides, padding, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Pooling
- [tf.nn.avg_pool(value, ksize, strides, padding, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.max_pool(value, ksize, strides, padding, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.max_pool_with_argmax(input, ksize, strides, padding, Targmax=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Normalization
- [tf.nn.l2_normalize(x, dim, epsilon=1e-12, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.local_response_normalization(input, depth_radius=None, bias=None, alpha=None, beta=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.moments(x, axes, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Losses
- [tf.nn.l2_loss(t, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Classification
- [tf.nn.sigmoid_cross_entropy_with_logits(logits, targets, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.softmax(logits, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.softmax_cross_entropy_with_logits(logits, labels, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Embeddings
- [tf.nn.embedding_lookup(params, ids, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  #### Evaluation
- [tf.nn.top_k(input, k, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.in_top_k(predictions, targets, k, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
#### Candidate Sampling
##### Sampled Loss Functions
- [tf.nn.nce_loss(weights, biases, inputs, labels, num_sampled, num_classes, num_true=1, sampled_values=None, remove_accidental_hits=False, name='nce_loss')](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.sampled_softmax_loss(weights, biases, inputs, labels, num_sampled, num_classes, num_true=1, sampled_values=None, remove_accidental_hits=True, name='sampled_softmax_loss')](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  ##### Candidate Samplers
- [tf.nn.uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.log_uniform_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.learned_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, seed=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)
- [tf.nn.fixed_unigram_candidate_sampler(true_classes, num_true, num_sampled, unique, range_max, vocab_file='', distortion=0.0, num_reserved_ids=0, num_shards=1, shard=0, unigrams=[], seed=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)

  ##### Miscellaneous candidate sampling utilities
- [tf.nn.compute_accidental_hits(true_classes, sampled_candidates, num_true, seed=None, name=None)](http://www.tensorfly.cn/tfdoc/api_docs/python/nn.html)