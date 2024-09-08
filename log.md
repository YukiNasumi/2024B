# 第二问：
## 未加入市场调节模型
```output
    plan: {'test1': 0, 'test2': 0, 'test_product': 0, 'disassemble': 0}
    profit:1134680 failed product in market:26860
    plan: {'test1': 0, 'test2': 0, 'test_product': 0, 'disassemble': 1}
    profit:1706778 failed product in market:29194
    plan: {'test1': 0, 'test2': 0, 'test_product': 1, 'disassemble': 0}
    profit:970976 failed product in market:0
    plan: {'test1': 0, 'test2': 0, 'test_product': 1, 'disassemble': 1}
    profit:1523466 failed product in market:0
    plan: {'test1': 0, 'test2': 1, 'test_product': 0, 'disassemble': 0}
    profit:947748 failed product in market:16971
    plan: {'test1': 0, 'test2': 1, 'test_product': 0, 'disassemble': 1}
    profit:1577198 failed product in market:19965
    plan: {'test1': 0, 'test2': 1, 'test_product': 1, 'disassemble': 0}
    profit:776045 failed product in market:0
    plan: {'test1': 0, 'test2': 1, 'test_product': 1, 'disassemble': 1}
    profit:1368744 failed product in market:0
    plan: {'test1': 1, 'test2': 0, 'test_product': 0, 'disassemble': 0}
    profit:1037692 failed product in market:17034
    plan: {'test1': 1, 'test2': 0, 'test_product': 0, 'disassemble': 1}
    profit:1691687 failed product in market:20008
    plan: {'test1': 1, 'test2': 0, 'test_product': 1, 'disassemble': 0}
    profit:875670 failed product in market:0
    plan: {'test1': 1, 'test2': 0, 'test_product': 1, 'disassemble': 1}
    profit:1473876 failed product in market:0
    plan: {'test1': 1, 'test2': 1, 'test_product': 0, 'disassemble': 0}
    profit:1226488 failed product in market:9051
    plan: {'test1': 1, 'test2': 1, 'test_product': 0, 'disassemble': 1}
    profit:1581896 failed product in market:9807
    plan: {'test1': 1, 'test2': 1, 'test_product': 1, 'disassemble': 0}
    profit:1019471 failed product in market:0
    plan: {'test1': 1, 'test2': 1, 'test_product': 1, 'disassemble': 1}
    profit:1338444 failed product in market:0
```
## 加入市场调节模型
### 采用温和市场 1/（1+exp(-20(x-0.5))
```output
plan:1 {'test1': 0, 'test2': 0, 'test_product': 0, 'disassemble': 0}
profit:1095638 failed product in market:26591 satisfacation rate:0.731417605171456
plan:2 {'test1': 0, 'test2': 0, 'test_product': 0, 'disassemble': 1}
profit:1150066 failed product in market:25764 satisfacation rate:0.7538667303558634
plan:3 {'test1': 0, 'test2': 0, 'test_product': 1, 'disassemble': 0}
profit:983800 failed product in market:0 satisfacation rate:1.0
plan:4 {'test1': 0, 'test2': 0, 'test_product': 1, 'disassemble': 1}
profit:1522861 failed product in market:0 satisfacation rate:1.0
plan:5 {'test1': 0, 'test2': 1, 'test_product': 0, 'disassemble': 0}
profit:924258 failed product in market:17084 satisfacation rate:0.8095259331935959
plan:6 {'test1': 0, 'test2': 1, 'test_product': 0, 'disassemble': 1}
profit:1566342 failed product in market:20019 satisfacation rate:0.8176377350240489
plan:7 {'test1': 0, 'test2': 1, 'test_product': 1, 'disassemble': 0}
profit:786120 failed product in market:0 satisfacation rate:1.0
plan:8 {'test1': 0, 'test2': 1, 'test_product': 1, 'disassemble': 1}
profit:1367537 failed product in market:0 satisfacation rate:1.0
plan:9 {'test1': 1, 'test2': 0, 'test_product': 0, 'disassemble': 0}
profit:-41758 failed product in market:12481 satisfacation rate:0.8096276749897042
plan:10 {'test1': 1, 'test2': 0, 'test_product': 0, 'disassemble': 1}
profit:-1705039 failed product in market:5528 satisfacation rate:0.8133504406253165
plan:11 {'test1': 1, 'test2': 0, 'test_product': 1, 'disassemble': 0}
profit:862849 failed product in market:0 satisfacation rate:1.0
plan:12 {'test1': 1, 'test2': 0, 'test_product': 1, 'disassemble': 1}
profit:1478358 failed product in market:0 satisfacation rate:1.0
plan:13 {'test1': 1, 'test2': 1, 'test_product': 0, 'disassemble': 0}
profit:1239716 failed product in market:8945 satisfacation rate:0.9004883801132508
plan:14 {'test1': 1, 'test2': 1, 'test_product': 0, 'disassemble': 1}
profit:-359112 failed product in market:5990 satisfacation rate:0.8997908824759515
plan:15 {'test1': 1, 'test2': 1, 'test_product': 1, 'disassemble': 0}
profit:1021404 failed product in market:0 satisfacation rate:1.0
plan:16 {'test1': 1, 'test2': 1, 'test_product': 1, 'disassemble': 1}
profit:1337918 failed product in market:0 satisfacation rate:1.0
```
### 采用严格市场 1/(1+exp(-5(x-0.5)))
```output
plan:1 {'test1': 0, 'test2': 0, 'test_product': 0, 'disassemble': 0}
profit:189928 failed product in market:20500 satisfacation rate:0.7305751235411628
plan:2 {'test1': 0, 'test2': 0, 'test_product': 0, 'disassemble': 1}
profit:460818 failed product in market:21810 satisfacation rate:0.7496096620132255
plan:3 {'test1': 0, 'test2': 0, 'test_product': 1, 'disassemble': 0}
profit:671880 failed product in market:0 satisfacation rate:1.0
plan:4 {'test1': 0, 'test2': 0, 'test_product': 1, 'disassemble': 1}
profit:1147639 failed product in market:0 satisfacation rate:1.0
plan:5 {'test1': 0, 'test2': 1, 'test_product': 0, 'disassemble': 0}
profit:258708 failed product in market:14038 satisfacation rate:0.8114616490054662
plan:6 {'test1': 0, 'test2': 1, 'test_product': 0, 'disassemble': 1}
profit:623614 failed product in market:16225 satisfacation rate:0.8150343711168618
plan:7 {'test1': 0, 'test2': 1, 'test_product': 1, 'disassemble': 0}
profit:460891 failed product in market:0 satisfacation rate:1.0
plan:8 {'test1': 0, 'test2': 1, 'test_product': 1, 'disassemble': 1}
profit:983614 failed product in market:0 satisfacation rate:1.0
plan:9 {'test1': 1, 'test2': 0, 'test_product': 0, 'disassemble': 0}
profit:323754 failed product in market:14211 satisfacation rate:0.807977623738295
plan:10 {'test1': 1, 'test2': 0, 'test_product': 0, 'disassemble': 1}
profit:751527 failed product in market:15888 satisfacation rate:0.8186549787700315
plan:11 {'test1': 1, 'test2': 0, 'test_product': 1, 'disassemble': 0}
profit:568312 failed product in market:0 satisfacation rate:1.0
plan:12 {'test1': 1, 'test2': 0, 'test_product': 1, 'disassemble': 1}
profit:1100786 failed product in market:0 satisfacation rate:1.0
plan:13 {'test1': 1, 'test2': 1, 'test_product': 0, 'disassemble': 0}
profit:708092 failed product in market:7826 satisfacation rate:0.9011531709042224
plan:14 {'test1': 1, 'test2': 1, 'test_product': 0, 'disassemble': 1}
profit:944068 failed product in market:8659 satisfacation rate:0.9002120450826284
plan:15 {'test1': 1, 'test2': 1, 'test_product': 1, 'disassemble': 0}
profit:680652 failed product in market:0 satisfacation rate:1.0
plan:16 {'test1': 1, 'test2': 1, 'test_product': 1, 'disassemble': 1}
profit:961070 failed product in market:0 satisfacation rate:1.0
```
# 第三问：进化算法
## 参数
种群数量：50    num_part:100000     迭代次数：20    交叉概率：0.6      变异概率：0.01
### 随机选取策略的结果：
```
第1代，最好的基因型[1 1 1 1 0 0 0 1 1 0 1 0 0 0 1 1]，收益为172208
第2代，最好的基因型[1 1 1 1 0 0 0 1 1 0 1 0 0 0 1 1]，收益为259920
第3代，最好的基因型[1 0 1 1 0 0 1 0 0 1 1 1 0 1 1 1]，收益为267150
第4代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为274736
第5代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为276530
第6代，最好的基因型[0 1 1 1 0 1 1 0 0 1 1 0 0 0 1 1]，收益为273804
第7代，最好的基因型[0 1 1 1 1 1 1 0 0 1 1 0 0 0 1 1]，收益为292070
第8代，最好的基因型[0 1 1 1 1 0 1 0 0 1 1 0 0 0 1 1]，收益为302830
第9代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为291176
第10代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为286354
第11代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为296192
第12代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为281822
第13代，最好的基因型[1 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为284072
第14代，最好的基因型[1 1 1 1 1 0 1 0 0 1 1 0 0 0 1 1]，收益为295642
第15代，最好的基因型[0 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为298750
第16代，最好的基因型[1 1 1 1 1 0 1 0 0 1 1 0 0 0 1 1]，收益为298648
第17代，最好的基因型[0 1 1 1 1 0 1 0 0 1 1 0 0 0 1 1]，收益为293684
第18代，最好的基因型[1 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1]，收益为296136
第19代，最好的基因型[0 1 1 1 1 0 1 0 0 1 1 0 0 0 1 1]，收益为281690
第20代，最好的基因型[0 1 1 1 1 0 1 0 0 1 1 0 0 0 1 1]，收益为290320
```
### 相同参数，策略经过初筛
```
第1代，最好的基因型[1 1 1 1 1 0 1 0 1 1 0 0 1 1 1 1]，收益为407726
第2代，最好的基因型[1 1 1 1 0 1 1 0 1 1 1 0 0 0 0 1]，收益为414210
第3代，最好的基因型[1 1 1 1 0 1 1 0 1 1 1 0 0 1 0 1]，收益为420354
第4代，最好的基因型[1 1 1 1 1 1 1 1 0 1 0 0 1 1 0 1]，收益为413322
第5代，最好的基因型[1 1 1 1 1 1 1 1 0 1 0 0 0 0 0 1]，收益为423936
['65315', '65339', '65459', '65331', '65435', '65283', '65343', '65377', '65489', '65491', '65457', '65345', '63283', '57057', '57039', '65361', '65529', '65533', '65411'] [4, 3, 4, 3, 3, 5, 4, 2, 7, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1]
第6代，最好的基因型[1 1 1 1 1 1 1 1 1 0 1 1 0 0 1 1]，收益为419550
第7代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为421560
第8代，最好的基因型[1 1 1 1 1 1 1 1 0 1 0 0 0 0 0 1]，收益为414396
第9代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为418554
第10代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为419118
['65281', '65459', '65315', '65331', '65283', '65475', '65345', '65489', '65505'] [1, 6, 6, 6, 18, 3, 5, 3, 2]
第11代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为417012
第12代，最好的基因型[1 1 1 1 1 1 1 1 0 0 1 0 0 0 1 1]，收益为420342
第13代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为427860
第14代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 1]，收益为417768
第15代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 1]，收益为422238
['65331', '65283', '65299', '65411', '65315', '65281'] [22, 18, 3, 1, 4, 2]
第16代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为418428
第17代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为419172
第18代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为421872
第19代，最好的基因型[1 1 1 1 1 1 1 1 0 0 1 1 0 0 1 1]，收益为417216
第20代，最好的基因型[1 1 1 1 1 1 1 1 0 0 0 0 0 0 1 1]，收益为420984
['65331', '65283', '65299'] [29, 18, 3]

```