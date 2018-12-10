import os
import argparse
import shlex

from variables import steps,files,runners

class Variables:
	_runners = runners
	_files = files

	@classmethod
	def get_runner(cls,cmd_str):
		return cls._runners.get(cmd_str) or cmd_str

	@classmethod
	def format_files(cls,args_str):
		try:
			return args_str.format_map(cls._files)
		except KeyError as e:
			e.args = ("Referência de arquivo não encontrado: %s"%str(e),)
			raise e

class PipelineStep(dict):

	def __missing__(self,key):
		return ''

	def __init__(self,step):
		self.runner = Variables.get_runner(step['runner'])
		self.args = Variables.format_files(step['args'])
		step['args'] = self.args
		self.update(step)

	def __str__(self):
		return "{name}({index}): {runner} {args}".format_map(self)

	__repr__ = __str__

	def run(self):
		print('Running',self)
		if type(self.runner)==str:
			self._runos()
		else:

			self.args = shlex.split(self.args)

			parser = argparse.ArgumentParser()
			[parser.add_argument(arg) for arg in self.args if arg.startswith('-')]
			args = parser.parse_args(self.args)
			self.runner(**vars(args))
	def _runos(self):
		command = "{runner} {args}".format_map(self)
		os.system(command)

pipeline = [PipelineStep(step) for step in steps]