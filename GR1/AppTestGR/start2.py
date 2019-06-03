# encoding=utf-8


#选取的特性：下载APP、查看我的功能验证。
#1、具备如下的能力，异常处理、截图、AW的封装
#0.1 用例信息封装成csv文件
#0.2 封装KW
#0.3、针对所有用例，设计配置文件，读取配置文件,返回参数值
#getTestDataInput(moduleName,testName)
#
#设计原则：测试用例一行，KWName.parma
#返回值：dict: KWName.parma:value

#2、生成日志文件
#createMainLog
# 返回值：log 对象
# 带filehandle 和 streamhandle
# 且其格式是：%(asctime)s","%(levelname)s","%(name)s","%(message)s"

#3、依据配置文件，获取要执行的用例
#说明：支持3种格式，格式1：*，格式2：modulename，格式3：modulename.TCName
# getCategories
# 入参：项目名称
# 返回值：
# moduleList = ['m1','m2']
# categoriesList = [['m1','t1'], ['m1','t2']]
# 实例：
# moduleList = ['Download']
# categoriesList = [['Download','download_app_notexist']]

#3、动态导入用例
##3.1 getScriptsList -- 使用到了动态导入模块的功能
# 入参：path
# 返回值：moduleList
# 其moduleList的意义如下：
# scriptModule = imp.load_source(moduleName, fileName)
# moduleList.append([moduleName,scriptModule])

#3.2 loadTestScripts
# 入参：self.projectName, self.testModelName, self.categoriesList
# 返回值：testsuit




#4、依据testsuit














