# ffmpeg之小白往前冲

ffmpeg工程浩大，功能繁复；非专业人士极容易望而生畏.加之中文文档偏少使得ffmpeg明珠暗投,被大多数人忽略.今天,本着不求甚解,但求能完成基本需求的精神进行一次冲锋.
下面是操作加猜测性注释:

```bash
#1.截取一段音频(估计视频也差不多这个意思)
ffmpeg -ss 00:00:10 -t 00:01:22 -i "Beat it.mp3"  output.mp3 
#-ss 	开始截取时间点
#-t		截取时长

#2.合并几段视频(有分有合才符合人类基本思维)
#2.1方式一:ffmpeg
ffmpeg -i part1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts
ffmpeg -i part2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts
ffmpeg -i part3.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp3.ts
ffmpeg -i "concat:temp1.ts|temp2.ts|temp3.ts" -c copy -bsf:a aac_adtstoasc out.mp4

#2.2方式二:mencode(作为mplayer系播放器的依赖已经装好了)
mencoder -oac pcm -ovc copy -idx -o output.mp4 file1.mp4 file2.mp4 file3.mp4
# 或者： 
mencoder -oac copy -ovc copy -idx -o output.mp4 file1.mp4 file2.mp4 file3.mp4
#之所以给出这种方式,你不觉得比方式一简洁了许多吗?

#3.格式转换(多设备,多用途当然要多格式)
ffmpeg -i input.原格式 output.目标格式
#这个够牛叉,点32个赞!

#4.字幕(如果你的英语专业八级以上或只看国产片的可以略过)
#注意:字幕编码应该是UTF-8编码,转换编码方法:vim -- :set fileencoding=utf-8
#方式一:嵌入字幕,通过播放器选择
ffmpeg -i input.mp4 -i subtitles.srt -c:s mov_text -c:v copy -c:a copy output.mp4

#方式二:将字幕直接写入视频文件,性能最高
ffmpeg -i subtitle.srt subtitle.ass		#先转成ass格式
ffmpeg -i input.mp4 -vf ass=subtitle.ass output.mp4

#5.录音:有两种方式,一种需要alsa-oss包,试了很久也没成功,本文采用第二种方式基于alasa-utils包
ffmpeg -f alsa -ac 2 -vol 512 -i hw:0,0 out.mp3
#-f alsa:基于alsa-utils软件包?不清楚.
#-ac 2:双声道?
#-vol 512:音量.默认256.
#-i hw:0,0:硬件设备

#6.屏幕录像:这个更牛叉,麻麻再也不会担心我的录像问题了.
ffmpeg -f x11grab -s wxga -r 24 -i :0.0+0+0 -qscale 5 foo.avi
#-f x11grab:基于X11软件包,这就是说纯命令行模式下不会工作.
#-s wxga:录制分辨率,应该和你的屏幕分辨率一致.wxga等效于1366x768,其它参数请man ffmpeg-utils
#-r 24:每秒采集24帧画面
#-i :0.0+0+0: 输入硬件0.0, +0+0应该是偏移量但不确定
#-qscale 5:应该是视频质量,数值越小质量越高,对应的文件越大.5应该是个折衷的值.
#不过这个录像可是没有声音的哦~

#7.有声录像:把上述两条命令加到一起就可以了,注意:音频在先.
ffmpeg -f alsa -ac 2 -vol 512 -i hw:0,0 -f x11grab -s wxga -r 24 -i :0.0+0+0 -qscale 5 output.avi
#槽点:	
#	1.只能输出avi格式,其它格式声音只有一小段,是我机器的特例还是通病?
#	2.必须要做录制完成后转码mp4,文件大小能缩小7倍左右.
#	3.因为偏移量的不理解,单独录制特定窗口暂时不能实现.不过我是i3-wm默认都是全屏,所以也不是个问题.
#单独录制窗口,确定窗口大小及位置:xwininfo然后点击目标窗口.

#8.录制摄像头捕获的影像.
ffmpeg -f v4l2 -s 640x480 -i /dev/video0 -qscale 5 output.mpg
ffmpeg -f alsa -i default -f v4l2 -s 640x480 -i /dev/video0 output.mpg
```

截图等功能有其它简洁替代方案,略过.

也许你会吐槽:这么长的命令怎么可能记得住?
最后再罗嗦一句:你知道alias么......
