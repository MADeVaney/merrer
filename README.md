# merrer
M(app)er (and) R(educ)er

[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

```
mapred streaming \
  -input ??? \
  -output ??? \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```

Tested on these three text files:
  https://www.gutenberg.org/cache/epub/1342/pg1342.txt
  https://www.gutenberg.org/cache/epub/84/pg84.txt
  https://www.gutenberg.org/cache/epub/768/pg768.txt
