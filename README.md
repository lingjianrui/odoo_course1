[TOC]

# What is Odoo? and Why?
1. Odoo 是一个模块化的 Erp 系统 功能很强大
2. Odoo Community Edition是开源的 Enterprise Edition 是收费的。(遗憾的是 他是 GPL 的)
3. 成熟的社区资源和app store，可以下载很多收费和免费的应用。
4. 使用python语言, postgresql数据库 开发快 上手容易，系统稳定。
5. 支持docker快速部署 源码部署，和数据库管理工具



## Demo
### website快速构建企业门户
![image](https://github.com/lingjianrui/odoo_course1/raw/master/screenshots/快速创建企业门户.gif)
              
### 模块化安装及丰富的已有的模块 & 强大的线上商店
![image](https://github.com/lingjianrui/odoo_course1/raw/master/screenshots/丰富的应用.gif)

### 多用户权限控制
![image](https://github.com/lingjianrui/odoo_course1/raw/master/screenshots/多用户权限.gif)

# Installation
## 源码安装
` /Users/xiaohei/Downloads/odoo-10.0/odoo-bin --addons-path=addons,mymodules -d odoo10standard -u release_module `
--addons-path   指定要加载的模块的路径 addons 是odoo 官方提供的模块, mymodules是 自定义的模块 可以在系统的任何位置
-d 指定数据库
-u 指定要更新的模块 这里的更新 仅仅指 xml 的更新，如果改了 python 代码 仍然需要重启odoo 才可以。
## Docker安装
以下是一些常用的启动方式，并不需要按顺序执行
1. 启动postgresql数据库
` $ docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo --name db postgres:9.4`
2. 启动odoo
` $ docker run -p 8069:8069 --name odoo --link db:db -t odoo `
3. 启动odoo 挂在插件
` docker run -v /path/to/addons:/mnt/extra-addons -p 8069:8069 --name odoo --link db:db -t odoo `
4. 启动挂在数据库
``` 
docker run -v /opt/my-addons:/mnt/extra-addons -v /var/www/testing:/opt/testing -v /var/lib/docker/volumes/324bfe0bde851f542bd72047cdcd7922510c3da7c4bcc409ace6cb8d54dcfc67/_data:/var/lib/odoo -v /data/csmp_release/latest:/opt/latest -p 8070:8069 --name odoo1 --link db:db -t odoo:v10
```
# QuickStart
## simple_module
只需要两个文件就可以被odoo的模块发现机制发现
```
├── simple_module
│   ├── *__init__.py*     
│   └── *__manifest__.py*
```
```
__init__.py  内容为空
__manifest__.py 内容如下
# -*- coding: utf-8 -*-
{
    'name': 'simple_module',
    'version': '10.0.0.1.0',
    'author': "xiaohei",
    'depends': [],
    'data': []
}
```




## simple_module_ii
增加模型, 视图, 菜单 , 菜单窗口
**Add model , view and menu**
```
├── simple_module_ii
│   ├── *__init__.py*
│   ├── *__manifest__.py*
│   ├── models.py
│   ├── static
│   │   └── description
│   │       └── icon.png
│   └── view.xml
```
为了给应用增加一个图标,不得不创建一个static目录，在将图标文件放到description文件夹中
odoo 会默认读取这个文件 并将它展示在 应用管理的列表中

下面这个图标是显示在 应用菜单中 需要在定义 菜单的时候增加

```
view.xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <!--表单视图定义  id只能包含一个 .  最好不要带 .  name 只用作页面上的展示-->
    <record id="simple_module_ii_student_form" model="ir.ui.view">
        <field name="name">simple_module_ii.student.form</field>
        <field name="model">simple_module_ii.student</field>
        <field name="arch" type="xml">
            <form>
                <group>
                    <field name="name"/>
                </group>
            </form>
        </field>
    </record>
    <!--列表视图定义-->
     <record id="simple_module_ii_student_tree" model="ir.ui.view">
        <field name="name">simple_module_ii.student.tree</field>
        <field name="model">simple_module_ii.student</field>
        <field name="arch" type="xml">
           <tree>
               <field name="name"/>
           </tree>
        </field>
    </record>
    <!--模块图标定义-->
    <menuitem id="simple_module_ii_menu" name="模块简单教程II" sequence="10" web_icon="simple_module_ii,static/description/icon.png"/>
    <!--菜单动作定义 注意 菜单要引用菜单动作，所以 菜单动作先定义  这个name 是打开窗口的名字-->
    <record model="ir.actions.act_window" id="action_simple_module_ii_menu1">
        <field name="name">模块简单教程学生窗口</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">simple_module_ii.student</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree,form</field>
    </record>
    <!--菜单定义-->
    <menuitem id="simple_module_ii_menu1" name="学生" sequence="10" parent="simple_module_ii_menu" action="action_simple_module_ii_menu1"/>
</odoo>
```
## simple_module_iii
继承式开发 和 权限基本设置
```
simple_module_iii
├── *__init__.py*
├── *__manifest__.py*
├── models.py
├── security
│   └── ir.model.access.csv
├── static
│   └── description
│       └── icon.png
└── view.xml
```
**1.继承式开发**
开发一个新的模块来拓展老的模块，simple_module_iii 依赖simple_module_ii 并在ii的基础上为表单增加了一个字段。

**2.权限基本设置**
我们在模块的跟目录里增加了一个 securtiy 目录，并创建ir_model_access.csv 文件
我们可以指定具体的某些组的用户可以访问这个模块。
如果不加这个文件 除了admin之外的其他用户 默认是不会有权限访问这个模块的。
下面我们来分析一下 ir_model_access.csv 的内容
ir_model_access.csv 
```
id, name, model_id:id, group_id:id, perm_read, perm_write, perm_create, perm_unlink
access_student_group_user,simple_module_ii.student,model_simple_module_ii_student,base.group_user,1,1,1,1
```

为了方便阅读，我把他改了一个格式
```
id                          access_student_group_user  这个随便起名 保证唯一
name                        simple_module_ii.student   
model_id:id                 model_simple_module_ii_student   这个要引用 model的 id, 前面是model_开头 后面是model的id，但是不能有点，把点换成下划线
group_id:id                 base.group_user            这个就是员工那个组
perm_read                   1
perm_write                  1
perm_create                 1
perm_unlink                 1
```
看起来 还是蛮简单的吧, 当然这个设置也可以通过图形界面去设置调整


这样我们使用一个 非管理员帐号的 账户登录  就可以 看我们的app 了

## simple_module_iv Button 按键
view 与 model 的交互
在form表单 我们可以通过 下面这句 很容易定义
```
<button string="btn名字" type="object" name="action_publish" class="oe_highlight" attrs="{'invisible':[('state', '==', 'published')]}"/>
```
 1. name="action_publish"  这里的 action_publish 是指向 model中方法
 2. attrs="{'invisible':[('state', '==', 'published')]}"  表示 满足一定条件了  invisible属性就为 true
 这里意思是 当state 的值等于 published 的时候 就不让这个字段 显示出来
 3. self.write 在上面的代码中，可以看到 self.write 了一段数据 self.write 就可以操作数据 将数据持久化，state的值会被更新到数据库，
 当页面发现了state数据变更了，就会隐藏调publish 按钮
