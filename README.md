# MagicMirrorGit
<h1>注意Linux和windows读取的中文字符编码的不同，linux读取时是gbk而windows 读取时是utf-8</h1>
<h2>windows环境需要selenium+chromedriver，Linux环境需要使用selenium+firefoxdriver环境</h2>
<li>windows下依赖包安装相对简单使用pip install基本都能安装完成，chromedriver需要与自己的谷歌浏览器版本相对应，chromedriver.exe直接放入python path 的scripts文件夹下即可</li>
<li>raspi buster 10 只能使用firefoxdriver，安装方法：
<h3>windows 环境运行run.py</h3>
<h3>Linux 环境下运行runLinux.py</h3>
<h2>Linux下安装ttf字体</h2>
<ul>下载所需的字体ttf文件</ul>
<li>sudo mkdir /usr/share/fonts/my_fonts --新建my_fonts文件夹</li>
<li>ttf文件放在Desktop，cd 进入桌面</li>
<li>mv DS-DIGIB.TTF /usr/share/fonts/my_fonts 将字体移动到自己的文件夹</li>
<li>cd /usr/share/fonts/my_fonts </li>
<li>sudo mkfontscale</li>
<li>sudo mkfontdir</li>
<li>sudo fc-cache -fv</li>
</ul>
<p>返回succeed 则字体安装成功</p>
