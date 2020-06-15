# -*- coding: utf-8 -*-

import pandas as pd
import json
 

data1 = json.loads(pd.read_excel('d:/py/CardTable.xls',header=1,sheet_name='CardList').to_json(orient ='records', force_ascii=False))
data2 = json.loads(pd.read_excel('d:/py/HeroTable.xls',header=1,sheet_name='JiBan').to_json(orient ='records', force_ascii=False))


test = {"cardList":data1,"jiBan":data2}

j = json.dumps(test,ensure_ascii=False)