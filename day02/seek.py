"""
seek.py  文件偏移量示例

注意: 1. 每次open 打开文件文件偏移量都在开头　
　　　2. 已ａ方式打开时文件偏移量在结尾
　　　3. 读写操作共用一个文件偏移的
"""

f = open('test','rb+') #　读写

data = f.read(5)
print("文件偏移量：",f.tell()) # 查看文件偏移量

f.seek(10,2)  #　操作文件偏移量位置

f.write(b"&&&")



f.close()