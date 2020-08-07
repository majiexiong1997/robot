
        timer_type = {

            'continue':1,
            'timeout':2,

        }
import functools
import time


class MyTimer:
    # 开始计时
    def start(self):
        self.begin = time.localtime()
        self.prompt = '提示：请先用stop()停止计时'
        print('开始计时')

    # 停止计时
    def stop(self):
        if not self.begin:
            print('提示：请先用start()开始计时')
        else:
            self.end = time.localtime()
            self._calc()
            print('计时结束')

    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt  # 重写__str__魔法方法，程序在调用print函数时，打印当时状态的prompt内容

    __repr__ = __str__  # 将__repr__和__str__相同化

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []  # 制作一个空列表，存放每个单位相减的值
        self.prompt = '总共运行了'
        for index in range(6):
            temp = self.end[index] - self.begin[index]
            if temp < 0:
                i = 1
                while self.lasted[index - i] < 1:  # 向前边的位数借
                    self.lasted[index - i] += self.borrow[index - i] - 1
                    self.lasted[index - i - 1] -= 1
                    i += 1  # 向更高位借
                print(self.lasted)
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index - 1] -= 1
            else:
                self.lasted.append(temp)
        for index in range(6):
            print(self.lasted)
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0


t1 = MyTimer()


# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         t1.start()
#         value = func(*args, **kwargs)
#         t1.stop()
#         print('{} 共用时：{}'.format(func.__name__, t1))
#         return value, t1
#
#     return wrapper


def fuc_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        time_consuming = end_time - start_time
        print(time_consuming)
        return value, time_consuming
    return wrapper



if __name__ == '__main__':
    t1 = MyTimer()
    t1.start()
    time.sleep(5)
    t1.stop()
    print(t1)
