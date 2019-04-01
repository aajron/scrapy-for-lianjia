# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt
import xlrd
from xlutils.copy import copy
from mySpider.style import Style
import pymysql

class LianjiaPipeline(object):

    style = xlwt.XFStyle()
    font = xlwt.Font()

    font.name = "SimSun"
    font.bold = True
    font.color_index = 4
    font.height = 12 * 20
    style.font = font

    def process_item(self, item, spider, style=style, a=[1]):
        xlsx = xlrd.open_workbook('test.xls')
        newwb = copy(xlsx)
        sheet1 = newwb.get_sheet(0)
        cur_rows = len(sheet1.get_rows())
        i_number = a[0]
        place = str(item['place'])
        size = str(item['size'])
        price = str(item['price'])
        if cur_rows > 0:

            sheet1.write(cur_rows, 0, place, style)
            sheet1.write(cur_rows, 1, size, style)
            sheet1.write(cur_rows, 2, price, style)
            newwb.save('test.xls')
        else:
            f = xlwt.Workbook(style_compression=2)
            sheet1 = f.add_sheet('租房', cell_overwrite_ok=True)
            row0 = ["地点", "大小", "价格"]
        # colum0 = ["张三", "李四", "恋习Python", "小明", "小红", "无名"]
        # 写第0行
            for i in range(0, len(row0)):
                sheet1.write(0, i, row0[i], style)
            # 写第一列
            # for i in range(0, len(colum0)):
            #     sheet1.write(i + 1, 0, colum0[i], set_style)

            sheet1.write(i_number, 0, place, style)
            sheet1.write(i_number, 1, size, style)
            sheet1.write(i_number, 2, price, style)

        # sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
        # sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
        # sheet1.write_merge(4, 5, 3, 3, '打篮球')
            [x+1 for x in a]
            f.save('test.xls')

            return item
        # try:
        #     place = str(item['place'])
        #     size = str(item['size'])
        #     price = str(item['price'])
        #     fb = open("lianjia.txt", "w+")
        #     fb.write(place + size + price + '\n')
        #     fb.close()
        # except:
        #     pass


class LianjiaPipelinedatabase(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='xx',
            db='school'
        )
        self.cur = self.conn.cursor()
        self.cur.execute("create table lianjia (place varchar(20), size varchar(20), prize varchar(20))")

    def process_item(self, item, spider):
        place = str(item['place'])
        size = str(item['size'])
        price = str(item['price'])
        self.cur.execute('insert into lianjia (place, size, prize) values (%s, %s, %s)', [place, size, price])
        self.conn.commit()
        # self.cur.close()
        # self.conn.close()
        return item
