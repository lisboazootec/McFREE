import json

def print_file(file):
  return f'- `{file[0]}`:\n\t- **Path**: `{file[1]}`\n'

def print_step(step):
  step_item = "\n".join(map(lambda key: f'  - **{key.capitalize()}**: *{step[key]}*',["key","name","description"]))
  return f'{step_item}\n'

def print_enitiy(entities,printter):
  return '\n'.join(map(printter,entities))


config = json.load(open('config.json'))

markdown = f'''
# Data
## Files
## Input
{print_enitiy(config['data']['files']['input'].items(),print_file)}

#Steps
{print_enitiy(config['steps'].values(),print_step)}
'''

open('PIPELINE-DESCRIPTION.2.md','w').write(markdown)