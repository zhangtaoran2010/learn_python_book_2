# # 圆弧旋转
# # 最终代码：
# def setup(): # 初始化函数，仅运行一次
#     global spanAngle,spanAngle,spanAngleSpeed 
#     size(600,600)  # 设定画面宽度、高度
#     noFill()       # 不填充
#     strokeWeight(3)# 设置线条的粗细
#     spanAngle = 0  # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 0.5 # 圆弧跨越的角度变化速度
    
# def draw():  # 绘制函数，每帧重复执行
#     global spanAngle,spanAngleSpeed # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2 * radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle # 求出圆弧起点长度
    
#     if spanAngle > 2 * PI or spanAngle < 0:# 当跨越角度达到2PI或0时
#       spanAngleSpeed = -spanAngleSpeed # 更改跨越角度变化速度的方向
      
#     for diam in range(50,width,50): # 圆弧直径从50开始遍历到width
#       angleShift = radians(360 * diam / width) # 不同直径圆弧有个偏移量
#       arc(width / 2,height / 2,diam,diam, # 绘制对应的各个圆弧
#           startAngle + angleShift,endAngle + angleShift)
      
#     for diam in range(50,width,50): # 圆弧直径从50开始遍历到width
#       angleShift = radians(360 * diam / width) # 不同直径圆弧有个偏移量
#       arc(width / 2,height / 2,diam,diam, # 绘制对应的各个圆弧
#           startAngle + angleShift,endAngle + angleShift)
# # 绘制圆弧
# # arc(x,y,width,height,stratAngle,endAngle)
# # 绘制一段圆弧
# # (x,y)为圆弧对应圆的圆心
# # (width,height)为对应圆外切矩形的宽度和高度
# # (startAngle,endAngle)为圆弧的起始角度、终止角度（顺时针方向，单位为弧度）
# def setup():    # 初始化函数，仅运行一次
#     size(600,600) # 设定画面宽度、高度
#     noFill()# 不填充
#     strokeWeight(3) # 设置线条的粗细
    
# def draw(): # 绘制函数，每帧重复执行
#     background(255) # 设置白色背景，并覆盖整个画面
#     arc(width/2,height/2,300,300,0,PI/2) # 绘制圆弧
# # PI为常量，表示圆周率
# # 角度从0到PI/2,绘制了四分之一个圆的圆弧
# # 练习：绘制笑脸
# def setup():
#     size(800,600)
#     strokeWeight(3)

# def draw():
#     background(255)
#     fill(255)
#     circle(400,300,500)
#     circle(305,180,180)
#     circle(495,180,180)
#     circle(400,300,40)
#     arc(400,380,250,180,0.1 * PI,0.9 * PI)  # 用圆弧绘制嘴巴
#     fill(0)
#     circle(275,180,110)
#     circle(465,180,110)
# # 圆弧的旋转：
# def setup(): # 初始化函数，仅运行一次
#     size(600,600)
#     noFill() # 不填充
#     strokeWeight(3) # 设置线条的粗细
    
# def draw():  # 绘制函数，每帧重复执行
#     background(255) # 设置白色背景，并覆盖整个画面
#     startAngle = radians(frameCount % 360) # 圆弧起始角度
#     endAngle = startAngle + PI/2 # 圆弧终止角度
#     arc(width/2,height/2,300,300,startAngle,endAngle) # 绘制圆弧
# # frameCount % 360从1增加到359，然后变成0，继续重复增加到359
# # radians()把[0,360]的度数转化为[0,2 * PI]的弧度
# # startAngle从0到PI循环变化,endAngle = startAngle + PI/2,实现圆弧的重复旋转
# # 全局变量
# def setup(): #  初始化函数，仅运行一次
#     global n
#     n = 0
# def draw(): # 绘制函数，每帧重复执行
#     print(n)
# # setup()函数中将变量n初始化为0
# # 为了在setup()函数中也能访问n，在setup()函数中添加代码global n，表示n为全局变量
# # draw()函数中既可以输出全局变量n的值
# # 利用全局变量实现圆弧变长
# def setup(): # 初始化函数，仅运行一次
#     global n
#     n = 0
    
# def draw(): # =绘制函数，每帧重复执行
#     global n
#     n = n + 1
#     print(n)
# # draw()函数中添加n = n + 1,表示让n的数值每帧增加1
# # draw()函数中修改全局变量n的值，也许添加语句global n
# # 不用frameCount，使用全局变量实现逐渐变大的圆圈
# def setup():
#     global diameter
#     size(600,600)
#     fill(200)
#     diameter = 1
    
