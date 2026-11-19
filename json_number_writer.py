import json
from pathlib import Path
import json_number_writer

numbers = [1,2,3,4,7,4,5]

path = Path('num.json')
contents = json.dumps(numbers)
path.write_text(contents)