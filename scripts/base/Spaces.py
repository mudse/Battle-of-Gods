# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
import SCDefine
import d_spaces
from SpaceAlloc import *
class Spaces(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		# 初始化空间分配器
		self.initAlloc()
		
		# 向全局共享数据中注册这个管理器的entityCall以便在所有逻辑进程中可以方便的访问
		KBEngine.globalData["Spaces"] = self

	def initAlloc(self):
		# 注册一个定时器，在这个定时器中我们每个周期都创建出一些NPC，直到创建完所有
		self._spaceAllocs = {}
		self.addTimer(3, 1, SCDefine.TIMER_TYPE_CREATE_SPACES)
		
		self._tmpDatas = list(d_spaces.datas.keys())
		for utype in self._tmpDatas:
			spaceData = d_spaces.datas.get(utype)
			if spaceData["entityType"] == "SpaceDuplicate":
				self._spaceAllocs[utype] = SpaceAllocDuplicate(utype)
			else:
				self._spaceAllocs[utype] = SpaceAlloc(utype)

	def createSpaceOnTimer(self, tid):
		"""
		创建space
		"""
		if len(self._tmpDatas) > 0:
			spaceUType = self._tmpDatas.pop(0)
			self._spaceAllocs[spaceUType].init()
			
		if len(self._tmpDatas) <= 0:
			del self._tmpDatas
			self.delTimer(tid)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if SCDefine.TIMER_TYPE_CREATE_SPACES == userArg:
			self.createSpaceOnTimer(tid)

	def onSpaceLoseCell(self, spaceUType, spaceKey):
		"""
		defined method.
		space的cell创建好了
		"""
		self._spaceAllocs[spaceUType].onSpaceLoseCell(spaceKey)
		
	def onSpaceGetCell(self, spaceUType, spaceEntityCall, spaceKey):
		"""
		defined method.
		space的cell创建好了
		"""
		self._spaceAllocs[spaceUType].onSpaceGetCell(spaceEntityCall, spaceKey)