# def setup():
#     size(600,600)
    
# def draw():
#     background(255)
#     fill(200)
#     diam = map(mouseY,0,height,1,1000)
#     circle(300,300,diam)
# def draw():
#     print(frameCount)

# def setup():
#     size(600,600)

# def draw():
#     background(255)
#     fill(200)
#     circle(300,300,frameCount)

# def setup():
#     frameRate(30)
    
# def draw():
#     print(frameRate)

# def setup():
#     size(600,600)
#     frameRate(30)
    
# def draw():
#     background(255)
#     fill(200)
#     circle(300,300,frameCount * 10)

# print(5.0 / 2) # 小数除法
# print(5 / 2) # 整数除法
# print(5%2) # 整数取余
# print(1/5.0) # 一般除法
# print(2/5) # 整数除法

# def draw():
#     print(frameCount % 10)
    
# def setup():
#     size(600,600)
#     frameRate(30)
    
# def draw():
#     background(255)
#     fill(200)
#     circle(300,300,frameCount % width)
# # print(3%5) # 整数取余
# # print(6%5) # 整数取余
# # print(10%5) # 整数取余

# def setup():
#     size(600,600)
    
# def draw():
#     background(255)
#     fill(200)
#     circle(300,300,250)
#     circle(300,300,200)
#     circle(300,300,150)
#     circle(300,300,100)
#     circle(300,300,50)

# def setup():
#     size(600,600)
# def draw():
#     background(255)
#     noFill()
#     circle(300,300,50)
#     circle(300,300,100)
#     circle(300,300,150)
#     circle(300,300,200)
#     circle(300,300,250)
#     circle(300,300,300)
#     circle(300,300,350)
#     circle(300,300,400)
#     circle(300,300,450)
#     circle(300,300,500)

# def setup():
#     size(600,600)
    
# def draw():
#     background(255)
#     noFill()
#     for diam in range(50,501,50):
#         circle(300,300,diam)
# for i in range(5):
#     print(i)

# for i in range(1,10):
# print(i)
# for i in range(1,6):
# print(i)
# for i in range(1,10,2):
# print(i)
# for i in range(3,6):
#     print(i)
# for i in range(10,16):
#     print(i)
# for i in range(10,51,10):
#     print(i)

# def setup():
#     size(600,600)
# def draw():
#     background(255)
#     noFill()
#     circle(300,300,1)
#     circle(300,300,2)
#     circle(300,300,3)
#     circle(300,300,4)
#     circle(300,300,5)
#     circle(300,300,6)
#     circle(300,300,7)
#     circle(300,300,8)
#     circle(300,300,9)
#     circle(300,300,10)
#     circle(300,300,11)
#     circle(300,300,12)
#     circle(300,300,13)
#     circle(300,300,14)
#     circle(300,300,15)
#     circle(300,300,16)
#     circle(300,300,17)
#     circle(300,300,18)
#     circle(300,300,19)
#     circle(300,300,20)

# def setup():
#     size(600,600)
#     noFill()
#     frameRate(30)
    
# def draw():
#     background(255)
#     for diam in range(1,21):
#         circle(300,300,30 * diam)
# for i in range(1,10,2):
#     print(i)
    
# def setup():
#     size(600,600)
#     noFill()
#     frameRate(30)
    
# def draw():
#     background(255)
#     for diam in range(5,width + 1,20):
#         circle(300,300,diam)
# for i in range(10,1,-2):
#     print(i)

# def setup():
#     size(600,600)
#     noFill()
#     frameRate(30)
# def draw():
#     background(255)
#     for diam in range(5,width + 1,20 ):
#         circle(300,300,(diam + frameCount) % width) 
# def setup():
#     size(600,600)
#     noFill()
#     strokeWeight(3)
#     frameRate(30)
    
# def draw():
#     background(255)
#     for diam in range(5,width + 1,20):
#         circle(300,300,(diam + frameCount) % width)

# def setup():
#     size(600,600)
#     strokeWeight(3)
#     noFill()
#     frameRate(30)
    
# def draw():
#     background(255)
#     for diam in range(5,width + 1,20):
#         d = (diam + 2 * frameCount) % width
#         stroke(map(d,0,width,0,255))
#         circle(300,300,d)

def setup(): # 初始化函数，仅运行一次
    size(600,600) # 设定画面宽度、高度
    strokeWeight(3) # 设置线条粗细
    noFill() # 不填充
    frameRate(30) # 设置帧率
    
def draw(): #绘制函数，每帧重复执行
    background(255) # 设置白色背景，并覆盖整个画面
    for diam in range(5,width + 1,20): # 直径从小遍历到画面宽度
        d = (99999999 + diam - frameCount*2) % width # 当前圆的直径
        stroke(map(d,0,width,0,255)) # 设置当前圆圈线条颜色
        circle(300,300,d) # 绘制圆心在画面中心，直径为d的圆圈 
    
