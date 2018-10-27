import requests
import json,time

import selenium
from lxml import etree
from selenium import webdriver

#创建一个selenium对象
# sel = selenium.webdriver.Chrome()
# sel.maximize_window()
#
# url='http://www.juanpi.com/search?keywords=%E5%81%A5%E8%BA%AB%E5%99%A8%E6%9D%90'
# sel.get(url)
# time.sleep(5)
# a= sel.find_elements_by_xpath("//a")
# time.sleep(3)
# for i in a:
#    print(i.get_attribute('href'))
list1=[]
tulist =[]
sta =int(input('起始'))
end =int(input('结束'))
for page in range(sta,end+1):

    url ='http://www.shuhua.com/list/0-page1'
    headers = {
        'Cookie': 'PHPSESSID=ofnlqohk5m9o1a2jhja7gvsi40; Hm_lvt_61e0cc39944f6de3239c5d5e7185f811=1540544561; Hm_lvt_0fa12009777c90a8bb1b5ec57a48c96a=1540544561; Hm_lvt_7c3d9fcbef58d1458feba4304f821c52=1540544561; LXB_REFER=www.baidu.com; Hm_lvt_1dbbc01afa7a27c9a8eeb15f5149a5c8=1540544561; __root_domain_v=.shuhua.com; _qddaz=QD.vmshca.7snq27.jnpsgg1f; _qdda=3-1.25kyx; _qddab=3-l0wcno.jnpsgged; _qddamta_2852158374=3-0; Hm_lpvt_0fa12009777c90a8bb1b5ec57a48c96a=1540544594; Hm_lpvt_1dbbc01afa7a27c9a8eeb15f5149a5c8=1540544594; Hm_lpvt_7c3d9fcbef58d1458feba4304f821c52=1540544594; Hm_lpvt_61e0cc39944f6de3239c5d5e7185f811=1540544594',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url1 =url.format(page)
    req = requests.get(url=url1,headers=headers)
    cont = req.content
    tree = etree.HTML(cont)
    quan = tree.xpath('//div[@class="goods-list clearfix"]')
    for qu in quan:
         lianjie = qu.xpath('.//div[@class="figure figure-img"]/a/@href')
         tupian = qu.xpath('//div[@class="figure figure-img"]/a/img/@src')
         item ={
             "图片地址":tupian,
         }
         tulist.append(item)
         for u in lianjie:
             req1 =requests.get(url=u,headers=headers)
             cont1 =req1.content
             tree1 =etree.HTML(cont1)
             xiang = tree1.xpath('//div[@class="goods-detail-info  clearfix J_goodsDetail"]')
             for xi in xiang:
                 mingcheng  = xi.xpath('.//dt[@class="goods-name"]/text()')
                 jianjie =xi.xpath('.//dd[@class="goods-subtitle"]//p/text()')
                 jiage = xi.xpath('.//b[@class="J_mi_goodsPrice"]/text()')
                 tupian=xi.xpath('.//ul[@id="goodsPicList"]//li/img/@src')
                 print(tupian)
                 itme ={
                     "商品名称":mingcheng,
                     "商品介绍":jianjie,
                     "商品价格":jiage,
                     "图片地址":tupian
                 }
                 list1.append(itme)
                 datas = json.dumps(list1)
                 with open('data4.json', 'w', encoding='utf8') as fp:
                     fp.write(datas)

