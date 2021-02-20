#!/usr/bin/python3

import xmltodict
import json
import pymongo

def xml2Json(xml_PAHT):
	xml_file = open(xml_PAHT,'r',encoding='utf-8')
	xml_str = xml_file.read()
	json= xmltodict.parse(xml_str)
	return json
	

filelist = {'ke_bi_sample.xml':'Kobe',
			'kang_ri_shen_ju_sample.xml':'抗日神剧',
			'bu_dong_chan_deng_ji_tiao_li.xml':'不动产登记条例',
			'cha_wei_si.xml':'查韦斯',
			'chu_zi_xi_zi_pi_zi.xml':'厨子戏子痞子',
			'chui_zi_ROM.xml':'锤子ROM',
			'du_wan_ju.xml':'毒玩具',
			'man_lian_vs_huang_ma.xml':'曼联VS皇马',
			'mo_jing_xian_zong.xml':'魔境仙踪',
			'wang_yu_yan.xml':'王语嫣',
			'xiao_ao_jiang_hu.xml':'笑傲江湖',
			'zhong_guo_fang_yan_shi_ying_yu.xml':'中国方言式英语'}

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient("mongodb://corpus.bhu.edu.cn:9100/")
mydb = myclient["weibo"]
mycol = mydb["OpinionElementExtraction"]


for filename in filelist.keys():
	xml_PAHT=filename
	print(xml_PAHT)
	jsonobj=xml2Json(xml_PAHT)

	weibo = jsonobj["Result"]['weibo']
	for item in weibo:
		item['topic']=filelist[filename]
		data= json.dumps(item)
		data = data.replace("@","")
		data = data.replace("#","")
		jsd = json.loads(data)
		mycol.insert_one(jsd)
		# print(data)

