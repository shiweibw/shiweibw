# -*- coding: utf-8 -*-
__author__ = 'sugyswang@126.com'

# http://www.cnblogs.com/tkinter/p/5632312.html
# http://www.runoob.com/python3/python3-mysql.html


import pymysql

class ConnectMysqlException(Exception):
    pass
class CreateTableException(Exception):
    pass
class QueryTableException(Exception):
    pass

class MySQLcommand():
    def __init__(self,user,password,**kw):
        self.port = kw.setdefault('port',3306)
        self.db = kw.setdefault('db',None)
        self.table = kw.setdefault('table',None)
        self.host = kw.setdefault('host',"127.0.0.1")
        self.user = user
        self.password = password
    
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,charset='utf8')
            # 设置charset 为utf8,支持中文
            self.cus = self.conn.cursor()
            # 创建Cursor对象,使用它执行SQL语句。			
        except Exception as reason:
            print("connect mysql error: %s " % reason)
            raise ConnectMysqlException 

        if self.db is not None:
            sql = "CREATE DATABASE IF NOT EXISTS " + self.db
            self.cus.execute(sql)
            self.cus.execute("use " + self.db)

    def createTable(self,column,table=None):
        #Usage: createTable(self,"id int unsigned,name char(20) not null"table=None):
        
        if table:
            self.table = table

        sql = "CREATE TABLE IF NOT EXISTS " + self.table + "(" + column +")ENGINE=INNODB CHARSET='utf8'"

        try:
            self.cus.execute(sql)
        except Exception as reason:
            raise CreateTableException("Fail to create Table ==> %s" % reason )    
			
    def queryTable(self,table=None):
        if table:
            self.table = table
        sql = "SELECT * FROM " + self.table
        try:
            self.cus.execute(sql)
            row = self.cus.fetchall()
            return row
        except Exception as reason:
            raise QueryTableException("Fail to query Table ==> %s" % reason)

    def insertTable(self,**args): 
        #Usage: insertMysql(table=tb_name,name1=value1,name2=value2,name3=value3...):
        if args.get('table'):
            self.table = args['table']
            args.pop('table')

        column_name = ''
        column_value = ''
        for column in args.items():
            column_name = column_name[:] + column[0] + ','
            column_value = column_value[:] + "\'" + column[1] + "\'" + ','
        column_name = column_name.strip(',')
        column_value = column_value.strip(',')

        sql = "INSERT INTO " + self.table + " (" +column_name + ") VALUES (" + column_value + ")"
        try:
            self.cus.execute(sql)
            self.conn.commit()
        except Exception as reason:
            print("insert failed: %s" % reason)
            self.conn.rollback()

    def executeSQL(sql,commit=True):
        try:
            self.cus.execute(sql)
            if commit:
                self.conn.commit()
        except Exception as reason:
            print("failed to execute the sql: %s \n Error: %s" % (sql,reason))
            self.conn.rollback()
            




		
    def closeMysql(self):
        self.cus.close()
        self.conn.close()
		
