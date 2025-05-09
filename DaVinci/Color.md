# 达芬奇调色师笔记

Date: 2025-02-03
---

## 1 在时间线上调色

课程目标:

- 平衡素材
- 创建色彩连贯性
- 对画面局部调色和增强

调色工作流程:

- 平衡与镜头匹配
  - 正常化: 亮度调整
  - 色彩平衡: 消除偏色
  - 镜头匹配: 消除相似镜头的差异(对比度和色彩)
- 执行二级调色: 仅对某些区域进行调整
  - 抠像: 基于一个特定的色相/饱和度/亮度范围来限定出图像的一部分
  - 遮罩: 利用几何矢量图形来隔离图像的一部分
  - 实际工作中往往是抠像和遮罩共同作用
- 创建风格化调色: 调整场景的色温来传递情绪, 并使用色彩和色调对观众的心理进行不同程度的影响, 暗示某些变化.
- 节点编辑器中的调色流程图
  - 一级校色
  - 二级调色
  - 风格化调色

> 人眼对光源和阴影特别敏感--这就是"先调光后调色"的理论基础.

### 1.1 调光

调色页面右下部--示波器--波形图--只显示亮度Y:
示波器的纵坐标代表画面的总体可用亮度范围.
横坐标代表图像本身, 可将图像与示波器画面对应.
各个色彩通道的波形产生重叠, 白色波形代表每个通道都有相同的强度.

在正常化素材时, 一个好的起始点是确保示波器中阴影分布在黑点0之上的5~10%之间, 同时纯白的亮部影刀止于白点之下90%, 剩余部分用于车灯/阳光/金属反射高光等.

调整方式:

- 一级校色轮
- 曲线

曲线工具相对来说更简便和灵活

一级校色轮旁的小框:

- 对比度
- 轴心: 用于改变黑白部分的比例 通过调整对于暗部和亮部的优先级来控制对比度平衡
- 色调: 即色彩的名称, 与色相类似, 色彩的本质特征(与饱和度和亮度一起构成色彩的三要素)
- 色温: 黑体辐射光谱--与温度有关, 常用于烘托气氛

### 1.2 平衡色彩

画面为白色时, 波形图中的RGB通道应该重合成白色, 否则在曲线面板中选择对应的通道进行调整, 从而使之重合.

Cmd+D: 绕过此次调色
Shift+D: 绕过所有调色

黑灰白渐变图像是直观理解个调色工具和调色理念的重要工具

一级校色轮和log校色轮之间相比: log校色轮改变的范围更小更精确, 一级校色轮范围更大更全面.
校色轮可以用来建立基本的亮度范围和对比度, 而log色轮则可以用作二级调整以进一步优化三个亮度范围
log色轮在处理曝光不足或过度曝光时尤其高效.

Opt+Z: 切换校色轮和log校色轮

假设: 高光部分占比很少, 整体偏暗, 暗部细节压缩严重的情况下. 
适当调高中灰部分避免高光被裁切, 又能提升暗部细节; 切换到log校色轮, 调整**范围**后再降低阴影部分亮度即可

知识点: log校色轮中的范围选项是一个很重要的参数, 用于控制改变的范围.

## 2 创建色彩连贯性

素材来源的多样性会在时间线上造成色彩不统一, 容易使得观众出戏.

G: 添加旗标

可将具有某些相同特征或要求的片段加上不同颜色的旗标, 可在上部片段选项中显示或隐藏某一颜色旗标的片段, 从而节省在时间线中寻找的时间同时又不会遗漏需要修改的片段.

### 2.1 镜头匹配

- 选择目标片段, Opt+S新建镜头匹配串行节点
- 右击基准片段--"与此片段进行镜头匹配"
- 目标片段将被匹配
- 匹配只是一个很好的起点, 还需要进一步调整

### 2.2 静帧匹配镜头

创建静帧: 监视器右击--抓取静帧

应用:

- 选择片段, 示波器选择"分量图"
- 双击静帧, Opt+W可翻转划像
- 分量图中被分为左右两部分, 可以很清晰的比较出差异
- 新建串行节点, 推荐使用校色条调整至三通道大致相同

## 3 调整并增强部分区域

### 3.1 借助窗口和控制饱和度来吸引注意力

窗口工具用于做遮罩, 调色仅针对窗口范围之内,窗口之外的部分对所有调整无效
对需要吸引目光的部分增加饱和度和对比度
对非引导部分降低中灰亮度和对比度

