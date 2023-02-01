## LemonLauncher使用指南

### 关于启动器

这是由HymnFo开发的Minecraft开源启动器，只在MacOS上可用，如果您是Windows用户请您移步至PCL2 启动器。

### 启动器报错指南

#### 报错声明

LemonLauncher是由Python制作的。由于语言自身限制某些地方可能会报错。HymnFo用的是MacOS12，某些依赖可能会因为操作系统的更改而报错。如果您出现了Python报错的情况您需要把报错窗口截图发送至“yincennan@163.com（商业勿扰）”。对于窗口使用不适您可以向“yincennan@126.com”投稿UI界面设计。

#### LemonLauncher因Python本身退出

系统会弹出“Python意外退出”提示，重启启动器即可，若问题依旧存在请提交到作者邮箱

### 登录方式

#### 离线登录

这是一种登录方式，仅限无网络时进行使用，并且账户名称是随机生成的。不能自己定义账户名，在不拥有Minecraft的情况下游玩Minecraft是违法的！请知悉。

#### 微软登录

HymnFo最推荐的一种登录方式，建议您使用此登录方式，如果在您输入最终网址后出现错误，请您检查账户是否购买Minecraft，如果您未购买请您前往“minecraft.net"进行购买。为避免盗号，启动器会每15天刷新一次账号，您的账号会被退出。

### Forge等扩展安装

#### Optfine高清修复

您需要到官网下载并手动安装。

#### Forge Mod加载器

您需要在安装Minecraft时安装

### 版本隔离

由于Python Minecraft-launcher-lib包的限制，软件不会自动进行版本隔离，需要您手动进行。在软件测试版通过后，HymnFo将会在下一版本添加上版本隔离功能。谢谢理解。

### LemonLauncher内置终端

您可以在主界面打开终端。命令指引如下：

```
launcher -login -microsoft
```

```
launcher -login url [登录后的URL]
```

打开浏览器进行Microsoft登录

```
launcher -login
```

添加离线临时账户

```
launcher -insall [minecraft version]
```

安装Minecraft

```
launcher -run [minecraft version]  -[user]
```

启动Minecraft

```
launcher -quitMC
```

退出Minecraft

```
launcher -quitLauncher
```

退出LemonLauncher

### 鸣谢

| 作者     | 联系方式             | 帮助                   |
| -------- | :------------------- | ---------------------- |
| Zheng ht | e2662020@outlook.com | 为启动器提供技术支持！ |
|          |                      |                        |

### LemonLauncher开发参考

```
Mine.py
https://github.com/e2662020/Python-Minecraft-Luncher
```



### LemonLauncher更新发布页

```
https://github/yincennan/LemonLauncher
```

