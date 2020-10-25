import ipaddress

def convert_ip_asn(host_ip):
    """
    引数で受け取ったホストIPアドレスをAS番号に変換する関数
    """
    # 基底となる4octet ASN
    base_asn = 4200000000

    # 入力したIPを32bitバイナリに変換し下位3オクテット(9bit目から)を10進数変換
    convert_ip = int(format(int(ipaddress.IPv4Address(host_ip)),'032b')[8:], 2)

    # ASNの算出
    return base_asn + convert_ip

# 変換対象のIP addressを入力
input_ip = input('Input IP Address: ')

print('AS Number: ' + str(convert_ip_asn(input_ip)))