- Shift+H: 突出显示遮罩切换开关
- Shift+`: 窗口控制器显示切换开关
- Opt+O: 新建外部节点, 反转前一个节点的键数据(选区)

窗口工具可直接反转

### 3.2 使用锐化突出画面关键元素

- 中调色面板中打开模糊面板--第二个图标激活锐化模式
- 半径向上是模糊, 向下则是锐化, 调整至0.40
- 缩放比例: 0.5 增加/减弱"半径"的调整浓度
- 级别: 设置锐化的阈值
- 核心柔化: 调整锐化权重
  最重要的参数就是半径, 其余的可用窗口跟踪排除在外

Cmd+Shift+H: 突出显示

### 3.3 跟踪复杂的画面元素

- 创建节点用于跟踪
- 合适的窗口工具套住目标物
- 通常的做法是从屁那段的中间或结尾处跟踪
- 剧烈变化时会跟丢, 在跟踪数据图表中框选出坏数据删除
- 切换跟踪模式为"帧"模式
- 手动将窗口重新移动到之前跟踪的区域
- 每一次手动改变都会建立一个新的关键帧
- 正向和反向跟踪完即可

### 3.4 修正阴天

选取出合适的选区是关键

- 新建Sky节点--限定器
- 鼠标点击天空部分, Shift+H突出显示
- 拖动色相, 饱和度和亮度滑块来微调选区
- 另一个隐藏技巧是可逐个禁用每个参数以观测选区的质量
- 切换蒙版到黑白模式
- 蒙版优化
  - 预处理滤镜: 可对原始图像进行一些小的清理, 用于减少类似宏块导致的压缩伪像.
  - 净化黑场: 用来缩小遮罩中非常小的选区来消除噪点
  - 净化白场: 可放大树枝之间的白色区域
  - 后处理滤镜: 会通过将原始图像中的一些袭击重新引入选区来清理蒙版区域.
  - 模糊半径: 更柔和的边缘可隐藏选区的一些缺陷
- 使用窗口来隔离限定器, 排除无关的区域

限定器选区的效果通常取决于素材本身的特点和画面质量

### 3.5 色彩扭曲器

这款工具分两个: 色相和饱和度的蜘蛛网, 以及色度-亮度网格

蜘蛛网:

- 径向控制饱和度
- 弧向控制色相
- 在画面上用鼠标滑过草地, 观察蜘蛛网上的激活点
- 鼠标框选, 调整到合适的色相和饱和度
- 使用窗口选区隔离无关区域

色度-亮度:

- 两个网格描绘了3D空间中色度-亮度立方体的两个横截面
- 横轴表示色度, 纵轴表示亮度
- 选择网格底部两行的任意控制点--点击选择行--点击将所选转换为固定, 锁定该行上所有的控制点
- 面板底部拖动"转轴角度"到20.00, 确定将要做哟的天空色相范围
- 网格1中调出更黄的色调, 网格2中调出更品的色调

<mark>这一工具背后的原理不清楚, 暂时不会.</mark>

### 3.6 手动调整肤色

"色相对色相"面板以线性的方式显示所有色相, 并在两侧的红色区域中为一个循环

- 点击监视器中曝光正常的皮肤, 会得到三个点
  - 中间点为所选色相
  - 两边的点为可用来调整色相的范围
- 中心控制点稍微往下拖动, 消除肤色中的偏红部分
- 输入色相和色相旋转不知道怎么用

矢量示波器: 会将画面数据呈现在表示当前画面的色相及饱和度分布的圆形范围中. 经过合理平衡的画面通常会显示未中心附近的"像素云", 其中偏离中心的部分表示不同色相饱和度较高的画面元素.

*Tips:*
通过曲线模式的命名, 就可以看出其选择并调整的模式.

- "色相对饱和度": 意味着你要针对特定的色相来调整各自的饱和度
- "饱和度对亮度": 你要针对图形中的某个特定饱和度的区域来调整亮度
- 命名规则: 第一个词表示用于选区的色彩属性, 第二个词表示将会影响的属性

## 4 掌握节点处理流程

每个节点都会影响图像结果，它会通过RGB链接输出更改后的信号，直到最终的RGB数据到达节点编辑器的输出节点。输出节点会把图像的最终状态呈现到检视器中，以此决定画面在渲染时的样子。
节点还能够复用来自上游节点的信息，从而大大减少了组建和输出最终图像所需的运算开销。这一功能通常在使用键时非常有帮助, 例如限定器和窗口生成的键.

### 4.1 并行节点

Opt+P: 创建并行节点
并行混合器可以均等的混合多个节点的调色操作; 类似串行节点, 区别在于并行节点能够从同一节点提取RGB信息.

![并行](media/并行.png)

### 4.2 图层节点

Opt+L: 新建图层节点
![图层](media/图层.png)
通过两张图片可以理解并行节点和图层节点的异同; 一般情况下并行节点足够使用

## 5 群组
