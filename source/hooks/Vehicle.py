# *************************
# Vehicle Hooks
# *************************
@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Vehicle.Vehicle, 'startVisual', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_BEFORE_HOOK)
def new_Vehicle_startVisual(self, *args, **kwargs):
	if hasattr(BigWorld.player(), 'XEdgeManager') and BigWorld.player().XEdgeManager is not None:
		if self.isStarted:
			self.removeEdge()
			BigWorld.player().XEdgeManager.updateHandle(self)
	return

@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Vehicle.Vehicle, 'stopVisual', calltype=XModLib.HookUtils.HookFunction.CALL_HOOK_BEFORE_ORIGIN)
def new_Vehicle_stopVisual(self, *args, **kwargs):
	if hasattr(BigWorld.player(), 'XEdgeManager') and BigWorld.player().XEdgeManager is not None:
		if self.isStarted:
			BigWorld.player().XEdgeManager.removeHandle(self)
	return

@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, Vehicle.Vehicle, '_Vehicle__onVehicleDeath', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_BEFORE_HOOK)
def new_Vehicle_onVehicleDeath(self, isDeadStarted=False):
	if hasattr(BigWorld.player(), 'XEdgeManager') and BigWorld.player().XEdgeManager is not None:
		if self.isStarted and not isDeadStarted:
			BigWorld.player().XEdgeManager.updateHandle(self)
	return
