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
			return args_str.format(**cls._files)
		except KeyError as e:
			e.args = ("Referência de arquivo não encontrado: %s"%str(e),)
			raise e

class PipelineStep:

	def __init__(self,step,command_list):

		command_runner,command_args = command_list

		command_runner = Variables.get_runner(command_runner)
		command_args = Variables.format_files(command_args)

		self.name = step
		self.runner = command_runner
		self.arguments = command_args

	def __str__(self):
		return "{name}: {runner} {arguments}".format(**self.__dict__)

	__repr__ = __str__

	def run(self):
		if type(self.runner)==str:
			self._runos()
		else:

			self.arguments = shlex.split(self.arguments)

			parser = argparse.ArgumentParser()
			[parser.add_argument(arg) for arg in self.arguments if arg.startswith('-')]
			args = parser.parse_args(self.arguments)
			self.runner(**vars(args))
	def _runos(self):
		command = "{} {}".format(self.runner,self.arguments)
		print('Execution command on OS:',command)
		os.system(command)

pipeline = [PipelineStep(step,command_list) for step,command_list in sorted(list(steps.items()),key=lambda x:x[0])]