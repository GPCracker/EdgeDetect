class TagsGroup(XModLib.VehicleManager.TagsGroup):
	pass

class EdgeEntity(XModLib.VehicleManager.Entity):
	def __init__(self, vehicle, colorIndex=0, drawMode=0):
		self._vehicle = vehicle
		self._colorIndex = colorIndex
		self._drawMode = drawMode
		self._addContour()
		return

	def _addContour(self):
		BigWorld.wgAddEdgeDetectEntity(self._vehicle, self._colorIndex, self._drawMode, False)
		return

	def _delContour(self):
		BigWorld.wgDelEdgeDetectEntity(self._vehicle)
		return

	@property
	def vehicle(self):
		return self._vehicle

	@property
	def colorIndex(self):
		return self._colorIndex

	@property
	def drawMode(self):
		return self._drawMode

	def __hash__(self):
		return hash((self._vehicle, self._colorIndex, self._drawMode))

	def __repr__(self):
		return 'EdgeEntity(vehicle={!r}, colorIndex={!r}, drawMode={!r})'.format(self._vehicle, self._colorIndex, self._drawMode)

	def __del__(self):
		self._delContour()
		return

class EdgeSettings(XModLib.VehicleManager.FilterSettings):
	def __init__(self, colorIndex=0, drawMode=0, eclass=EdgeEntity):
		self._colorIndex = colorIndex
		self._drawMode = drawMode
		self._eclass = eclass
		return

	@property
	def colorIndex(self):
		return self._colorIndex

	@property
	def drawMode(self):
		return self._drawMode

	def __hash__(self):
		return hash((self._colorIndex, self._drawMode))

	def __repr__(self):
		return 'EdgeSettings(colorIndex={!r}, drawMode={!r}, eclass={!r})'.format(self._colorIndex, self._drawMode, self._eclass)

	def __call__(self, vehicle):
		return self._eclass(vehicle, self._colorIndex, self._drawMode)

class VehicleFilter(XModLib.VehicleManager.VehicleFilter):
	pass

class VehicleManager(XModLib.VehicleManager.VehicleManager):
	pass
