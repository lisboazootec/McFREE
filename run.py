import argparse

from variables import steps,files,runners

parser = argparse.ArgumentParser()
args = parser.parse_args()

class Pipeline:

	def __init__(self,step,command_list):

		command_runner,command_args = command_list

		command_runner = Variables.get_runner(command_runner)
		command_args = Variables.format_files(command_args)

		self.name = step
		self.runner = command_runner
		self.arguments = command_args

	def run(self):
		if type(self.runner)==str:
			self._runos()
		else:
			# raise NotImplementedError()
			self.runner(*self.arguments)

	def _runos(self):
		command = "{} {}".format(self.runner,self.arguments)
		# os.system(command)
		print('Execution command "{}" on OS',command)

	def _args_str(self):
		return " ".join(self.arguments)

for step,command_list in steps.items().sort(lambda x:x[0]):
	Pipeline(step,command_list).run()