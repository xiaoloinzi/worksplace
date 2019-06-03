# encoding=utf-8
from GR1.formal_Class.PayMocker.util.Alipay.common import DataHelper



# 订单业务

def alipay_trade_precreate(contentDic=None):
#     校验,通过校验模块进行校验
# 消息返回
    response = DataHelper.readfile("E:\\worksplace\\GR1\\formal_Class\\PayMocker\\util\\Alipay\\data\\response\\alipay_trade_precreate_response.json")
    return response
def alipay_trade_pay(contentDic=None):
#     校验,通过校验模块进行校验
# 消息返回
    response = DataHelper.readfile("E:\\worksplace\\GR1\\formal_Class\\PayMocker\\util\\Alipay\\data\\response\\alipay_trade_pay_response.json")
    return response





