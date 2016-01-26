# *************************
# EdgeDetectColorController Hooks
# *************************
@XModLib.HookUtils.HookFunction.methodHookOnEvent(_inject_hooks_, helpers.EdgeDetectColorController.EdgeDetectColorController, '_EdgeDetectColorController__changeColor', calltype=XModLib.HookUtils.HookFunction.CALL_ORIGIN_INSIDE_HOOK)
def new_EdgeDetectColorController_changeColor(old_EdgeDetectColorController_changeColor, self, *args, **kwargs):
	if not isinstance(BigWorld.player(), Avatar.PlayerAvatar):
		return old_EdgeDetectColorController_changeColor(self, *args, **kwargs)
	BigWorld.wgSetEdgeDetectColors(map(lambda color: color.scale(0.00390625), _config_['colors']))
	return
