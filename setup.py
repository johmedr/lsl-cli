from setuptools import setup

setup(
	name="lslutils", 
	version='0.0.1', 
	entry_points = {
		'console_scripts': [
			'lsl = lslutils.lsl:main'
		]
	}
) 