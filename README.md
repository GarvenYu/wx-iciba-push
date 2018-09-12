# wx-iciba-push
---
**项目说明：** 将爱词霸每日一句推送到微信
# 效果图
---
![每日一句](http://github-readme-img.oss-cn-shenzhen.aliyuncs.com/wx-iciba-push.png)
# 使用的API
---
**爱词霸获取每日一句：**[爱词霸每日一句](http://open.iciba.com/?c=wiki)
**微信接口测试公众号：**[微信接口测试公众号](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)
# 注意的问题
---

1. 解码爱词霸的json数据
2. 微信测试公众号：
   1. 填写内容模板
   2. 获取access_token
   3. 获取用户列表
   4. 推送消息
   5. Linux服务器使用crontab设置定时任务即可每天接受到推送
3. **仔细阅读服务号开发文档**[微信开发文档](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1445241432)
### 给自己打个广告
---
关注下我的个人博客v1.0[传送门](www.fre3sia.site)

有任何问题可以在留言板留言给我。
