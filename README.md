# Game Of Life
Simple Conway's Game of Life, written in Python.

To run `cd` into `/src`, and do: 
```python
python cgl.py
```

You can also load [Life 1.05](http://www.conwaylife.com/wiki/Life_1.05) files:
```python
python cgl.py PATH_TO_FILE
```

Some basic patterns are provided in the `/maps` folder. So for example, to load a pulsar:
```python
python cgl.py ../maps/pulsar_105.lif
```

Output:

![alt text](https://raw.githubusercontent.com/umutseven92/GameOfLife/master/pulsar.gif "Pulsar")

You need to have pygame installed.

## Controls
* `R` key to reset
* `P` key to pause
* Right arrow to speed up
* Left arrow to slow down
* `Esc` to quit
