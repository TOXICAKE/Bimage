# [Bimage]

  这是一个方便解一种CTF MISC题目的工具。当遇到大量相似度很高的图片时，可以用这个工具尝试这些图片是否代表二进制字串。大量相似度很高的图片可以是一个文件夹中有多张图片，也可以是一张gif，还可以是组合成的一张大图。*by N0P3.*

## 图像解码:

**一个文件夹中有大量图片：**使用 [-d]+['文件夹路径'] 来打开文件夹。使用 [-p]+['目标像素坐标'] 来指定要检查的像素。例如: Bimage.py -d test -p "0,0" 打开文件夹‘test’以每张图片的左上角第一个坐标为检像素。

**包含多帧的gif:**  使用 [-g]+['Gif文件路径'] 来打开文件。使用 [-o]+['输出文件夹路径'] 来指定分解后的图片储存位置。分解后再用【一个文件夹中有大量图片】去解。

**多张图组合的大图(未完成):**

## 生成图像：

(未完成)

## 二进制串与字符串互转：

**二进制串转字符串:** [-b]+['二进制字符串'] 例如：Bimage.py -b "1001110 110000 1010000 110011"
**字符串转二进制串:** [-s]+['字符串'] 例如：Bimage.py -s "Hello"

ps: 示例【test】文件夹来自攻防世界 (xctf) MISC新手区【gif】一题，侵删。