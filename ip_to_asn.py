import ipaddress

# 基底となる4octet ASN
base_asn = 4200000000

# 変換対象のIP addressを入力
input_ip = input('Input IP Address: ')

# 入力したIPを32bitバイナリに変換し下位3オクテット(9bit目から)を10進数変換
convert_ip = int(format(int(ipaddress.IPv4Address(input_ip)),'032b')[8:], 2)

# ASNの算出
convert_asn = base_asn + convert_ip
print('AS Number: ' + str(convert_asn))
