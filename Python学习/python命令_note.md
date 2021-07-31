## python好用命令

###  1、随机排列一个序列，打乱顺序

#### 语法格式：

    numpy.random.permutation(x) 
随机排列一个序列，或者数组。
如果x是多维数组，则沿其第一个坐标轴的索引随机排列数组。
#### 参数:  
**x :** 整数或者数组
如果x是整数，则随机排列np.arange(x)。若果x是数组，对其复制之后再搅乱其元素。

#### 返回: 
out : 排列的序列或数组

    np.random.permutation(10)
输出：

    array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6])
    
    np.random.permutation([1, 4, 9, 12, 15])
输出：

    array([15,  1,  9,  4, 12])
若

    arr = np.arange(9).reshape((3, 3))
    np.random.permutation(arr)
输出：

    array([[6, 7, 8],
        [0, 1, 2],
        [3, 4, 5]])

### 2、断言函数

assert 断言语句和 if 分支有点类似，它用于对一个 bool 表达式进行断言，如果该 bool 表达式为 True，该程序可以继续向下执行；否则程序会引发 AssertionError 错误。

例如如下程序： 

```
s_age = input("请输入您的年龄:")
age = int(s_age)
assert 20 < age < 80print("您输入的年龄在20和80之间")
```

 上面程序中，使用 asser 语句断言 age 必须位于 20 到 80 之间。运行上面程序，如果输入的 age 处于执行范围之内，则可看到如下运行过程：
```
 请输入您的年龄:23
 您输入的年龄在20和80之间
```
 如果输入的 age 不处于 20 到 80 之间，将可以看到如下运行过程： 
```
 请输入您的年龄:1
 Traceback (most recent call last):
   File "C:\Users\mengma\Desktop\1.py", line 3, in <module>
     assert 20 < age < 80
 AssertionError
```
 从上面的运行过程可以看出，断言也可以对逻辑表达式进行判断，因此实际上断言也相当于一种特殊的分支。

assert 断言的执行逻辑是：
```
 if 表达式的值为 True：
     程序继续运行；
 else：     # 表示式的值为 False
     程序引发 AssertionError 错误
```

### 3、setdefault用法

在python中，我们学过了通过append和insert来给列表插入值，那在词典中，可以通过setdefault来给词典插入值，方法如下

```
dic1={"name":"fen","age":32}

r=dict1.setdefault("age",45)

dic2={"name":"fen","age":32}

b=dic2.setdefault("money",32000)


dic1 ----- {"name":"fen","age":32}
  r  ----- 32
dic2 ----- {"name":"fen","age":32,"money":32000}
  b  ----- 32000
```

注：当原词典中有该键值时，则不对原键值做改动，返回原来的键值

当原词典中没有该键值时，则新增该键和对应的值，并返回键值