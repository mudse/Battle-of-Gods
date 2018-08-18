# -*- coding: utf-8 -*-
import KBEngine
import Equipment_Mould
import json
import GlobalDefine

from KBEDebug import *

class Equipment:
	def __init__(self):
		pass

	def initEquipmentAttribute(self):
		'''
		当你装备发生变动时 调用此函数 通常之前跟上initLevelAttribute函数
		'''
		for values in self.Equipment_ON:
			self.hp_max=values['hp']+self.hp_max
			self.mp_max=values['mp']+self.mp_max
			self.defense=values['defense']+self.defense
			self.damage1=values['damage1']+self.damage1
			self.damage2=values['damage2']+self.damage2
			self.attack_speed=values['attack_speed']*self.attack_speed
			DEBUG_MSG("attack_speed:%f"%(self.attack_speed))
			self.weapon_range=values['weapon_range']*self.weapon_range
			DEBUG_MSG("weapon_range:%f"%(self.weapon_range))

	def getEquipment(self,nn):
		'''
		获得装备函数：交易行购买获取 打怪掉落等
		'''
		if len(self.Equipment_BAG)<GlobalDefine.BAG_NUMBER:
			props = {
				"id": Equipment_Mould.datas[nn]['id'],
				"name": Equipment_Mould.datas[nn]['name'],
				"level_need": Equipment_Mould.datas[nn]['level_need'],
				"type": Equipment_Mould.datas[nn]['type'],
				"damage1": Equipment_Mould.datas[nn]['damage1'],
				"damage2": Equipment_Mould.datas[nn]['damage2'],
				"attack_speed": Equipment_Mould.datas[nn]['attack_speed'],
				"weapon_range": Equipment_Mould.datas[nn]['weapon_range'],
				"defense": Equipment_Mould.datas[nn]['defense'],
				"hp": Equipment_Mould.datas[nn]['hp'],
				"mp": Equipment_Mould.datas[nn]['mp'],
				}
			INFO_MSG("props1:%s"%(props.items()))
		
			self.Equipment_BAG.append(props)
		else:	
			pass

	def wearEquipment(self,number,arg_type):
		'''
		穿装备调用
		替换装备先脱再穿
		for i in self.Equipment_ON:
			if i['type']==arg_type:
				self.client.changeEquipment(0,{})
		for j in range(len(self.Equipment_BAG)):
			if self.Equipment_BAG[j]==number:
				self.Equipment_ON.append(self.Equipment_BAG.pop(j))
				self.client.changeEquipment(1,self.Equipment_ON[-1])
		'''
		for i in self.Equipment_ON:
			if i['type']==arg_type:
				self.client.changeEquipment(0)
		else:
			self.Equipment_ON.append(self.Equipment_BAG.pop(number))
			self.client.changeEquipment(1)
	def removeEquipment(self,arg_number):
		'''
		脱装备调用
		替换装备先脱再穿
		if len(self.Equipment_BAG)<GlobalDefine.BAG_NUMBER:
			for j in range(len(self.Equipment_ON)):
				if self.Equipment_ON[j]==arg_number:
					self.Equipment_BAG.append(self.Equipment_ON.pop(j))
					self.client.changeEquipment(1,self.Equipment_BAG[-1])
		'''
		if len(self.Equipment_BAG)<GlobalDefine.BAG_NUMBER:
			self.Equipment_BAG.append(self.Equipment_ON.pop(arg_number))
			self.client.changeEquipment(1)






	def destroyEquipment(self,arg_number):
		'''
		销毁装备
		'''
		self.Equipment_BAG.pop(arg_number)
		self.client.changeEquipment(1)