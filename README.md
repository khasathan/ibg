IBG email resolver
----
This is quick and dirty Python script to resolve email
from the question in [this link](https://www.blognone.com/node/64683)

```
{[([dota + is + ijlegcod]/[a*(game^of^love) + b])*zanroo ] + tmfafj = } @ibgcompany.com
วิธีการสมการ จากโจทย์ คือการคำนวณค่าโดย มี a-z เป็นตัวแปร โดย เริ่มที่ a=0 ... z= 25
เมื่อถอดสมการข้างตันแล้วจะได้ ชื่อ e-mail ที่ใช้ในการสมัครงาน
ตัวอย่างเช่น
a+ a = a
z + b = ba
lina + luna = xdaa
is + and = vv
```

Just for fun! :)

## Developed environments
- Ubuntu 15.04
- Python 3.4.3
- Pylint 1.4.3

## Testing
```
$cd /PATH/TO/ibg
$python3 -m unittest tests
```
You may install `nose` for Python 3 to help you to test the software.

```
$sudo apt-get install python3-nose
$cd /PATH/TO/ibg/
$nosetest3
```
If error not happen, It should be show the message like below
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
## Runing
```
$cd /PATH/TO/ibg/
$python3 emailsolver.py
```
for easier way
```
$chmod +x emailsolver.py
$./emailsolver.py
```
