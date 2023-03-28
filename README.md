# holmesxu
A library for pypi to help users to simplify some logic steps on programming.

## aorb
This helps you to short your if... else...

utility:
`aorb(value_1, value_2, inp_value, res_1, res_2)`
```Python
from holmesxu import aorb
import random

a = 1
b = 2
c = random.randrange(1, 4, 1)
print(aorb(a, b, c, a, b))```

c = 1
``` > 1```

c = 2
``` > 2 ```

c = 3
``` > Exception: Error! ```
