# 创建二维码
import qrcode,base64


def CreateCode(code):
    msg = f"Test App|9c04b45a-0f96-4474-8cc2-08770394d57c||A8A91948-A594-A2DB-CC29-3497F69F40AD|{code}|D13001|"
    str = base64.b64encode(msg.encode("utf-8")) # base64加密
    qr = qrcode.QRCode(box_size=10, border=10)
    qr.add_data(str)
    img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))  # 生成图片对象
    code_img = img.show()  # 展示图片
    return code_img


CreateCode('测试标识码eU1')