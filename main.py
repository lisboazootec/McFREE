import os
import argparse
import shlex
from string import Formatter
from async_promises import Promise

from variables import steps,files,runners

frmt = Formatter()

class Variables:
	_runners = runners
	_files = files

	@classmethod
	def get_runner(cls,cmd_str):
		return cls._runners.get(cmd_str) or cmd_str

	@classmethod
	def format_files(cls,args_str):
		def frmt_rec(arg):
			arg = arg.format_map(cls._files)
			formatable = [b for a,b,c,d in frmt.parse(arg) if b]
			return frmt_rec(arg) if formatable else arg
			
		try:
			return frmt_rec(args_str)
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

class Pipeline:
	def run(self):
		for parallel_steps in self.steps:
			Promisse.all(parallel_steps)
	