if __name__ == "__main__":
    data = ''' 
    {"resp": [{"city": "上海"}, {"updatetime": "14:20"}, {"wendu": "34"}, {"fengli": "3级"}, {"shidu": "62%"}, {"fengxiang": "东北风"}, {"sunrise_1": "05:23"}, {"sunset_1": "18:29"}, {"sunrise_2": ""}, {"sunset_2": ""}, {"environment": [{"aqi": "18"
}, {"pm25": "12"}, {"suggest": "各类人群可自由活动"}, {"quality": "优"}, {"MajorPollutants": ""}, {"o3": "53"}, {"co": "1"}, {"pm10": "17"}, {"so2": "5"}, {"no2
": "11"}, {"time": "14:00:00"}]}, {"yesterday": [{"date_1": "21日星期一"}, {"high_1": "高温 34℃"}, {"low_1": "低温 27℃"}, {"day_1": [{"type_1": "阴"}, {"fx_1"
: "东南风"}, {"fl_1": "<3级"}]}, {"night_1": [{"type_1": "阴"}, {"fx_1": "东南风"}, {"fl_1": "<3级"}]}]}, {"forecast": [{"weather": [{"date": "22日星期二"}, {"h
igh": "高温 34℃"}, {"low": "低温 28℃"}, {"day": [{"type": "小雨"}, {"fengxiang": "东南风"}, {"fengli": "3-4级"}]}, {"night": [{"type": "多云"}, {"fengxiang":
"东南风"}, {"fengli": "3-4级"}]}]}, {"weather": [{"date": "23日星期三"}, {"high": "高温 35℃"}, {"low": "低温 28℃"}, {"day": [{"type": "多云"}, {"fengxiang": "
东南风"}, {"fengli": "3-4级"}]}, {"night": [{"type": "多云"}, {"fengxiang": "东南风"}, {"fengli": "3-4级"}]}]}, {"weather": [{"date": "24日星期四"}, {"high": "
高温 36℃"}, {"low": "低温 28℃"}, {"day": [{"type": "多云"}, {"fengxiang": "东南风"}, {"fengli": "<3级"}]}, {"night": [{"type": "多云"}, {"fengxiang": "南风"},
 {"fengli": "<3级"}]}]}, {"weather": [{"date": "25日星期五"}, {"high": "高温 35℃"}, {"low": "低温 27℃"}, {"day": [{"type": "多云"}, {"fengxiang": "东南风"}, {
"fengli": "3-4级"}]}, {"night": [{"type": "多云"}, {"fengxiang": "南风"}, {"fengli": "<3级"}]}]}, {"weather": [{"date": "26日星期六"}, {"high": "高温 33℃"}, {"
low": "低温 26℃"}, {"day": [{"type": "小雨"}, {"fengxiang": "东风"}, {"fengli": "<3级"}]}, {"night": [{"type": "多云"}, {"fengxiang": "东南风"}, {"fengli": "<3
级"}]}]}]}, {"zhishus": [{"zhishu": [{"name": "晨练指数"}, {"value": "较不宜"}, {"detail": "有降水，风力稍大，较不宜晨练，室外锻炼请携带雨具。建议年老体弱人群适
当减少晨练时间。"}]}, {"zhishu": [{"name": "舒适度"}, {"value": "较不舒适"}, {"detail": "白天天气较热，虽然有雨，但仍然无法削弱较高气温给人们带来的暑意，这种天
气会让您感到不很舒适。"}]}, {"zhishu": [{"name": "穿衣指数"}, {"value": "炎热"}, {"detail": "天气炎热，建议着短衫、短裙、短裤、薄型T恤衫等清凉夏季服装。"}]}, {"
zhishu": [{"name": "感冒指数"}, {"value": "少发"}, {"detail": "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。"}]}, {"zhishu": [{"nam
e": "晾晒指数"}, {"value": "不宜"}, {"detail": "有降水，不适宜晾晒。若需要晾晒，请在室内准备出充足的空间。"}]}, {"zhishu": [{"name": "旅游指数"}, {"value": "较
适宜"}, {"detail": "有较弱降水作伴的一天，虽然风稍大，较热，但仍较适宜旅游，可不要错过机会呦！"}]}, {"zhishu": [{"name": "紫外线强度"}, {"value": "弱"}, {"detai
l": "紫外线强度较弱，建议出门前涂擦SPF在12-15之间、PA+的防晒护肤品。"}]}, {"zhishu": [{"name": "洗车指数"}, {"value": "不宜"}, {"detail": "不宜洗车，未来24小时
内有雨，如果在此期间洗车，雨水和路上的泥水可能会再次弄脏您的爱车。"}]}, {"zhishu": [{"name": "运动指数"}, {"value": "较不宜"}, {"detail": "有降水，且风力较强，
气压较低，推荐您在室内进行低强度运动；若坚持户外运动，须注意避雨防风。"}]}, {"zhishu": [{"name": "约会指数"}, {"value": "较不适宜"}, {"detail": "天气较热，室外
有风，而且有降水，会给室外约会带来不便，外出约会请一定做好准备。"}]}, {"zhishu": [{"name": "雨伞指数"}, {"value": "带伞"}, {"detail": "有降水，请带上雨伞，如果
你喜欢雨中漫步，享受大自然给予的温馨和快乐，在短时间外出可收起雨伞。"}]}]}]}
'''
    column = "Date DATE not null,City CHAR(20),Json_data blob not null comment 'json'"
    test = MySQLcommand('root','123456',db='my_DBa')
    test.connectMysql()
    test.createTable(column,'shanghai')
    test.insertTable(table='shanghai',Date='2017-08-22',City='shanghai',Json_data=data)


    


