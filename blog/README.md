DEMO
===========================

###########环境依赖
python 3.4+
mysql or mssql

###########部署步骤
1. 安装项目依赖的包
    pip install -r requirements.txt


2. 到项目中对数据库进行创建并对应于config文件 

3.  到项目中执行脚本 如果是新装要执行1.python manage.py db init 2.python manage.py db migrate 3.更新python manage.py db upgrade  
 //创建数据库


4. 启动项目
    python blog.py 



###########目录结构描述
├── Readme.md                   // help
├── blog.py                         // 应用
├── config.py                      // 配置
├── models.py                      //数据库模型
├── manage.py                     // 数据库更新创建脚本
├── static                      // web静态资源加载
│   └── css                 //css 文件
│   └── images            //images文件
├── templates                      // html页面
│   └── base                 //基础模板





###########V1.0.0 版本内容更新
1. 新功能     增加删除文章功能
