from async_promises import Promise

class Pipeline:
	def __init__(self, data):
		self._files = data['files']
		self._runners = data['runners']
		self._steps = data['steps']

		self.formatFiles()
		self.formatRunners()
		self.initSteps()
 

	def formatFiles(self):
		pass

	def formatRunners(self):
		pass

	def initSteps(self):
		pass

	def run(self):
		for parallel_steps in self._steps:
			Promise.all(parallel_steps)
