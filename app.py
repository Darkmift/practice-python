from exercises.vars import print_calc_result
from utils.prettyPrint import prettyPrint
from exercises.print1 import prompForNameAndColor, promptForAge

result1 = print_calc_result([1, 2, 3], '+')
prettyPrint(result1,True)  # 6
result2 = print_calc_result([1, 2, 3], '-')
prettyPrint(result2)  # -4

result3 = prompForNameAndColor()
prettyPrint(result3)  # {"name": "John", "color": "blue"}
prettyPrint(f"{result3.name} likes {result3.color}")  # {"name": "John", "color": "blue"}

result4 = promptForAge()
prettyPrint(result4,True)  # {"age": 30}