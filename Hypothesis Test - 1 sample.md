```python
import pandas as pd
from scipy import stats
```


```python
data=pd.Series([0.593, 0.142, 0.329, 0.691, 0.231, 0.793, 0.519, 0.392, 0.418])
```


```python
p=stats.ttest_1samp(data,0.3)[1]
p_value=p/2
p_value
```




    0.029265164842448826



### Since p_value<0.05, reject Ho


```python

```
