# 给定一个已排序的数组nums，就地删除重复项，以使每个元素仅出现一次并返回新的长度。
#
# 不要为另一个数组分配额外的空间，必须通过使用O（1）额外的内存就地修改输入数组来做到这一点。
#
# 范例1：
#
# 给定nums = [1,1,2]，
#
# 您的函数应返回length = 2，且nums的前两个元素分别为1和2。
#
# 剩下的长度与返回的长度无关紧要。范例2：
#
# 给定nums = [0,0,1,1,1,2,2,3,3,4]，
#
# 您的函数应返回length = 5，并将nums的前五个元素分别修改为0、1、2、3和4。
#
# 超出返回的长度设置什么值都没有关系。澄清：
#
# 困惑为什么返回值是整数但答案是数组？
#
# 请注意，输入数组是通过引用传递的，这意味着调用者也将知道对输入数组的修改。
#
# 在内部，您可以想到：
#
# // nums通过引用传递。（即不制作副本）int len = removeDuplicates（nums）;
#
# //调用者将知道对函数中nums的任何修改。//使用函数返回的长度，它将打印前len个元素。


def function(num):
    if not num:
        return 0
    length = 0
    for index in range(1,len(num)):
        if num[index] != num[length]:
            length += 1
            num[length] = num[index]
    print(length+1)




if __name__ == '__main__':
    num = [0,0,1,1,1,2,2,3,3,4]
    result = function(num)