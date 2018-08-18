# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
import d_avatar_inittab
import GlobalDefine
import Equipment_Mould
import json
from interfaces.Equipment import Equipment
from interfaces.Attribute import Attribute



class Avatar(KBEngine.Proxy,
			Equipment,
			Attribute):

	def __init__(self):
		KBEngine.Proxy.__init__(self)
		Equipment.__init__(self)
		Attribute.__init__(self)
		DEBUG_MSG("Avatar have client")
		# 增加一个定时器，5秒后执行第1次，而后每1秒执行1次，用户参数是9
		self.addTimer( 1, 1, 9 )
		
		self.initLevelAttribute(self.level)
		self.initEquipmentAttribute()


	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)

		
	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("avatar[%i] entities enable. entityCall:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onTimer( self, id, userArg ):
		pass
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Avatar[%i].onClientDeath:" % self.id)
		self.writeToDB(self._write())
		self.clean()

	def setName(self,name):
		self.playerName=name
		DEBUG_MSG("Avatar:Name[%s]" % self.playerName)

	def getPlayerList(self,PLAYER_LIST):
		name_list=[]
		name_list.append("测试1")
		for i in range(len(PLAYER_LIST)):
			name_list.append(PLAYER_LIST[i].playerName)
			DEBUG_MSG("getPlayerList--Avatar[%i]:Name[%s]" % (i,PLAYER_LIST[i].playerName))
		self.client.getPlayerList_client(name_list)

	def EnterChat(self):
		KBEngine.globalData["Chat"].EnterChat(self)

	def clean(self):
		KBEngine.globalData["Chat"].destoryPlayer(self.id)

	def ReceiveMessage(self,message,entityid,messagecomfrom):
		DEBUG_MSG("entityid[%i]message:%s" % (entityid,message))
		type=0;
		if entityid==self.id:
			type=1
			#自己的话
		elif  entityid==-1:
			type=-1
			#登陆 退出
		else: 
			type=2
			#他人
		self.client.ReceiveMessage_client(message,type,messagecomfrom)

	def sendMessage(self,message):
		DEBUG_MSG("message[%s]" % (message))
		KBEngine.globalData["Chat"].sendMessage(self,message)


	def reqsendEquipment_ON(self):
		'''
		发送穿戴装备数据
		'''
		self.client.sendEquipment_ON(self.Equipment_ON)
	def reqsendEquipment_BAG(self):
		'''
		发送包裹装备数据
		'''
		self.client.sendEquipment_BAG(self.Equipment_BAG)





	def onhit(self,hit):
		self.hp=self.hp-hit
		self.test()

	def _write(self):
		DEBUG_MSG("HP %i"%(self.hp))


'''

	def getEquipment(self):
	
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
		

		props1 = {
			"id": Equipment_Mould.datas[100001]['id'],
			"name": Equipment_Mould.datas[100001]['name'],
			"level_need": Equipment_Mould.datas[100001]['level_need'],
			"type": Equipment_Mould.datas[100001]['type'],
			"damage1": Equipment_Mould.datas[100001]['damage1'],
			"damage2": Equipment_Mould.datas[100001]['damage2'],
			"attack_speed": Equipment_Mould.datas[100001]['attack_speed'],
			"weapon_range": Equipment_Mould.datas[100001]['weapon_range'],
			"defense": Equipment_Mould.datas[100001]['defense'],
			"hp": Equipment_Mould.datas[100001]['hp'],
			"mp": Equipment_Mould.datas[100001]['mp'],
			}

		INFO_MSG("props1:%s"%(props1.items()))
		
		self.Equipment_ON.append(props1)
		
		INFO_MSG("Equipment_Mould_List:%s"%(self.Equipment_ON))
'''
