import os
import csv
import random
import string

class CsvHanlder():
    def __init__(self):
        if not os.path.isdir('./ilovecoffee'):
            folder = 'ilovecoffee'
            parent_dir = './'
            path = os.path.join(parent_dir, folder)
            os.mkdir(path)
    
    def create_csv(self):
        '''
        隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv
        '''
        # if not os.path.exists('./ilovecoffee/customers.csv')

        with open('./ilovecoffee/customers.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            name_list = ['tom','peter','hank','john','jack','jason','tommy','amy','dora','rosa']
            n = 500
            writer.writerow(['customer_id', 'customer_name', 'customer_mobile', 'frequency'])
            for i in range(n):
                customer_id = random.choice(string.ascii_letters) + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(7))
                customer_name = random.choice(name_list) + '.' + customer_id
                customer_mobile = "+" + "8869" + "".join(random.choice(string.digits) for x in range(8))
                frequency = random.randrange(21)

                writer.writerow([customer_id, customer_name, customer_mobile, frequency])


if __name__ == '__main__':
    CsvHanlder = CsvHanlder()
    CsvHanlder.create_csv()





