# Editor官方视频教学笔记

Author: Chris

Date: 2025.03.20

---

## 1 Introduction to Editing

### 1.1 组织素材

媒体页面--媒体存储--右击添加新的文件位置, 可添加任意文件夹/外置硬盘等

正确组织素材目的是高效, 不要把时间浪费在寻找素材上, 同理, 如果工程简单, 素材简单, 过度优化也是低效和错误的.

- 在硬盘上合理组织素材

- 在媒体夹中组织的特殊性
  
  - 关键词: 选择同类素材, 元数据中关键词中写入合适的关键词--保存, 就会在智能媒体夹中自动显示 
  
  - 场景/人物等, 在偏好设置中开启
  
  - 可新建智能媒体夹创建逻辑自洽例如BROLL:
    
    - 媒体池文件属性--关键词--不包含--Interview/片尾
    
    - Opt+点击加号添加
    
    - 任意一项符合:
    
    - 媒体池文件属性--片段类型--是--video/Video+Audio

元数据可编辑 , 可利用!

自建智能媒体夹的原因可归纳为: 懒得为那么多素材夹关键词

### 1.2 剪辑补遗

Shift+鼠标滚轮: 调整音视频轨道高度

Shift+Z: 切换时间线全局查看和原来的时间线长度

Shift+Cmd+,/.: 片段向前/后移动

修剪模式下的滑移操作对动作转场有奇效!

在重大改变或关键节点之前复制时间线是一个聪明的决定

轨道太多的时候, 轨道名和颜色设置是必要的

轨道顺序更改: Fairlight的调音台里可拖拽调整

添加素材时哪个轨道标记被选中自动添加到哪个轨道

时间线上标记长度: 作用是限定操作在时间维度上的限制, 例如三点剪辑法, 这里一次就限制了两点

- Shift+A: 在时间线上标出选中的片段长度

- 在时间线上打IO点, 可定义任意长度

- X: 全选当前全部剪辑长度

- Opt+X: 取消上面操作

- Opt+I/O: 取消入点/出点

原则: 人声最重要, 一定要保证人声清晰, 其他都是陪衬

音频局部调节: 音频轨道上Opt+点击添加关键帧调高/低

音频全轨道调节: 调音台电平推子

音频标准化: 选择, 右击

音效轨道: 单独调节音量一致后再电平推子整体调节; 音效重叠处淡入淡出, 效果专业连贯 

## 2 多机位剪辑

多机位剪辑的第一步一定是同步素材, 同步依据包括时间码, 音频等, 实际工作中以音频的占多数.

每台摄像机都有现场录音, 还有一条专业的录音音频, 实现方式为: 每台摄像机依照现场录音波形为依据进行同步, 专业的录音音频作为剪辑时的音频.

## 2.1 双机位剪辑

时间线上打I/O点可直接删除很高效, 可代替Cmd+B操作



1. 新建时间线上放入AB两段, 将A或B拖入不同的轨道, 全选, 右击--自动同步--波形

2. 媒体池中右击时间线--将时间线转换为多机位片段. 这将关闭时间线, 因为此时转换为多机位剪辑而不是时间线了.

3. 将多机位剪辑放入另外时间线的合适位置, 进行正常编辑, 得到电台剪辑版, 会产生若干跳切

4. SourceViewer中点击视频B, 在跳切片段之间替换--隐藏缺陷

5. 在影片情绪节奏点上替换--提升影片质感

### 2.2 多机位剪辑

一个乐队的舞台演出



1. 对于一个媒体夹中都是多机位剪辑的情况: 右击--使用所选媒体夹创建多机位片段
   
   - 重命名
   
   - 角度同步方式: 音响
   
   - 角度命名方式: 元数据-相机
   
   - 勾选"Move source clip to 'Original Clips' bin"
   
   - 创建

2- 新建时间线

3- 点击主镜头, 在第一个演出音符出现前打入点I, F10覆盖到时间线

4- 主镜头可修改, 断开音视频锁定链接, 右击视频部分--切换多机位片段角度; 右击音频部分--切换多机位片段角度--选择专业录音

5- 在sourceViewer的左下角选择多机位, 并选择"纯视频", 这样可保证专业录音不会被替换

6- 开始播放, 粗略地凭感觉在SourceViewer中点击切换镜头, 得到粗剪版本
   
   - 所谓的感觉就是多看几遍多机位片段, 心中感觉会自然建立
   
   - 原则上声音对应画面, 各个镜头尽量都照顾到, 根据节奏切换

7- 添加编辑点/调整长短/切换镜头等等进行精修, 得到最终版本; 与普通剪辑最大的不同就是点击某个镜头就会替换时间线上的镜头
   
   - 修正不准确, 捕捉精彩画面, 修复瑕疵

8- 重新锁定音视频链接, 导出



## 3 剪辑页面中的视觉特效

### 3.1 理解复合片段

F11: Replace

