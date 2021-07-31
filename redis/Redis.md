## Redis

### 要点：

- Redis是远程的
- Redis是基于内存的（因此高速）
- Redis是非关系型数据库

### 应用场景：

- 缓存  -- 不用每次都写sql语句，可以通过缓存提取数据

- 队列 -- pop弹出队列元素， push插入元素

- 数据存储 -- 可以进行增删改

### 启动并查看Redis

- 启动Redis服务

  redis-server.exe redis.windows.conf

  **注：**若端口启动过：

  ```
  1.redis-cli.exe
  2.shutdown
  3.exit
  4.redis-server.exe redis.windows.conf
  ```

  

- 启动Redis客户端

  `redis -cli -h 127.0.0.1 -p 7200`

- 查看Redis信息

  `info`

### Redis数据类型

| 数据类型 |                         存储的值                          |                   读写能力                    |
| :------: | :-------------------------------------------------------: | :-------------------------------------------: |
|  String  |           可以是字符串、整数或浮点，统称为元素            |          对字符串操作对整数类型加减           |
|   List   |          一个序列集合且每个节点都包好了一个元素           | 序列两端推入、或弹出元素 修剪、查找或移除元素 |
|   Set    |                      各不相同的元素                       |           从集合中插入或者删除元素            |
|   Hash   |     有key-value的散列组，其中key是字符串，value是元素     |              按照key进行增加删除              |
| Sort Set | 带分数的score-value有序集合，其中score为浮点，value为元素 |          集合插入，按照分数范围查找           |

- **String**

  类型：key | value(string/int/float)

  - 设置 a 为字符串‘woaidongdong’：

    `set a 'woaidongdong'`

  - 获取字符串a:

    `get a`

  - 设置字符串b为5，并进行增和减法(-2)

    `set b 5`

    `incr b`

    `decrby b 2`

- **List**

  类型：key -> value(12)       左

  ​					   value(13)

  ​					   value(14)       右

  基本的操作是push和pop,不要求数据是唯一的

  从左边push:

  `lpush list1 12`

  `lpush list1 13`

  右边pop:

  `rpop list1`

  >"12"

  列出list中元素

  llen  list1

- **Set**

  类型： key -> value(12)   

  ​					   value(13)

  ​					   value(14)  

  无序的方式存储不同的值。

  插入元素：

  `sadd set1 12`

  查看元素个数：

  `scard set1`

  查看元素是否在set集合中：

  `sismember set1 12`

  删除元素

  `srem set1 12`

- **hash**

  类型： key -> key1    |      value(string/int/float)   

  ​					   key2    |      value(string/int/float)

  ​					   key3    |      value(string/int/float)  

  插入元素：

  `hset hash1 key1 12`

  获取元素:

  `hget hash1 key1`
  
  查看元素个数：
  
  `hlen hash1`
  
  修改元素
  
  `hset hash1 key1 13`
  
  批量获取元素
  
  `hmget hash1 key1 key2`

- **sort set(有序分数集)**

  类型： key -> score(10,1)    |      value(string/int/float)     |  rank:1

  ​					    score(9,1)      |      value(string/int/float)     |  rank:0

  ​					    score(11,1)    |      value(string/int/float)     |  rank:2

  value是全局唯一，若score分数一样，则按照value字典顺序排列先后

  插入元素
  ```
  zadd zset1 10.1 val1

  zadd zset1 11.2 val2

  zadd zset1 9.2 val3
  ```
  查看元素个数

  `zcard zset1`

  查看元素0-2排名(从小到大)

  `zrange zset1 0 2 withscores`

  查看元素排名

  `zrank zset1 val2`

### Redis常用命令

