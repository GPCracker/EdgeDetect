# *************************
# PlayerAvatar Hooks
# *************************
@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, 'onBecomePlayer', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_BEFORE_HOOK)
def new_PlayerAvatar_onBecomePlayer(self, *args, **kwargs):
	if not hasattr(self, 'XEdgeManager') or self.XEdgeManager is None:
		getVehicleFilter = lambda vfilter: VehicleFilter(
			groups=[TagsGroup(include=group['include'], exclude=group['exclude']) for group in vfilter['groups']],
			settings=[EdgeSettings(colorIndex=contour['colorIndex'], drawMode=contour['drawMode']) for contour in vfilter['contours']],
			activated=vfilter['activated']
		)
		getShortcut = lambda vfilter: XModLib.KeyBoard.Shortcut.fromSequence(vfilter['key'], vfilter['switch'], vfilter['invert'])
		self.XEdgeManager = VehicleManager(vfilters=[(getVehicleFilter(vfilter), getShortcut(vfilter)) for vfilter in _config_['filters'] if vfilter['enabled']])
	return

@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, 'onBecomeNonPlayer', calltype=XModLib.HookUtils.HookFunction.CALL_HOOK_BEFORE_ORIGIN)
def new_PlayerAvatar_onBecomeNonPlayer(self):
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		self.XEdgeManager = None
	return

@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, 'targetBlur', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_PlayerAvatar_targetBlur(old_PlayerAvatar_targetBlur, self, prevEntity):
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(prevEntity) and prevEntity.isStarted:
			self.XEdgeManager.removeHandle(prevEntity)
	result = old_PlayerAvatar_targetBlur(self, prevEntity)
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(prevEntity) and prevEntity.isStarted:
			prevEntity.removeEdge()
			self.XEdgeManager.updateHandle(prevEntity)
	return result

@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, 'targetFocus', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_PlayerAvatar_targetFocus(old_PlayerAvatar_targetFocus, self, entity):
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(entity) and entity.isStarted:
			self.XEdgeManager.removeHandle(entity)
	result = old_PlayerAvatar_targetFocus(self, entity)
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(entity) and entity.isStarted:
			entity.removeEdge()
			self.XEdgeManager.updateHandle(entity)
	return result

@XModLib.HookUtils.HookFunction.propertyHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, '_PlayerAvatar__autoAimVehID', '_autoAimVehID', action=XModLib.HookUtils.HookFunction.PROPERTY_ACTION_GET, calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_PlayerAvatar_autoAimVehID_getter(old_PlayerAvatar_autoAimVehID_getter, self):
	try:
		result = old_PlayerAvatar_autoAimVehID_getter(self)
	except AttributeError:
		result = 0
	return result

@XModLib.HookUtils.HookFunction.propertyHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, '_PlayerAvatar__autoAimVehID', '_autoAimVehID', action=XModLib.HookUtils.HookFunction.PROPERTY_ACTION_SET, calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_PlayerAvatar_autoAimVehID_setter(old_PlayerAvatar_autoAimVehID_setter, self, value):
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		oldAutoAimVehicle = BigWorld.entity(self._PlayerAvatar__autoAimVehID)
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(oldAutoAimVehicle) and oldAutoAimVehicle.isStarted:
			self.XEdgeManager.updateHandle(oldAutoAimVehicle)
	result = old_PlayerAvatar_autoAimVehID_setter(self, value)
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		newAutoAimVehicle = BigWorld.entity(self._PlayerAvatar__autoAimVehID)
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(newAutoAimVehicle) and newAutoAimVehicle.isStarted:
			self.XEdgeManager.updateHandle(newAutoAimVehicle)
	return result

@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, '_PlayerAvatar__setVisibleGUI', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_PlayerAvatar_setVisibleGUI(old_PlayerAvatar_setVisibleGUI, self, flag):
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		playerVehicle = BigWorld.entity(self.playerVehicleID)
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(playerVehicle) and playerVehicle.isStarted:
			self.XEdgeManager.removeHandle(playerVehicle)
	result = old_PlayerAvatar_setVisibleGUI(self, flag)
	if hasattr(self, 'XEdgeManager') and self.XEdgeManager is not None:
		playerVehicle = BigWorld.entity(self.playerVehicleID)
		if XModLib.VehicleInfo.VehicleInfo.isVehicle(playerVehicle) and playerVehicle.isStarted:
			playerVehicle.removeEdge()
			self.XEdgeManager.updateHandle(playerVehicle)
		self.XEdgeManager.activated = flag
		self.XEdgeManager.updateHandles()
	return result

@XModLib.HookUtils.HookFunction.propertyHookOnEvent(_inject_hooks_, Avatar.PlayerAvatar, 'isGuiVisible', '_PlayerAvatar__isGuiVisible', action=XModLib.HookUtils.HookFunction.PROPERTY_ACTION_GET, calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_PlayerAvatar_isGuiVisible_getter(old_PlayerAvatar_isGuiVisible_getter, self):
	try:
		result = old_PlayerAvatar_isGuiVisible_getter(self)
	except AttributeError:
		result = True
	return result
