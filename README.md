# MagicMirrorGit
<h1>注意Linux和windows读取的中文字符编码的不同，linux读取时是gbk而windows 读取时时utf-8</h1>
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
