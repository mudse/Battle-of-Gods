# -*- coding: utf-8 -*-
import KBEngine
import Equipment_Mould
import json
from KBEDebug import *

class Exchange(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		self.shouldAutoArchive=True
		self.Equipment_Num=0;
		self.Loaddate()
		#储存大厅
		KBEngine.globalData["Equipment"] = self
		
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def Loaddate(self):
		for key,equipment in Equipment_Mould.datas.items():
			props1 = {
				"id": equipment['id'],
				"name": equipment['name'],
				"level_need": equipment['level_need'],
				"type": equipment['type'],
				"damage1": equipment['damage1'],
				"damage2": equipment['damage2'],
				"attack_speed": equipment['attack_speed'],
				"weapon_range": equipment['weapon_range'],
				"defense": equipment['defense'],
				"hp": equipment['hp'],
				"mp": equipment['mp'],
				}

			self.Equipment_Mould_List.append(props)
	def addEquipment(self,mould_id,ower_id):
		DEBUG_MSG("addEquipment mould_id:%i ower_id:%i")
		return self.id