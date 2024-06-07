import json
import os
import sys
from utils.genericObjFactory import createBlankObj
from utils.genericObjFactory import GenericObj

plainObj = createBlankObj()

class CustomEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, GenericObj):
      return obj.__dict__  # Convert the DataPrint object to a dictionary
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, obj)

def prettyPrint(data,clear=False):

  plainObj.data = data
  header_footer = "*" * 13
  printable = json.dumps(plainObj, indent=2, sort_keys=True, cls=CustomEncoder)
  if clear:
    os.system('clear')
  print(f"{header_footer}\n{printable}\n{header_footer}")