# -*- coding: utf-8 -*-
import KBEngine
import d_avatar_inittab
import json
from KBEDebug import *

class Attribute:
	def __init__(self):
		pass

	def initLevelAttribute(self,lv):
		'''
		lv指人物当前等级
		重置人物属性，调用时机：升级 换装 
		调用此函数后需再调用initEquipmentAttribute函数。
		'''
		self.hp_max=d_avatar_inittab.datas[lv]['hp_max']
		self.mp_max=d_avatar_inittab.datas[lv]['mp_max']
		self.defense=d_avatar_inittab.datas[lv]['defense']
		self.damage1=d_avatar_inittab.datas[lv]['damage1']
		self.damage2=d_avatar_inittab.datas[lv]['damage2']
		self.attack_speed=d_avatar_inittab.datas[lv]['attack_speed']
		DEBUG_MSG("attack_speed:%f"%(self.attack_speed))
		self.weapon_range=d_avatar_inittab.datas[lv]['weapon_range']
		DEBUG_MSG("weapon_range:%f"%(self.weapon_range))

