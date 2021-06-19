# moleworld
摩尔庄园捐献统计小工具
# usage
## 必要文件
```
members.json： 存储镇民信息  
contribute.txt： 存储当天未贡献者信息  
contribution.py： 程序  
```
## option
```
-i： 当天第一次执行
-c： 继续统计
```
## 可实现功能
```
exit: 退出程序
append: 添加镇民
remove: 删除镇民
contribute: 统计捐献
```
## append
输入镇民名字缩写+名字全称  
输入f退出append
```
mole+摩尔庄园
```
## remove
输入镇民名字缩写
## contribute
输入贡献者名字缩写  
输入f退出contribute
# output
程序输出未捐献者名字全程以及未捐献者数量  
镇民信息会更新在members.json  
当天未捐献者信息会更新在contribute.txt  
想继续统计请执行
```
python contribution.py -c
```

