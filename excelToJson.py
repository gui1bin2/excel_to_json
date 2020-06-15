# -*- coding: utf-8 -*-

import pandas as pd
import json
 
#导入原始文件
data1 = json.loads(pd.read_excel('d:/py/CardTable.xls',header=1,sheet_name='CardList').to_json(orient ='records', force_ascii=False))
data2 = json.loads(pd.read_excel('d:/py/HeroTable.xls',header=1,sheet_name='JiBan').to_json(orient ='records', force_ascii=False))

#第一种格式，直接运行test，复制粘贴
test = {"cardList":data1,"jiBan":data2}

#第二种格式，导出json文件
j = json.dumps(test,ensure_ascii=False)
fileObject = open('d:/py/jsonFile.json', 'w')
fileObject.write(j)
fileObject.close()