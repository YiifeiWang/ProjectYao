 # -*- coding: utf-8 -*-
class GuaXiang:
    def __init__(self, info_dict):
        self.info_dict = info_dict
        assert(set(info_dict.keys()) == set(['upper','lower','name','num','description']))
        for key in self.info_dict.keys():
            setattr(self, key, self.info_dict[key])

    def print_info(self):
        print("{}: {} {}".format(self.num, self.name, self.description))

GuaDict = {"乾":1, "兑":2, "离":3, "震":4, "巽":5, "坎":6, "艮":7, "坤":8} # Fu Xi
GuaDict2 = {"乾":3, "兑":6, "离":2, "震":4, "巽":1, "坎":8, "艮":7, "坤":9} # 9 gong
GuaDict3 = {"乾":1, "兑":2, "离":8, "震":6, "巽":7, "坎":4, "艮":5, "坤":3} # rotate