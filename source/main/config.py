# *************************
# Configuration
# *************************
_config_ = None

# *************************
# Default configuration
# *************************
def defaultConfig():
	return {
		'applicationEnabled': ('Bool', True),
		'ignoreClientVersion': ('Bool', False),
		'hookInjectTimeout': ('Float', 3.0),
		'appLoadedMessage': ('WideString', u'&lt;a href=&quot;event:EdgeDetect.official_topic&quot;&gt;&lt;font color=&quot;#0080FF&quot;&gt;&quot;Edge&amp;nbsp;Detect&quot;&lt;/font&gt;&lt;/a&gt; &lt;font color=&quot;#008000&quot;&gt; successfully loaded.&lt;/font&gt;'),
		'appFailedMessage': ('WideString', u'&lt;a href=&quot;event:EdgeDetect.official_topic&quot;&gt;&lt;font color=&quot;#0080FF&quot;&gt;&quot;Edge&amp;nbsp;Detect&quot;&lt;/font&gt;&lt;/a&gt; &lt;font color=&quot;#E00000&quot;&gt; is incompatible with current client version.&lt;/font&gt;'),
		'colors': ('ColorsList', [
			Math.Vector4(127, 127, 127, 255),
			Math.Vector4(255, 18, 7, 255),
			Math.Vector4(124, 214, 6, 255),
			Math.Vector4(255, 255, 255, 255)
		]),
		'filters': ('FiltersList', [
			{
				'enabled': ('Bool', True),
				'activated': ('Bool', True),
				'key': ('String', 'KEY_NONE'),
				'switch': ('Bool', True),
				'invert': ('Bool', False),
				'groups': ('GroupsList', [
					{
						'include': ('TagsList', ['alive', 'player']),
						'exclude': ('TagsList', [])
					}
				]),
				'contours': ('ContoursList', [
					{
						'colorIndex': ('Int', 0),
						'drawMode': ('Int', 1)
					}
				])
			},
			{
				'enabled': ('Bool', True),
				'activated': ('Bool', True),
				'key': ('String', 'KEY_NONE'),
				'switch': ('Bool', True),
				'invert': ('Bool', False),
				'groups': ('GroupsList', [
					{
						'include': ('TagsList', ['alive', 'target']),
						'exclude': ('TagsList', ['ally'])
					}
				]),
				'contours': ('ContoursList', [
					{
						'colorIndex': ('Int', 1),
						'drawMode': ('Int', 0)
					}
				])
			},
			{
				'enabled': ('Bool', True),
				'activated': ('Bool', True),
				'key': ('String', 'KEY_NONE'),
				'switch': ('Bool', True),
				'invert': ('Bool', False),
				'groups': ('GroupsList', [
					{
						'include': ('TagsList', ['alive', 'ally', 'target']),
						'exclude': ('TagsList', [])
					}
				]),
				'contours': ('ContoursList', [
					{
						'colorIndex': ('Int', 2),
						'drawMode': ('Int', 0)
					}
				])
			}
		])
	}

# *************************
# Read configuration from file
# *************************
def readConfig():
	mainSection = ResMgr.openSection(os.path.splitext(__file__)[0] + '.xml')
	if mainSection is None:
		print '[{}] Config loading failed.'.format(__application__[1])
	else:
		print '[{}] Config successfully loaded.'.format(__application__[1])
	return XModLib.ConfigReader.ConfigReader({
		'ColorsList': XModLib.ConfigReader.ListXMLReader.customize(
			'ColorsListReader',
			ITEM_NAME = 'color',
			ITEM_TYPE = 'Vector4',
			ITEM_DEFAULT = Math.Vector4(255, 255, 255, 255)
		),
		'FiltersList': XModLib.ConfigReader.ListXMLReader.customize(
			'FiltersListReader',
			ITEM_NAME = 'filter',
			ITEM_TYPE = 'Dict',
			ITEM_DEFAULT = {
				'enabled': ('Bool', False),
				'activated': ('Bool', False),
				'key': ('String', 'KEY_NONE'),
				'switch': ('Bool', True),
				'invert': ('Bool', False),
				'groups': ('GroupsList', []),
				'contours': ('ContoursList', [])
			}
		),
		'GroupsList': XModLib.ConfigReader.ListXMLReader.customize(
			'GroupsListReader',
			ITEM_NAME = 'group',
			ITEM_TYPE = 'Dict',
			ITEM_DEFAULT = {
				'include': ('TagsList', []),
				'exclude': ('TagsList', [])
			}
		),
		'TagsList': XModLib.ConfigReader.ListXMLReader.customize(
			'TagsListReader',
			ITEM_NAME = 'tag',
			ITEM_TYPE = 'String',
			ITEM_DEFAULT = ''
		),
		'ContoursList': XModLib.ConfigReader.ListXMLReader.customize(
			'ContoursListReader',
			ITEM_NAME = 'contour',
			ITEM_TYPE = 'Dict',
			ITEM_DEFAULT = {
				'colorIndex': ('Int', 0),
				'drawMode': ('Int', 0)
			}
		)
	}).readSection(mainSection, defaultConfig())
