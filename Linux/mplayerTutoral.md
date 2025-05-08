# Mplayer tutoral
---

MPlayer 是我在 Linux 系统中用到的相当好的媒体播放程序，它因支持播放广泛的音频/视频文件格式而著称。本文所要探讨的，除却一般的使用方法之外，更包括一些鲜为人知的提示和诀窍。相信在阅读此文后，你的多媒体播放体验将会增色不少。

## 播放文件

使用 MPlayer 播放媒体文件最简单的方式是：

	mplayer <somefile>

MPlayer 会自动检测文件的类型并加以播放，如果是音频文件，则会在命令行中显示该播放文件的状态信息；而假如是视频文件的话，则会打开一个新的播放窗口。

## 倒退与快进

在播放文件的时候，你可以通过以下三组快捷键来对播放进程进行倒退与快进操作：

 -   左方向键和右方向键：分别执行倒退 10 秒和快进 10 秒操作
 -   下方向键和上方向键：分别执行倒退 1 分钟和快进 1 分钟操作
 -   下翻页键和上翻页键：分别执行倒退 10 分钟和快进 10 分钟操作

## 使用字幕

当播放电影文件时，你可以指定字幕文件：

	mplayer -sub <somesubtitlefile> <somefile>

在播放 DVD 电影时，你也可以通过指定语言代码来使用字幕：

	mplayer dvd://<titlenumber> -slang nl,en

这样，MPlayer 就会优先使用荷兰语字幕，如果该语言不可用，则再使用英语字幕。

## 有用的快捷键

以下是 MPlayer 中一些有用的快捷键：

-    f－当播放视频时，在全屏和窗口模式之间切换。你也可以在命令行中使用 -fs 选项，以便让 MPlayer 开始在全屏模式中播放。
-    o－在播放视频时切换 OSD（OnScreen Display）模式。
-    p 或 Space－暂停／继续播放。
-    q 或 Esc－退出 MPlayer。在 GUI 模式时，Esc 不会退出，仅停止播放。
-    / 和 * 或 9 和 0－减小或增大音量。
-    m－静音切换。
-    T（通常是 Shift + t）－播放窗口置顶切换。
-    b 和 j－在可用的字幕间循环。
-    x 和 z－调整字幕的延迟时间。
-    I（Shift + i）－显示播放电影的文件名称。
-    1 和 2－调整对比度。
-    3 和 4－调整亮度。
-    5 和 6－调整色度。
-    7 和 8－调整饱和度。

## 播放流媒体

如果 MPlayer 无法自动找到播放列表或直接的流媒体文件，你可以尝试使用 -playlist 选项：

	mplayer -playlist <file or url>

同时你也可以设置较大的缓存：

	mplayer -cache 8192 -playlist <file or url>

指定缓存大小的单位是 KB，上面的命令将允许 MPlayer 使用 8 MB 缓存。你可以使用 -cache-min 选项来改变 MPlayer 占用缓存的百分比：

	mplayer -cache 8192 -cache-min 50 -playlist <file or url>

## 循环播放

如果你想让媒体文件循环播放，可以使用 -loop 选项：

	mplayer -loop 3 <somefile>

上面的命令将播放 <somefile> 3 次，然后才退出。

	mplayer -loop 0 <somefile>

上面的命令将永远重复播放 <somefile>。

## 改变播放速度

你可以使用 -speed 选项来改变 MPlayer 播放媒体文件的速度。值为 1.0，意味着正常速度；0.5 意味着慢两倍；2.0 意味着快两倍。像这样指定选项：

	mplayer -speed 2.0 <somefile>


## 指定纵横比

当你在宽屏中播放电影时，可能想要使用 16:9 的纵横比：

	mplayer -aspect 16:9 <somefile>

在非宽屏中，你可以使用 4:3 的纵横比。

##将选项放置到 MPlayer 的配置文件中

对于一般用户来说，该配置文件位于 ~/.mplayer/config；全局的配置文件在 /etc/mplayer/config。不同的值使用行分隔，如：

	# MPlayer config file
	srate=48000
	ao="pcm:file=dumpedaudio.wav"

有时从网络上down下来的视频音量太小那么:

	softvol=yes		#软件控制音量开
	volume=30		#默认起始音量30%
	softvol-max=300	#软件控制最大音量是原始音量的300%
	
	# 这里的逻辑就是,音量正常的视频正常播放,音量太小的继续软件增益可以加大.
