# *************************
# AvatarInputHandler Hooks
# *************************
@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, AvatarInputHandler.AvatarInputHandler, 'handleKeyEvent', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_BEFORE_HOOK)
def new_AvatarInputHandler_handleKeyEvent(self, event):
	getShortcut = XModLib.KeyBoard.Shortcut.fromSequence
	## HotKeys - Common
	if self.ctrlModeName in ['arcade', 'sniper', 'strategic']:
		if hasattr(BigWorld.player(), 'XEdgeManager') and BigWorld.player().XEdgeManager is not None:
			BigWorld.player().XEdgeManager.handleShortcut(event)
	## HotKeys - Arcade
	if self.ctrlModeName == 'arcade':
		pass
	## HotKeys - Sniper
	elif self.ctrlModeName == 'sniper':
		pass
	## HotKeys - Strategic
	elif self.ctrlModeName == 'strategic':
		pass
	return
