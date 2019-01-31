
Part 1
1. 执行顺序
    sh getdata1.sh
    sh merge_test1.sh

2. 具体作用
    （1）getdata1.sh
        先执行两个python文件，对唐宋诗进行提取，去除一些乱码内容，宋诗只有63000，占总数的接近1/4.
        再进行去重和shuf，得到唐诗tangout：56000，宋诗song1out：62840.
        然后分为valid和train，valid均5600，剩下的唐tangout.train:50380, 宋song1out.train:57200.
    （2）merge_test1.sh
        先合并两个valid和两个train，并shuf
        再调用fasttext

3. 实验结果
    第一次用的宋诗是59000，准确率是79.5%-79.6%
    第二次用的宋诗为63000，准确率是79.7%-80.1%



Part2
1. 思路
    用所有4个part的宋诗做四次训练。
    唐诗不动。

2. 执行顺序
    sh getdata.sh 
    sh merge_test.sh

3. 具体作用
    （1）getdata
        poetry_song.py得到4个宋诗文件song1，song2, song3, songtxt, 前三个630000，最后65000
        去重，shuf，得到4个宋诗out: song2out:62810, song3out:62080, song4out:64750
        再分4个valid，train，valid均5600. song234: 57200, 56480, 58950
    （2）merge_test
        分别合并4个valid和trian，并shuf
        再调用4次fasttext

4. 实验结果
    p1: 79.2%
    p2: 80.0%
    p3: 79.0%
    p4: 79.2%












