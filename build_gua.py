 # -*- coding: utf-8 -*-
import pickle

info_dict_list = []
info_dict = {'name':'乾卦','num':1,'description':'乾为天','upper':'乾','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'坤卦','num':2,'description':'坤为地','upper':'坤','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'屯卦','num':3,'description':'水雷屯','upper':'坎','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'蒙卦','num':4,'description':'山水蒙','upper':'艮','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'需卦','num':5,'description':'水天需','upper':'坎','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'讼卦','num':6,'description':'天水讼','upper':'乾','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'讼卦','num':7,'description':'地水师','upper':'坤','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'讼卦','num':8,'description':'水地比','upper':'坎','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'小畜卦','num':9,'description':'風天小畜','upper':'巽','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'履卦','num':10,'description':'天澤履','upper':'乾','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'泰卦','num':11,'description':'地天泰','upper':'坤','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'否卦','num':12,'description':'天地否','upper':'乾','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'同人卦','num':13,'description':'天火同人','upper':'乾','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'大有卦','num':14,'description':'火天大有','upper':'离','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'谦卦','num':15,'description':'地山谦','upper':'坤','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'豫卦','num':16,'description':'雷地豫','upper':'震','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'随卦','num':17,'description':'澤雷随','upper':'兑','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'蛊卦','num':18,'description':'山風蛊','upper':'艮','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'临卦','num':19,'description':'地澤临','upper':'坤','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'观卦','num':20,'description':'風地观','upper':'巽','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'噬嗑卦','num':21,'description':'火雷噬嗑','upper':'离','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'贲卦','num':22,'description':'山火贲','upper':'艮','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'贲卦','num':23,'description':'山地剥','upper':'艮','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'复卦','num':24,'description':'地雷复','upper':'坤','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'无妄卦','num':25,'description':'天雷无妄','upper':'乾','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'无妄卦','num':26,'description':'山天大畜','upper':'艮','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'颐卦','num':27,'description':'山雷颐','upper':'艮','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'大过卦','num':28,'description':'澤風大过','upper':'兑','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'坎卦','num':29,'description':'坎为水','upper':'坎','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'离卦','num':30,'description':'离为火','upper':'离','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'咸卦','num':31,'description':'澤山咸','upper':'兑','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'恒卦','num':32,'description':'雷風恒','upper':'震','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'遯卦','num':33,'description':'天山遯','upper':'乾','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'大壯卦','num':34,'description':'雷天大壯','upper':'震','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'晉卦','num':35,'description':'火地晉','upper':'震','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'明夷卦','num':36,'description':'地火明夷','upper':'坤','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'家人卦','num':37,'description':'風火家人','upper':'巽','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'睽卦','num':38,'description':'火澤睽','upper':'离','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'蹇卦','num':39,'description':'水山蹇','upper':'坎','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'解卦','num':40,'description':'雷水解','upper':'震','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'損卦','num':41,'description':'山澤損','upper':'艮','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'益卦','num':42,'description':'風雷益','upper':'巽','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'夬卦','num':43,'description':'澤天夬','upper':'兑','lower':'乾'}
info_dict_list.append(info_dict)
info_dict = {'name':'姤卦','num':44,'description':'天風姤','upper':'乾','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'萃卦','num':45,'description':'澤地萃','upper':'兑','lower':'坤'}
info_dict_list.append(info_dict)
info_dict = {'name':'萃卦','num':46,'description':'地風升','upper':'坤','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'困卦','num':47,'description':'澤水困','upper':'兑','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'井卦','num':48,'description':'水風井','upper':'坎','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'革卦','num':49,'description':'澤火革','upper':'兑','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'鼎卦','num':50,'description':'火風鼎','upper':'离','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'震卦','num':51,'description':'震为雷','upper':'震','lower':'震'}
info_dict_list.append(info_dict)
info_dict = {'name':'艮卦','num':52,'description':'艮为山','upper':'艮','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'漸卦','num':53,'description':'風山漸','upper':'巽','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'歸妹卦','num':54,'description':'雷澤歸妹','upper':'震','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'豐卦','num':55,'description':'雷火豐','upper':'震','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'旅卦','num':56,'description':'火山旅','upper':'离','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'巽卦','num':57,'description':'巽为風','upper':'巽','lower':'巽'}
info_dict_list.append(info_dict)
info_dict = {'name':'兑卦','num':58,'description':'兑为澤','upper':'兑','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'渙卦','num':59,'description':'風水渙','upper':'巽','lower':'坎'}
info_dict_list.append(info_dict)
info_dict = {'name':'節卦','num':60,'description':'水澤節','upper':'坎','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'中孚卦','num':61,'description':'風澤中孚','upper':'巽','lower':'兑'}
info_dict_list.append(info_dict)
info_dict = {'name':'小過卦','num':62,'description':'雷山小過','upper':'震','lower':'艮'}
info_dict_list.append(info_dict)
info_dict = {'name':'既濟卦','num':63,'description':'水火既濟','upper':'坎','lower':'离'}
info_dict_list.append(info_dict)
info_dict = {'name':'未濟卦','num':64,'description':'火水未濟','upper':'离','lower':'坎'}
info_dict_list.append(info_dict)


with open('gua.pi', 'wb') as f:
    pickle.dump(info_dict_list, f)