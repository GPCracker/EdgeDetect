__application__ = ['Edge Detect Mod', 'EdgeDetect']
__official_topic__ = 'http://www.koreanrandom.com/forum/topic/16984-/'
__authors__ = ['GPCracker']
__version__ = '<version>'
__xmodlib__ = [["0.0.2", None]]
__client__ = [['ru'], '0.9.13', None]

if __name__ == '__main__':
	appInfo = '{appname} ({appshort}) {version} ({client} {clusters}) by {authors}'.format(
		appname = __application__[0],
		appshort = __application__[1],
		version = __version__,
		client = __client__[1],
		clusters = ', '.join(__client__[0]).upper(),
		authors = ', '.join(__authors__)
	)
	print appInfo
	from time import sleep
	sleep(len(appInfo) * 0.06)
	exit()

import XModLib
if not XModLib.isCompatibleLibVersion(__xmodlib__):
	raise ImportError('XModLib version does not suit this version of application.')
