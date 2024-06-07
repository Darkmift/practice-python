import json
import os
import sys
from utils.genericObjFactory import createBlankObj
from utils.genericObjFactory import GenericObj
from utils.typeDetector import isPrimitive

plainObj = createBlankObj()

class CustomEncoder(json.JSONEncoder):
  """
  Custom JSON encoder that converts objects to dictionaries.
  """
  def default(self, obj):
    if isinstance(obj, object):
      return obj.__dict__  # Convert the DataPrint object to a dictionary
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, obj)

def prettyPrint(data, clear=False):
    """
    Pretty prints the given data as stringified JSON if it is an object, 
    or as is if it is a primitive type.
    """
    if isPrimitive(data):
        printable = data
    else:
        plainObj.data = data
        printable = json.dumps(plainObj, indent=2, sort_keys=True, cls=CustomEncoder)
    
    header_footer = "*" * 13
    if clear:
        os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{header_footer}\n{printable}\n{header_footer}")