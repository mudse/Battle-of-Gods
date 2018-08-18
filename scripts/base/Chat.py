# -*- coding: utf-8 -*-
import KBEngine
import Equipment_Mould
import json
from KBEDebug import *
import Functor
import random


class Chat(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		self.PlayerEntitys = []
		self.Message="123"
		#储存聊天大厅
		KBEngine.globalData["Chat"] = self

	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)

	def EnterChat(self,entityCall):
		self.PlayerEntitys.append(entityCall)
		for i in range(len(self.PlayerEntitys)):
			self.PlayerEntitys[i].getPlayerList(self.PlayerEntitys)
		self.Message=("%s加入聊天室" % (entityCall.playerName))
		#-1表示系统信息
		self.tallAveryOne(self.Message,-1)

	def tallAveryOne(self,messsage,entityID,messsagecomfrom="测试"):
		for i in range(len(self.PlayerEntitys)):
			self.PlayerEntitys[i].ReceiveMessage(messsage,entityID,messsagecomfrom)

	def destoryPlayer(self,entityID):
		for i in range(len(self.PlayerEntitys)):
			if self.PlayerEntitys[i].id == entityID:
				self.Message=("%s离开聊天室" % (self.PlayerEntitys[i].playerName))
				self.PlayerEntitys.pop(i)
				break
		for i in range(len(self.PlayerEntitys)):
			self.PlayerEntitys[i].getPlayerList(self.PlayerEntitys)
		#-1表示系统信息
		self.tallAveryOne(self.Message,-1)

	def sendMessage(self,entityCall,messsage):
		self.tallAveryOne(messsage,entityCall.id,entityCall.playerName)
