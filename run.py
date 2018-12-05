import argparse
from commands import process
from variables import *

parser = argparse.ArgumentParser()
args = parser.parse_args()

class Pipeline:

	def __init__(self,command):
		def evaluate(cmd):
			try:
				cmd = eval(cmd)
			except Exception as e:
				pass
			return cmd

		command = [evaluate(cmd) for cmd in command]
			
		self.runner = command[0]
		self.arguments = command[1:]

	def run(self):
		if type(self.runner)==str:
			self._runos()
		else:
			# raise NotImplementedError()
			self.runner(*self.arguments)

	def _runos(self):
		command = "{} {}".format(self.runner,self._args_str)
		# os.system(command)
		print('Execution command "{}" on OS',command)

	def _args_str(self):
		return " ".join(self.arguments)

for step in process:
	Pipeline(step).run()