# def draw():
#     global diameter
#     background(255)
#     diameter = diameter + 1
#     circle(300,300,diameter)
# # 利用全局变量实现圆弧变长
# def setup():   # 初始化函数，仅运行一次
#     global spanAngle # 全局变量
#     size(600,600)    # 设定画面宽度、高度
#     noFill() # 不填充
#     strokeWeight(3)  # 设置线条的粗细
#     spanAngle = 0    # 圆弧跨越的角度，初始为0
    
# def draw():    # 绘制函数，每帧重复执行
#     global spanAngle # 全局变量
#     background(255) # 设置白色背景，并覆盖整个画面
#     spanAngle = spanAngle + radians(1) # 圆弧跨越的角度逐渐增加
#     arc(width/2,height/2,300,300,0,spanAngle) # 绘制圆弧
# # 角度跨越范围spanAngle逐渐增加
# def setup():   # 初始化函数，仅运行一次
#     global spanAngle # 全局变量
#     size(600,600)    # 设定画面宽度、高度
#     noFill() # 不填充
#     strokeWeight(3)  # 设置线条的粗细
#     spanAngle = 0    # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 1  # 圆弧跨越角度变化速度
    
# def draw():    # 绘制函数，每帧重复执行
#     global spanAngle # 全局变量
#     background(255) # 设置白色背景，并覆盖整个画面
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越的角度增加
#     arc(width/2,height/2,300,300,0,spanAngle) # 绘制圆弧
# # if语句实现圆弧长度重复变化
#  def setup():   # 初始化函数，仅运行一次
#     global spanAngle # 全局变量
#     size(600,600)    # 设定画面宽度、高度
#     noFill() # 不填充
#     strokeWeight(3)  # 设置线条的粗细
#     spanAngle = 0    # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 1  # 圆弧跨越角度变化速度  
     
# def draw():    # 绘制函数，每帧重复执行
#     global spanAngle # 全局变量
#     background(255) # 设置白色背景，并覆盖整个画面
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越的角度增加
#     if spanAngle > 2 * PI:     # 当跨越角度达到2PI时
#         spanAngleSpeed = -spanAngle # 更改跨越角度变化速度的方向
#     arc(width/2,height/2,300,300,0,spanAngle) # 绘制圆弧
# # 当spanAngle大于2 * PI时，执行冒号后的spanAngleSpeed =-spanAngleSpeed，将圆弧跨越角度变化速度反向，圆弧长度开始变小
# # if语句（选择判断语句）
# # python共有6种运算符判断两个数字的大小关系：
# # |---------|-----------|
# # |  表达式 |  含义     |
# # |  x > y  | x是否大于y|
# # |  x < y  | x是否小于y|
# # |  x == y | x是否等于y|--
# # |  x != y | x是否不等于y|----
# # |  x >= y | x是否大于或等于y|
# # |  x <= y | x是否小于或等于y|
# # |---------------------------|
# # 例如：
# x = 3
# y = 5
# if x > y:
#     print("x > y")
# if x == y:
#     print("x == y")
# if x < y:
#     print("x < y")
# # 练习：编程计算11 * 13 * 15 * 17，并用if语句判断结果是否大于30000
# a = 11
# b = 13
# c = 15
# d = 17
# if a * b * c * d > 30000:
#     print("11 * 13 * 15 * 17 > 3000")
# else:
#     print("11 * 13 * 15 * 17不大于3000")
# # if语句实现圆弧长度重复变化
# def setup():   # 初始化函数，仅运行一次
#     global spanAngle # 全局变量
#     size(600,600)    # 设定画面宽度、高度
#     noFill() # 不填充
#     strokeWeight(3)  # 设置线条的粗细
#     spanAngle = 0    # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 1  # 圆弧跨越角度变化速度  
     
