from setuptools import setup

setup(
	name="lsl-cli", 
	version='0.0.1', 
	entry_points = {
		'console_scripts': [
			'lsl = lsl_cli.lsl:main'
		]
	}
) 