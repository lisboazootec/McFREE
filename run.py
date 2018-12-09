import argparse

from variables import steps,files,runners

parser = argparse.ArgumentParser()
args = parser.parse_args()

class Pipeline:

	def __init__(self,step,command_list):
		def evaluate(cmd):
			try:
				cmd = eval(cmd)
			except Exception as e:
				pass
			return cmd

		command = [evaluate(cmd) for cmd in command]
			
		self.name = step
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

for step,command_list in steps.items().sort(lambda x:x[0]):
	Pipeline(step,command_list).run()