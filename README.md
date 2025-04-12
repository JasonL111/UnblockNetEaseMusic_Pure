# UnblockNetEaseMusic_Pure
一个简单的脚本来帮助大家在海外正常使用网易云。Python原生部署，不使用docker。

# 原理
每日自动用国内IP和网易云服务器交互一次来绕过IP限制。

# 使用方法


## 1. 下载程序
```bash
git clone https://github.com/JasonL111/UnblockNetEaseMusic_Pure.git
```
## 2. 安装依赖
一般来说，需要额外安装`requests`和`bs4`
```bash
pip install requests beautifulsoup4
```


## 3. 准备需要的参数
本项目成功运行需要一个参数`MUSIC_U`.
- 打开网易云(https://music.163.com/) 登录账号后 --> 按下`F12` --> `Application` --> `Cookies` --> `https://music.163.com`
- 找到所需要参数对应的数据.
- 找到代码中的这一行`music_u = ""`，填入你从浏览器获取的网易云音乐 Cookie 中的 MUSIC_U 值
注意：`MUSIC_U`有过期日期，若解锁失败的同时日志无异常，请考虑排查`MUSIC_U1`过期



# 参考项目

[UnblockNetEaseMusic](https://github.com/Kyle-Kyle/UnblockNetEaseMusic/blob/main/README.md?plain=1)
