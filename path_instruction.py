import os

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


from pathlib import Path
# 根据相对路径的.获取当前的绝对路径
p = Path('.')                             # 与os不同，pathlib里要先进行封装
print(p.resolve())                              # C:\Users\lenovo
# 创建目录
p1 = Path('d:/PY/Test')          # 先将要创建的目录封装
Path.mkdir(p)       # mkdir来进行创建
p2 = Path('d:/PY/Test/a')       # 如果要创建的目录有两层以上,如PY为已有目录，在该目录下创建Test,并且在Test里再创建a目录
Path.mkdir(p, parents=True)     # 此时，parents要为True,则能创建目录，为False则出现错误“找不到指定路径”