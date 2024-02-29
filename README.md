<div align="center">
    <h1>GameTimePause 加速器时长暂停脚本</h1>
    <img src="https://img.shields.io/github/license/JasonYANG170/GameTimePause?label=License&style=for-the-badge">
    <img src="https://img.shields.io/github/commit-activity/w/JasonYANG170/GameTimePause?style=for-the-badge">
	<img src="https://img.shields.io/github/languages/count/JasonYANG170/GameTimePause?logo=python&style=for-the-badge">
	<br>
    	<a href="https://discord.com/invite/az3ceRmgVe"><img alt="Discord" src="https://img.shields.io/discord/978108215499816980?style=social&logo=discord&label=echosec"></a>
  <br>

这是一项基于Python语言的Github Actions自动化定时脚本
  
<br>

</div>

## 支持平台
- [x] 雷神加速器
- [ ] NN加速器

如您使用其他以时间结算的加速器请向我提出issues
## 使用教程
1.请先Fork本项目。 

2.在仓库的Settings-Secrets-Actions中分别New repository secrets以下两个变量  
    - PHONE(填写您注册的手机号)  
    - PASSWORD(填写您的账户密码)  
    - TOKEN(可选 填写PUSHPLUS的Token)
3.点击仓库的Actions，再点击“I understand my workflows, go ahead and enable them”的绿色按钮启用actions  

4.在左侧边栏找到“pause”并点击，再点击右侧的“Enable workflow”启用此action  

5.默认每天凌晨3点(UTC+8)执行定时任务（由于github action的特性，可能会延迟20分钟左右），如需修改请手动更改- cron: '0 19 * * *'字段，生成表达式可以用https://crontab.guru/

