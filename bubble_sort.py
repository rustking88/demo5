def bubble_sort(arr):
    """
    实现冒泡排序算法
    :param arr: 需要排序的列表
    :return: 排序后的列表
    """
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经排好序，不需要再比较
        for j in range(0, n-i-1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试冒泡排序函数
if __name__ == "__main__":
    # 创建一个包含随机数的示例数组
    example_arr = [11, 22, 33, 19, 30, 49]
    # 打印原始数组
    print("排序前的数组:", example_arr)
    # 调用冒泡排序函数对数组进行排序
    sorted_arr = bubble_sort(example_arr)
    # 打印排序后的结果
    print("排序后的数组:", sorted_arr) 
