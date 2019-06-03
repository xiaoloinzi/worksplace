# encoding=utf-8
import requests
def test_alipay_trade_precreate():
    url = "http://127.0.0.1:8002/tradePrecreate"
    param={"biz_content": '{"out_trade_no":"209","seller_id":"2088102146225135","total_amount":88.88,"discountable_amount":8.88,"subject":"Iphone6 16G",      "goods_detail":[{        "goods_id":"apple-01","goods_name":"ipad","quantity":1,"price":2000,"goods_category":"34543238","body":"特价手机","show_url":"http://www.alipay.com/xxx.jpg"        }],"body":"Iphone6 16G","operator_id":"yx_001","store_id":"NJ_001","disable_pay_channels":"pcredit,moneyFund,debitCardExpress","enable_pay_channels":"pcredit,moneyFund,debitCardExpress","terminal_id":"NJ_T_001","extend_params":{"sys_service_provider_id":"2088511833207846"    },"timeout_express":"90m"  }'}
    r = requests.post(url,params=param,timeout=10)
    print r.content


def test_alipay_trade_pay():
    url = "http://127.0.0.1:8002/tradePay"
    param={"biz_content": '{    "out_trade_no": "88",    "product_code": "FACE_TO_FACE_PAYMENT",    "scene": "bar_code",    "auth_code": "28763443825664394",    "buyer_id": "2088202954065786",    "seller_id": "2088102146225135",    "discountable_amount": 8.88,    "total_amount": 88.88,    "subject": "Iphone6 16G",    "body": "Iphone6 16G",    "goods_detail": [        {            "goods_id": "apple-01",            "goods_name": "ipad",            "quantity": 1,            "price": 2000,            "goods_category": "34543238",            "body": "特价手机",            "show_url": "http://www.alipay.com/xxx.jpg"        }    ],    "operator_id": "yx_001",    "store_id": "NJ_001",    "terminal_id": "NJ_T_001",    "extend_params": {        "sys_service_provider_id": "2088511833207846"    },    "timeout_express": "90m"}'}
    r = requests.post(url,params=param,timeout=10)
    print r.content
if __name__ == '__main__':
    #交易预创建接口
    test_alipay_trade_precreate()
    #交易支付接口
    # test_alipay_trade_pay()