# def draw():
#     print(frameCount % 10)

# def setup():
#     size(600,600)
#     frameRate(30)
    
# def draw():
#     background(255)
#     fill(200)
#     circle(300,300,10 * frameCount % width)
# 需要先绘制大圆，避免小圆被大圆覆盖
def setup():
    size(600,600)
    
def draw():
    background(255)
    noFill()
    circle(300,300,250)
    circle(300,300,200)
    circle(300,300,150)
    circle(300,300,100)
    circle(300,300,50)
# 绘制同心圆：
def setup():
    size(600,600)
    
def draw():
    background(255)
    noFill()
    circle(300,300,50)
    circle(300,300,100)
    circle(300,300,150)
    circle(300,300,200)
    circle(300,300,250)
# 绘制十个同心圆：
def setup():
    size(600,600)
    
def draw():
    background(255)
    noFill()
    circle(300,300,50)
    circle(300,300,100)
    circle(300,300,150)
    circle(300,300,200)
    circle(300,300,250)
    circle(300,300,300)
    circle(300,300,350)
    circle(300,300,400)
    circle(300,300,450)
    circle(300,300,500)
# 利用for循环语句绘制同心圆：
def setup():
    size(600,600)
def draw():
    background(255)
    noFill()
    for diam in range (50,501,50):
        circle(300,300,diam)
# for语句:
for i in range(5):
    print(i)
# 关于for语句：
# range（范围），range（5）表示从0开始、小于5的整数：0、1、2、3、4
# for和in是关键字，表示变量i依次取range（5）范围内的五个数字
# 循环执行冒号后的print（i）语句，依次输出0、1、2、3、4
#冒号后的语句向后缩进一个单位
# 练习：修改代码的输出：
for i in range(10):
    print(i)
for i in range(5):
    print(i + 1)
for i in range(1,51,10):
    print(i)
# 设定range()两端的取值范围：
for i in range(3,6):
    print(i)
# range()也可以设定两端整数的取值范围，变量i取值范围是从3开始，小于六的整数，输出结果为：3、4、5
# 用for语句绘制20层同心圆：
def setup():
    size(600,600)
    noFill()
    frameRate(30)
    
def draw():
    background(255)
    for diam in range(1,21):
        circle(300,300,30 * diam)
# range设置步长：
for i in range(1,10,2):
    print(i)
# 输出从1开始，每次增加2，且小于10的整数
# 例子：
def draw():
    background(255)
    for diam in range(5,width + 1,20):
        circle(300,300,diam)
# range取值递减：
for i in range(10,1,-2):
    print(i)
# 练习：尝试用递减的方法画出多层同心圆：
def setup():
    size(600,600)
    noFill()
    frameRate(30)
    
def draw():
    background(255)
    for diam in range(width,1,-20):
        circle(300,300,diam)
# 所有同心圆直径逐渐变大：
def setup():
    size(600,600)
    noFill()
    frameRate(30)
    
def draw():
    background(255)
    for diam in range(5,width + 1,20):
        circle(300,300,(diam + frameCount) % width)
# 设置圆圈线条的粗细
def setup():
    size(600,600)
    noFill()
    strokeWeight(3)                  # 设置线条的粗细，值越大，线条越粗；不设置，线条粗细默认为1
    frameRate(30)
    
def draw():
    background(255)
    for diam in range(5,width + 1,20):
        circle(300,300,(diam + frameCount) % width)
# 线条颜色逐渐变淡
def setup():
    size(600,600)
    noFill()
    strokeWeight(3)                  # 设置线条的粗细，值越大，线条越粗；不设置，线条粗细默认为1
    frameRate(30)
    
def draw():
    background(255)
    for diam in range(5,width + 1,20):
        d = (diam + 2 * frameCount) % width
        stroke(map(d,0,width,0,255))
        circle(300,300,d)
# stroke()设定绘制图形线条的亮度，0为最暗，255为最亮
# 同心圆直径d随着帧数重复变大
# 用map()将d从[0,width]映射到[0,255],同心圆半径越大，越接近白色
# 添加注释：
def setup():         # 初始化函数，仅运行一次
    size(600,600)    # 设定画面宽度、高度
    noFill()         # 不填充 
    strokeWeight(3)  # 设置线条的粗细，值越大，线条越粗；不设置，线条粗细默认为1
    frameRate(30)    # 设置帧率
    
def draw():          # 绘制函数，每帧重复执行
    background(255)  # 设置白色背景，并覆盖整个画面
    for diam in range(5,width + 1,20): # 直径从小遍历到画面宽度
        d = (diam + 2 * frameCount) % width # 当前圆圈的直径
        stroke(map(d,0,width,0,255)) # 设置当前圆圈线条颜色
        circle(300,300,d)            # 绘制圆心在画面中心，直径为d的圆圈
# --------------------------------------------------------------------------------
# 盯着同心圆中心5秒，再看其他物体，会有其他物体在收缩变形的错觉
# 小结：
# &学习了整除、取余、for循环等语法知识
# &学习了帧数帧率、设置线条等用法
        
    

    



    
