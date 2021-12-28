from setuptools import setup

setup(
	name="lsl-cli", 
	version='0.0.2', 
	entry_points = {
		'console_scripts': [
			'lsl = lsl_cli.lsl:main'
		]
	}, 
	package_data = {
		'': ['extra/lsl-completion.*']
	}, 
	include_package_data = True
) 