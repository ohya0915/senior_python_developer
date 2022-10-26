

class google_phone():
    def __init__(self):
        self.price = 10
        self.camera_count = 3
        self.screen_size = 5

    def special_freature(self, data):
        '''
        輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
        例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]
        '''
        result = []
        for value in data:
            if value % 2 == 0 and value > 10:
                result.append(value)
                result.sort(reverse=True)
        return result


class taiwan_phone():
    def __init__(self):
        self.price = 20
        self.camera_count = 1
        self.screen_size = 3

    def _factorial(self, number):
        '''
        輸入一個數字返回該數字階乘
        '''
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    def _fibonacci(self, number):
        '''
        輸入一個數字返回該數字Fibonacci 斐波那契數
        '''
        n = number
        result = 0
        if n < 0:
            return "輸入錯誤"
        elif n == 0:
            return result
        elif n == 1 or n == 2:
            result = 1
            return result
        else:
            result = self._fibonacci(n-1) + self._fibonacci(n-2)
            return result

    def special_freature(self, number):
        '''
        輸入一個數字自動計算 Fibonacci 斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
        例如: 輸入 10 回傳 120
        '''
        n = number 
        result = 0
        if n < 0:
            return "輸入錯誤"
        elif n == 0:
            return result
        elif n == 1 or n == 2:
            result = 1
            return result
        n = self._fibonacci(n)
        str_n = str(n)
        if len(str_n) < 2:
            return '這數字沒有十位數'
        x = int(str_n[-2:-1])
        y = int(str_n[-1:])
        if x - y < 0:
            return 'Fibonacci 斐波那契數列的十位數減個位數為負的' 
        result = self._factorial(x) / self._factorial(x - y)
        return int(result)


if __name__ == '__main__':
    google_phone = google_phone()
    print(google_phone.special_freature([3, 43, 62, 15, 18, 22]))
    taiwan_phone = taiwan_phone()
    print(taiwan_phone.special_freature(2))
    print(taiwan_phone.special_freature(1))
    print(taiwan_phone.special_freature(7))
    print(taiwan_phone.special_freature(8))
    print(taiwan_phone.special_freature(9))
    print(taiwan_phone.special_freature(10))
    print(taiwan_phone.special_freature(14))
            
            
