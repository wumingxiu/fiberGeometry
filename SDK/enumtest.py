def enum(**enums):
    return type('Enum', (), enums)

        
emSdkLutMode = enum(
LUTMODE_PARAM_GEN = 0 ,#//通过调节参数动态生成LUT表
LUTMODE_PRESET = 1 ,#使用预设的LUT表
LUTMODE_USER_DEF  = 2) # //使用用户自定义的LUT表


emSdkRunMode = enum(
RUNMODE_PLAY = 0 ,#正常预览，捕获到图像就显示。（如果相机处于触发模式，则会等待触发帧的到来）
RUNMODE_PAUSE = 1 ,#暂停，会暂停相机的图像输出，同时也不会去捕获图像
RUNMODE_STOP  = 2) # //停止相机工作。反初始化后，相机就处于停止模式


emSdkDisplayMode = enum(
DISPLAYMODE_SCALE = 0 ,#缩放显示模式，缩放到显示控件的尺寸
DISPLAYMODE_REAL  = 1) # //1:1显示模式，当图像尺寸大于显示控件的尺寸时，只显示局部


emSdkRecordMode = enum(
RECORD_STOP  = 0 ,#停止
RECORD_START = 1 ,#录像中
RECORD_PAUSE  = 2) # //暂停


emSdkMirrorDirection = enum(
MIRROR_DIRECTION_HORIZONTAL  = 0 ,#//水平镜像
MIRROR_DIRECTION_VERTICAL  = 1) # //垂直镜像


emSdkRotateDirection = enum(
ROTATE_DIRECTION_0  = 0 ,# 不旋转
ROTATE_DIRECTION_90 = 1 ,# 逆时针90度
ROTATE_DIRECTION_180 = 2 ,# 逆时针180度
ROTATE_DIRECTION_270 = 3) #  逆时针270度


