import string

# 模板文件路径
fileConfig = open('C:\\Users\\24676\\Desktop\\config.txt', 'r')
# 数据源路径
fileSource = open('C:\\Users\\24676\\Desktop\\checkadd.txt', 'r')
# 生成的文件路径
fileOutput = open('C:\\Users\\24676\\Desktop\\out.txt', 'w')

# 读取模板文件 读出的是一个字符串
config = fileConfig.read();
# 不加换行 输出文件的数据会连接在一起不会分段
config+="\n"

# 读取一行数据源数据
line = fileSource.readline()
# 循环一行一行地读取数据源数据 循环中包含将数据填入模板中的流程
while line:
    # 将每一行的数据 根据空格 拆分成两段
    line_list=line.split()

    # 控制台打印出拆分后的数据
    # print(line_list[0]+','+line_list[1])

    # 加载模板
    temple = string.Template(config)
    # 将从数据源读取到的数据 填入模板中 并输出到文件
    fileOutput.write(temple.substitute(var1=line_list[0], var2=line_list[1]))
    # 将line重新赋值 这是while的循环条件 如果读取到最后一行 line就是null 会跳出循环
    line = fileSource.readline()

# 关闭文件流
fileOutput.close()
fileSource.close()
fileOutput.close()




