# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *

class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		self.updataeAvatarListInfo()

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
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()		

	def reqAvatarList(self):
		self.client.onReqAvatarList(self.AvatarListInfo)

	def reqCreateAvatar(self,image_head,playerName):
		DEBUG_MSG("reqCreateAvatar")
		props={
			"image_head"		: image_head,
			"playerName"		: playerName,
			"level"				: 1,
		}
		avatar = KBEngine.createEntityLocally('Avatar', props)
		avatar.writeToDB(self._avatarwritetodb)

	def reqRemoveAvatar(self,dbid):
		DEBUG_MSG("dbid:%i"%(dbid))
		for key in range(len(self.AvatarList)):
			DEBUG_MSG("self.AvatarList[key]:%i"%(self.AvatarList[key]))
			if self.AvatarList[key]==dbid:
				avatar=KBEngine.createEntityFromDBID("Avatar", self.AvatarList[key],self.__onAvatarCreatedinRemove)
				self.AvatarList.pop(key)
				self.writeToDB(self._selfwritetodbinremove)
				return

	def updataeAvatarListInfo(self):
		self.AvatarListInfo=[]
		for key in range(len(self.AvatarList)):
			avatar=KBEngine.createEntityFromDBID("Avatar", self.AvatarList[key],self.__onAvatarCreated)

	def startgame(self,dbid):
		avatar=KBEngine.createEntityFromDBID("Avatar",dbid,self.__onAvatarCreatedinstartgame)

	def _avatarwritetodb(self, success, avatar):
		INFO_MSG('Account::_avatarwritetodb: %i, %i' % (success, avatar.databaseID))
		self.AvatarList.append(avatar.databaseID)
		self.writeToDB(self._selfwritetodbincreate)

	def _selfwritetodbincreate(self, success, avatar):
		DEBUG_MSG("_selfwritetodb %i"%(len(self.AvatarListInfo)))
		self.updataeAvatarListInfo()
		self.client.onCreateAvatar()

	def _selfwritetodbinremove(self, success, avatar):
		DEBUG_MSG("_selfwritetodb %i"%(len(self.AvatarListInfo)))
		self.updataeAvatarListInfo()
		self.client.onRemoveAvatar()

	def __onAvatarCreated(self, baseRef, dbid, wasActive):
		avatar = KBEngine.entities.get(baseRef.id)
		DEBUG_MSG("%i"%(avatar.databaseID))
		props={
			"DBID"				: avatar.databaseID,
			"Image_Head"		: avatar.image_head,
			"PlayerName"		: avatar.playerName,
			"Level"				: avatar.level,
		}
		self.AvatarListInfo.append(props)

	def __onAvatarCreatedinRemove(self, baseRef, dbid, wasActive):
		avatar = KBEngine.entities.get(baseRef.id)
		avatar.destroy(True)

	def __onAvatarCreatedinstartgame(self, baseRef, dbid, wasActive):
		avatar = KBEngine.entities.get(baseRef.id)
		self.giveClientTo(avatar)