- **String**

  |                      命令                      |                             解释                             |
  | :--------------------------------------------: | :----------------------------------------------------------: |
  |                    get key                     |                         获取key的值                          |
  |                 set key value                  |                         设置key的值                          |
  |                    del key                     |                  删除key（应用于所有类型）                   |
  |                    incr key                    |                       将储存的值加上1                        |
  |                    decr key                    |                       将储存的值减去1                        |
  |               incrby key amount                |                        加上整数amount                        |
  |               decrby key amount                |                        减去整数amount                        |
  |            incrbybyfloat key amout             |                 加上浮点数amount字符串二进制                 |
  |                append key value                |                将值追加到key当前储存值的末尾                 |
  |             getrange key start end             |                  获取下标start到end的字符串                  |
  |           setrange key offset value            | 将字符串看做二进制串，并将位串中偏移量为offset的二进制位的值 |
  |               getbit key offset                | 将字符串看做是二进制位串值为1的二进制位的数量，如果给定了可选的start偏移量和end偏移量，那么只对偏移量指定范围的二进制位进行统计 |
  | bitop operation dest-key key-name [key-name …] | 对一个或多个二进制位串进行 并and，或 or，异或XOR，非NOT 在内的任意一种安位运算符操作（bitwise operation），并将计算的结果放到dest -key里面 |

- **List**

  |         命令         |                  解释                   |
  | :------------------: | :-------------------------------------: |
  | rpush key [v1,v2...] |        将一个或多个加入列表右端         |
  | lpush key[v1,v2...]  |        将一个或多个加入列表左端         |
  |       rpop key       |       移除并返回列表最右端的元素        |
  |       lpop key       |       移除并返回列表最左端的元素        |
  |   lindex key size    |     返回下标（偏移量）为size的元素      |
  | lrange key start end |  返回从start到end的元素 包含start和end  |
  | ltrim key start end  | 只保留从start到end的元素 包含start和end |

- **Hash**

  |              命令               |             解释             |
  | :-----------------------------: | :--------------------------: |
  |        hmget hkey key...        |          获取多个值          |
  |       hmset hkey key v...       |       为多个key设置值        |
  |        hdel hkey key...         |       删除多个值并返回       |
  |            hlen hkey            |          返回总数量          |
  |        hexists hkey key         |    检查key是否存在散列中     |
  |           hkeys hkey            |      获取散列中所有key       |
  |           hvals hkey            |       获取三列中所有值       |
  |          hgetall hkey           |           获取散列           |
  |   hincrby hkey key increment    |  为key的值加上整数increment  |
  | hincrbyfloat hkey key increment | 为key的值加上浮点数increment |

- **Set**

  |                 命令                  |                             解释                             |
  | :-----------------------------------: | :----------------------------------------------------------: |
  |           sadd key item ...           |          添加多个，返回新添加的个数（已存在的不算）          |
  |           srem key item...            |           从集合移除多个元素，返回被移除元素的数量           |
  |          sismember key item           |                   检查元素item是否在集合中                   |
  |               scard key               |                         返回集合总数                         |
  |             smembers key              |                         返回所有元素                         |
  |         srandmember key cout          | 随机返回cout个元数cout为正整数 随机元素不重复 相反可能会出现重复 |
  |               spop key                |            随机的移除一个元素 并返回已删除的元素             |
  |         smove key1 key2 item          | 如果key1中包含item移除key1中的item 添加到key2中，成功返回1，失败返回0 |
  | 差运算 sdiffstore newkey key key1 ... | 将存在于key集合但是不存在key1...集合的其他元素放到newkey里面 |
  |         交运算 sinter key ...         |                      返回所有集合的交集                      |
  |   交运算 sinterstore newkey key ...   |               返回多个集合的交集生成集合newkey               |
  |         并运算 sunion key ...         |                     返回不重复的所有元素                     |
  |     并运算 sunion newkey key ...      |                       结果放到newkey中                       |

- **zset**

  |             命令             |              解释               |
  | :--------------------------: | :-----------------------------: |
  |  zadd key score member ...   |            添加多个             |
  |     zerm key member ...      |            移除多个             |
  |          zcard key           |          返回所有成员           |
  | zincrby key incremnet member | 将member成员的分值加上increment |
  |      zcount key min max      |  返回分值在min和max中间的排名   |
  |       zrank key member       |      返回成员member的分值       |
  |       zsore key member       |        返回member的分值         |
  |    zrange key start stop     |     返回 介于两者之间的成员     |

  