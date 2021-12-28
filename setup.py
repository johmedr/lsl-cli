from setuptools import setup

setup(
	name="lsl-cli", 
	version='0.1.0', 
	description="Command-line tools for the Lab Streaming Layer.",
	url="https://github.com/yop0/lsl-cli", 
	author="Johan Medrano",
	author_email="johan.medrano653@gmail.com",
	license="MIT",
	entry_points = {
		'console_scripts': [
			'lsl=lsl_cli.lsl:main'
		]
	}, 
	packages=['lsl_cli'],
	install_requires = [
		'pylsl'
	],
	package_data = {
		'lsl_cli': ['extra/lsl-completion.*', 'extra/lsl_complete_script.sh']
	}, 
	classifiers = [
        'Development Status :: 1 - Planning',
	]
) 
