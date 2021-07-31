### 用tf的VocabularyProcessor创建词汇表vocab

    from tensorflow.contrib import learn
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
其中VocabularyProcessor（max_document_length,min_frequency=0,vocabulary=None, tokenizer_fn=None)的构造函数中有4个参数
- **max_document_length**是文档的最大长度。如果文本的长度大于最大长度，那么它会被剪切，反之则用0填充
- **min_frequency**词频的最小值，出现次数>最小词频 的词才会被收录到词表中
- **vocabulary CategoricalVocabulary**对象，不太清楚使用方法
- **tokenizer_fn tokenizer function**讲句子或给定文本格式 token化得函数，可以理解为分词函数

### token化

    vp = learn.preprocessing.VocabularyProcessor(10, tokenizer_fn=list)
    x = list(vp.fit_transform(["abc", "bbd"]))
    print(x)
创建一个长为10的词表，然后将字符串token化得到结果为

    [array([1,2,3,0,0,0,0,0,0,0],dtype=int64),array([2,2,4,0,0,0,0,0,0,0],dtype=int64)]
也可以结合中文来做，当然tokenizer_fn要与文本相适应，可以实现自己的tokenizer function，如

    from jieba import cut
    from tensorflow.contrib import learn
    import numpy as np
    
    DOCUMENTS = [
        '这是一条测试1',
        '这是一条测试2',
        '这是一条测试3',
        '这是其他测试',
    ]
    def chinese_tokenizer(docs):
        for doc in docs:
            yield list(cut(doc))
    vocab = learn.preprocessing.VocabularyProcessor(10, 0, tokenizer_fn=chinese_tokenizer)
    x = list(vocab.fit_transform(DOCUMENTS))
    print(np.array(x))
这里中文引入了jieba分词，实现了自己的tokenizer函数，输出结果如下：

    [[1,2,3,4,0,0,0,0,0,0]
    [1,2,3,5,0,0,0,0,0,0]
    [1,2,3,6,0,0,0,0,0,0]
    [1,7,3,0,0,0,0,0,0,0]]
CategoricalVocabulary 对象可以先构建一个词典，再做token化，还是不太熟，但是有一个小demo可以示范：

    vocab = learn.preprocessing.CategoricalVocabulary()
    vocab.get("A")
    vocab.get("B")
    vocab.freeze()
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length=4,
                                                            vocabulary=vocab,
                                                            tokenizer_fn=list)
    tokens = vocab_processor.fit_transform(["ABC", "CBABAF"])
    print(np.array(list(tokens)))
这里预先创建了一个词典，添加了"A","B" 进去，并且设置最大文本长度为4，结果如下

    [[1 2 0 0]
    [0 2 1 2]]
我们可以还可以观察得到的词典，以dict的形式输出 这是一个 词--->词表id的映射

    vocab_dict = vocab.vocabulary_._mapping
    print(vocab_dict)
分别输出以上的中文词表，和通过CategoricalVocabulary构建的词表如下

    {'< UNK >'： 0, '这是'：1, '一条':2, '测试':3, '1':4, '2':5, '3':6, '其他':7}
    {'< UNK >'： 0, 'A'：1, 'B':2}
反向的索引 即 词表id--->词的映射 这是一个列表

    print(vocab_dict)
    print(vocab.vocabulary_._reverse_mapping)
    
    {'< UNK >', '这是', '一条', '测试', '1', '2', '3', '其他'}
可以通过id索引到词

    vocab.vocabulary_.reverse(3)

输出 在词表中id为3的词