Shift+F11: 适配填充(自动调节速度来满足填充时间线的限制)

复合片段的作用之一: 片段需要进行额外的处理之后再返回到主时间线/封装额外处理的内部细节



目标: 一张底图上制作4个画中画, 其中3个已完成, 只剩最后一个

1. 将片段放入时间线
   
   - 添加自定义轨道(音频数量0), 置于Archive 3 之上
   
   - 选择新建轨道, X选择全部长度--作用为选定剪辑作用的轨道, 和时间线范围.
   
   - 选择片段, Shift+F11适配填充轨道
   
   - 转入Compositing媒体夹, 右击片段, 新建复合片段Archive 4
   
   - 时间线左上角打开时间线堆叠
   
   - 右击片段在时间线上打开

2- 添加自定义轨道: 纯视频轨道, 在第一个视频下方

3- 在Matts媒体夹下选择"Matt 4 alpha"加入到时间线新建轨道中
   
   - 检查器中合成--合成模式: Alpha
   
   - 片段检查器中, 合成--合成模式: 前景, 此时效果出现
   
   - 返回原来的时间线

4- 检查器或屏幕控制的变换, 调整大小位置



### 3.2 绿幕抠像(3Dkeyer时间线)

1. 选择绿幕片段, 特效库中找到3D键控器, 双击, 自动添加的片段中

2. 检查器--特效选项卡

3. Viewer左下角选项--OpenFX叠加

4. 鼠标在绿色区域划线, 直到绿色部分没有灰色, 完全变成黑色为止; 下层视频轨道信号显示
   
   - 继续在边缘残留绿色的部分划线进行改善
   
   - 检查器中, 输出--突出显示Alpha(黑白); 蒙版优化: 净化黑场/白场
   
   - 关闭屏幕控制

5- 处理绿色溢出(绿幕映射到人物脸上和衣服上的绿色)
   
   - 行为选项--去除溢出色调整到1



### 3.3 2D变换贴图

1. 特效库选择变换, 开启屏幕控制--fx

2. 检查器--特效--控制模式: 交互-画布, 调整四个角到窗口的四个角, 关闭屏幕控制

3. 检查器--视频--合成: 叠加, 调整透明度80左右; 此时, 静态完美, 但一播放就露馅(不涉及Fusion中的追踪, 下面用关键帧解决)

4. 回到特效选项卡--动画--画布关键帧, 打开屏幕控制
   
   - 首帧打上关键帧, 跳到最后一帧
   
   - 调整四个角对应窗口
   
   - 关闭屏幕控制, 播放, 完美

关键帧替代Fusion追踪的前提是: 镜头运动平稳线性! 有抖动马上露馅, 或者多加关键帧节点进行调整



### 3.4 视频拼贴画

这里背景视频不一定要在视频轨道最下面



示例1:

1. 视频拼贴画设置:
   
   - 选择背景视频, 特效库--视频拼贴画, 双击
   
   - 检查器--特效--工作流程: 创建背景; 勾选布局预览; 贴片
   
   - 管理贴片--选择"Tile 4"; 勾选手动管理贴片--删除贴片; 再次选择"Tile 2"
   
   - 自定义大小形状--结束行: 2 (获得左侧1 3两小片, 右侧一大片的布局)
   
   - 贴片方式, 投影和贴片动画里分别设置美化
   
   - 取消勾选"布局预览", 勾选底部的"使用Alpha", 设置完成

2. 打开Viewer屏幕控制选择变换, 选择V3设置拖动

3. 其余两个如法炮制; 如遇放大遮挡其他画面切换屏幕控制到裁切



示例2:

1. 视频拼贴画设置:
   
   - 播放头置于LOGO刚出现时, 选择V3, 取消禁止显示
   
   - 特效库--Open FX--视频拼贴画, 双击
   
   - 检查器--特效--工作流程: 创建贴片; 勾选预览布局
   
   - 全局--布局: 调整3列1行, 圆角向右拉到头变成一行圆形; 调整垂直偏移, 将一行圆圈放在山脉之上
   
   - 贴片--贴片方式: 调整边框和颜色
   
   - 投影--调节阴影参数
   
   - 贴片动画--飞行动画: 向上飞行; 
   
   - 飞行进程: 后面点击关键帧动画变成红色, 播放头移到开头, 飞行进程调节一行圆圈置于画面上部, 后面自动打上关键帧
   
   - 取消预览布局

2- 检查器--特效--缩放内容: 调整三个参数使得内容恰当展示

3- V3时间线上Cmd+C复制

4- V4取消禁用, 时间线上Opt+V粘贴属性--选择插件, 检查器--特效--管理贴片--活动的贴片: Tile 2; 缩放内容中微调

5- V5如法炮制



当然, 剪辑页面的特效远不止此, 这里的示例只是让你对添加特效的一般步骤和操作逻辑有一个粗浅的认识, 还需要进一步探索和学习.
