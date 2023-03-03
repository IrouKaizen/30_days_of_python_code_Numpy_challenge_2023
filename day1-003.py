#Using NumPy, create a 10x10 array filled with number 8 (set the data type to float32) and assign it to a variable named arr.

import numpy as np

arr = np.full((10, 10), 8, dtype=np.float32)
print(arr)

#Solution II:

import numpy as np

arr = np.full(shape=(10, 10), fill_value=8, dtype='float32')
print(arr)

#output

#[[8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]]
