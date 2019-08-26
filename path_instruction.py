import os

'''
绝对路径：从盘符开始的完整路径，如: a = open(r'C:\Users\lenovo\Desktop\新建文本文档.txt')
相对路径：从当前路径开始的路径，如当前路径在C:\Users\lenovo\Desktop, a = open('新建文本文档.txt')
'''

# 根据相对路径的.获取当前的绝对路径
print(os.path.abspath('.'))          # C:\Users\lenovo
# 相对路径..表示上一级目录
print(os.path.abspath('..'))           # C:\Users
# 判断目录是否存在,括号内是路径名
print(os.path.exists('/Users/lenovo'))      # True
# 判断是否是目录
print(os.path.isdir('/Users/lenovo'))          # True
# 判断是否是文件
print(os.path.isfile('d:/PY/zodiac'))            # False
print(os.path.isfile('d:/PY/zodiac.py'))          # True
# 路径的连接 os.path.join(path, *paths)

# 指定工作路径
os.chdir(r'D:\PY')

# 输出字符串指示正在使用的平台；如果是Windows则用'nt'表示，如果是Linux/Unix则用posix表示
print(os.name)           

# 返回工作路径
print(os.getcwd())                 # 返回当前脚本文件所在的工作路径

# 返回工作路径下的目录文件名
print(os.listdir())

# 将文件路径分割成目录和文件名，返回元组
x = os.path.split(r'C:\Users\lenovo\Desktop\新建文本文档.txt')
print(x, type(x))                  # ('C:\\Users\\lenovo\\Desktop', '新建文本文档.txt') <class 'tuple'>


# 删除文件，就地操作，直接删除了，谨慎操作
# os.remove(r'C:\Users\lenovo\Desktop\新建文本文档.txt')  # 如果文件在工作路径下，参数只需要写文件名即可









from pathlib import Path
# 根据相对路径的.获取当前的绝对路径
p = Path('.')                             # 与os不同，pathlib里要先进行封装
print(p.resolve())                              # C:\Users\lenovo
# 创建目录
p1 = Path('d:/PY/Test')          # 先将要创建的目录封装
Path.mkdir(p1)       # mkdir来进行创建
p2 = Path('d:/PY/Test/a')       # 如果要创建的目录有两层以上,如PY为已有目录，在该目录下创建Test,并且在Test里再创建a目录
Path.mkdir(p2, parents=True)     # 此时，parents要为True,则能创建目录，为False则出现错误“找不到指定路径”