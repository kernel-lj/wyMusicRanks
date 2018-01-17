1. cd /Users/你的名字 创建文件夹 mkdir -p PATH/TO
2. 将libs.zip解压放到/Users/你的名字/PATH/TO 目录下
3. cd /Users/你的名字 目录下vi .bash_profile 添加：alias phantomjs='~/PATH/TO/phantomjs'
4. 执行命令source .bash_profile

5.进入到此目录执行命令:scrapy crawl wymusic -o songs.csv
会在此目录看到songs.csv文件，
