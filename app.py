#-----------------------
# 匯入Flask類別
#-----------------------
from flask import Flask, render_template

#-----------------------
# 產生一個Flask物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 用裝飾器定義app的路由
#-----------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer/test')
def customer_test():
    '''
    data = {}
    data['name'] = "DIO"
    data['gender'] = "男"
    '''
    data={'name':'DIO', 'gender':'男', 'age':500}
    return render_template('test.html', data=data)

@app.route('/customer/list')
def customer_list():
    
    data=[{'name':'王小明', 'gender':'男', 'age':50},
          {'name':'假面騎士帝騎', 'gender':'男', 'age':100},
          {'name':'假面騎士Decard', 'gender':'男', 'age':20},
          {'name':'Decade', 'gender':'男', 'age':35},
          {'name':'池塘的守護者', 'gender':'男', 'age':500}]
    return render_template('list.html', data=data)

#-----------------------
# 執行app
#-----------------------
if __name__ == '__main__':
    app.run(port=5000, debug=True)