# def draw():    # 绘制函数，每帧重复执行
#     global spanAngle # 全局变量
#     background(255) # 设置白色背景，并覆盖整个画面
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越的角度增加
#     if spanAngle > 2 * PI:     # 当跨越角度达到2PI时
#         spanAngleSpeed = -spanAngle # 更改跨越角度变化速度的方向
#     if spanAngle < 0: # 当跨越角度小于0时
#         spanAngleSpeed =-spanAngle    # 更改跨越角度变化速度的方向
#     arc(width/2,height/2,300,300,0,spanAngle) # 绘制圆弧
# # 当spanAngle大于2 * PI时，将圆弧跨越角度变化速度反向，圆弧长度开始变小
# # 当spanAngle小于0时，再让变化速度反向，又让圆弧长度开始增加
# # 逻辑运算符
# print(3 > 2)   # 输出：True
# print(4 < 5)   # 输出：False
# # not
# print(not(3 > 2)) # 输出：True
# print(not(4 > 5)) # 输出：False
# # or and
# print((3 > 2) or (4 > 5))  # 输出：True
# print((3 > 2) and (4 . 5)) # 输出：False
# # Python有三个逻辑运算符，方便进行多个判断条件的组合：not（非）、and（与）、or（或）
# # 练习：利用if语句实现圆弧长度重复变大、变小的效果
# def setup():
#     global diameter,diamSpeed
#     size(600,600)
#     fill(200)
#     diameter = 1
#     diamSpeed = 2
# def draw():
#     global diameter,diamSpeed
#     background(255)
#     diameter = diameter + diamSpeed
#     if diameter > width or diameter < 1:
#         diamSpeed = -diamSpeed
#     circle(300,300,diameter)  
# 圆弧同时旋转与长度变化
# def setup(): # 初始化函数，仅运行一次
#   global spanAngle,spanAngle,spanAngleSpeed 
#   size(600,600)  # 设定画面宽度、高度
#   noFill()       # 不填充
#   strokeWeight(3)# 设置线条的粗细
#   spanAngle = 0  # 圆弧跨越的角度，初始为0
#   spanAngleSpeed = 0.5 # 圆弧跨越的角度变化速度
  
# def draw():  # 绘制函数，每帧重复执行
#     global spanAngle,spanAngleSpeed # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2 * radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle # 求出圆弧起点长度
#     if spanAngle > 2 * PI or spanAngle < 0:# 当跨越角度达到2PI或0时
#       spanAngleSpeed = -spanAngleSpeed # 更改跨越角度变化速度的方向
#     arc(width/2, height/2, 300, 300, startAngle, endAngle) # 绘制圆弧 
# 多层圆弧效果
def setup(): # 初始化函数，仅运行一次
#     global spanAngle,spanAngle,spanAngleSpeed 
#     size(600,600)  # 设定画面宽度、高度
#     noFill()       # 不填充
#     strokeWeight(3)# 设置线条的粗细
#     spanAngle = 0  # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 0.5 # 圆弧跨越的角度变化速度
    
# def draw():  # 绘制函数，每帧重复执行
#     global spanAngle,spanAngleSpeed # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2 * radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle # 求出圆弧起点长度
    
#     if spanAngle > 2 * PI or spanAngle < 0:# 当跨越角度达到2PI或0时
#       spanAngleSpeed = -spanAngleSpeed # 更改跨越角度变化速度的方向
      
#     for diam in range(50,width,50): # 圆弧直径从50开始遍历到width
#       arc(width / 2,height / 2,diam,diam,startAngle,endAngle) # 绘制圆弧
# for循环中变量diam从50逐渐增加到width，绘制多层圆弧效果
# 多层圆弧效果
# def setup(): # 初始化函数，仅运行一次
#     global spanAngle,spanAngle,spanAngleSpeed 
#     size(600,600)  # 设定画面宽度、高度
#     noFill()       # 不填充
#     strokeWeight(3)# 设置线条的粗细
#     spanAngle = 0  # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 0.5 # 圆弧跨越的角度变化速度
    
# def draw():  # 绘制函数，每帧重复执行
#     global spanAngle,spanAngleSpeed # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2 * radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed) # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle # 求出圆弧起点长度
    
#     if spanAngle > 2 * PI or spanAngle < 0:# 当跨越角度达到2PI或0时
#       spanAngleSpeed = -spanAngleSpeed # 更改跨越角度变化速度的方向
      
#     for diam in range(50,width,50): # 圆弧直径从50开始遍历到width
#       angleShift = radians(360 * diam / width) # 不同直径圆弧有个偏移量
#       arc(width / 2,height / 2,diam,diam, # 绘制对应的各个圆弧
#           startAngle + angleShift,endAngle + angleShift)
      
#     for diam in range(50,width,50): # 圆弧直径从50开始遍历到width
#       angleShift = radians(360 * diam / width) # 不同直径圆弧有个偏移量
#       arc(width / 2,height / 2,diam,diam, # 绘制对应的各个圆弧
#           startAngle + angleShift,endAngle + angleShift)
# 本章小结：
# 学习了全局变量、if选择判断、比较大小运算符、逻辑运算符等语法知识
# 学习了圆弧的绘制
# 学习实现理发店标志转灯等效果