emSdkFrameSpeed = enum(
FRAME_SPEED_LOW  = 0 ,#低速模式
FRAME_SPEED_NORMAL = 1 ,#普通模式
FRAME_SPEED_HIGH = 2 ,#高速模式(需要较高的传输带宽,多设备共享传输带宽时会对帧率的稳定性有影响)
FRAME_SPEED_SUPER //瓒呴珮閫熸ā寮�(闇�瑕佽緝楂樼殑浼犺緭甯﹀ = 3) # 多设备共享传输带宽时会对帧率的稳定性有影响)


emSdkSnapMode = enum(
CONTINUATION  = 0 ,#//连续采集模式
SOFT_TRIGGER = 1 ,#软件触发模式，由软件发送指令后，传感器开始采集指定帧数的图像，采集完成后，停止输出
EXTERNAL_TRIGGER  = 2) # //硬件触发模式，当接收到外部信号，传感器开始采集指定帧数的图像，采集完成后，停止输出


emSdkLightFrequency = enum(
LIGHT_FREQUENCY_50HZ  = 0 ,#//50HZ,一般的灯光都是50HZ
LIGHT_FREQUENCY_60HZ //60HZ = 1) # 主要是指显示器的


emSdkParameterMode = enum(
PARAM_MODE_BY_MODEL  = 0 ,#根据相机型号名从文件中加载参数，例如MV-U300
PARAM_MODE_BY_NAME = 1 ,#根据设备昵称(tSdkCameraDevInfo.acFriendlyName)从文件中加载参数，例如MV-U300,该昵称可自定义
PARAM_MODE_BY_SN = 2 ,#根据设备的唯一序列号从文件中加载参数，序列号在出厂时已经写入设备，每台相机拥有不同的序列号。
PARAM_MODE_IN_DEVICE  = 3) # //从设备的固态存储器中加载参数。不是所有的型号都支持从相机中读写参数组，由tSdkCameraCapbility.bParamInDevice决定


emSdkPropSheetMask = enum(
PROP_SHEET_INDEX_EXPOSURE  = 0 ,#
PROP_SHEET_INDEX_ISP_COLOR = 1 ,#
PROP_SHEET_INDEX_ISP_LUT = 2 ,#
PROP_SHEET_INDEX_ISP_SHAPE = 3 ,#
PROP_SHEET_INDEX_VIDEO_FORMAT = 4 ,#
PROP_SHEET_INDEX_RESOLUTION = 5 ,#
PROP_SHEET_INDEX_IO_CTRL = 6 ,#
PROP_SHEET_INDEX_TRIGGER_SET = 7 ,#
PROP_SHEET_INDEX_OVERLAY = 8 ,#
PROP_SHEET_INDEX_DEVICE_INFO = 9) # #


emSdkPropSheetMsg = enum(
SHEET_MSG_LOAD_PARAM_DEFAULT  = 0 ,#参数被恢复成默认后，触发该消息
SHEET_MSG_LOAD_PARAM_GROUP = 1 ,#加载指定参数组，触发该消息
SHEET_MSG_LOAD_PARAM_FROMFILE = 2 ,#从指定文件加载参数后，触发该消息
SHEET_MSG_SAVE_PARAM_GROUP  = 3) # //当前参数组被保存时，触发该消息


emSdkRefWinType = enum(
REF_WIN_AUTO_EXPOSURE  = 0 ,#
REF_WIN_WHITE_BALANCE = 1) # 


emSdkResolutionMode = enum(
RES_MODE_PREVIEW  = 0 ,#
RES_MODE_SNAPSHOT = 1) # 


emSdkClrTmpMode = enum(
CT_MODE_AUTO  = 0 ,#自动识别色温
CT_MODE_PRESET = 1 ,#使用指定的预设色温
CT_MODE_USER_DEF  = 2) # //自定义色温(增益和矩阵)


emSdkLutChannel = enum(
LUT_CHANNEL_ALL  = 0 ,#//R,B,G三通道同时调节
LUT_CHANNEL_RED = 1 ,#红色通道
LUT_CHANNEL_GREEN = 2 ,#绿色通道
LUT_CHANNEL_BLUE = 3) # 蓝色通道


emSdkIspProcessor = enum(
ISP_PROCESSSOR_PC  = 0 ,#//使用PC的软件ISP模块
ISP_PROCESSSOR_DEVICE  = 1) # //使用相机自带的硬件ISP模块


emStrobeControl = enum(
STROBE_SYNC_WITH_TRIG_AUTO  = 0 ,#和触发信号同步，触发后，相机进行曝光时，自动生成STROBE信号。此时，有效极性可设置(CameraSetStrobePolarity)。
STROBE_SYNC_WITH_TRIG_MANUAL = 1 ,#和触发信号同步，触发后，STROBE延时指定的时间后(CameraSetStrobeDelayTime)，再持续指定时间的脉冲(CameraSetStrobePulseWidth)，有效极性可设置(CameraSetStrobePolarity)。
STROBE_ALWAYS_HIGH = 2 ,#始终为高，忽略STROBE信号的其他设置
STROBE_ALWAYS_LOW  = 3) # //始终为低，忽略STROBE信号的其他设置


emExtTrigSignal = enum(
EXT_TRIG_LEADING_EDGE  = 0 ,#上升沿触发，默认为该方式
EXT_TRIG_TRAILING_EDGE = 1 ,#下降沿触发
EXT_TRIG_HIGH_LEVEL = 2 ,#高电平触发,电平宽度决定曝光时间，仅部分型号的相机支持电平触发方式。
EXT_TRIG_LOW_LEVEL = 3 ,#低电平触发
EXT_TRIG_DOUBLE_EDGE = 4) # 双边沿触发


emExtTrigShutterMode = enum(
EXT_TRIG_EXP_STANDARD  = 0 ,#标准方式，默认为该方式。
EXT_TRIG_EXP_GRR = 1) # 全局复位方式，部分滚动快门的CMOS型号的相机支持该方式，配合外部机械快门，可以达到全局快门的效果，适合拍高速运动的物体


emEvaluateDefinitionAlgorith = enum(
EVALUATE_DEFINITION_DEVIATION  = 0 ,# 方差法
EVALUATE_DEFINITION_SMD = 1 ,# 相邻像素灰度方差法
EVALUATE_DEFINITION_GRADIENT = 2 ,# 梯度统计
EVALUATE_DEFINITION_SOBEL = 3 ,# Sobel
EVALUATE_DEFINITION_ROBERT = 4 ,# Robert
EVALUATE_DEFINITION_LAPLACE = 5 ,# Laplace
EVALUATE_DEFINITION_ALG_MAX = 6) # 


emCameraGPIOMode = enum(
IOMODE_TRIG_INPUT  = 0 ,#触发输入
IOMODE_STROBE_OUTPUT = 1 ,#闪光灯输出
IOMODE_GP_INPUT = 2 ,#通用型输入
IOMODE_GP_OUTPUT = 3 ,#通用型输出
IOMODE_PWM_OUTPUT = 4) # PWM型输出

