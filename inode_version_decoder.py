#coding=utf-8

# H3C inode �汾�Ž��ܹ���
# ʹ�÷�����
# �޸�base64_dataΪ���inode������base64��Ϣ
# ���б��ű����۲�����İ汾�ţ�����16���ƽ��Ϊ׼
# �������汾�����������룬�����H3C��KEYֵ��������
from hashlib import md5
import base64
from binascii import hexlify

def XOR(txt,key):
    result =range(0,len(txt)) 
    new_key = key+key
    new_key = new_key[:len(txt)]
    new_key_r = new_key[::-1]
    for i in range(0,len(txt)):
        result[i] = new_key[i] ^ new_key_r[i] ^ txt[i]
    return result

H3C_KEY = 'Oly5D62FaE94W7'
# H3C_KEY = 'HuaWei3COM1X' # ���ܵ� H3C_KEY ֵ
base64_data = 'bTMMHhsGZ3YvHx5gJlQqf1D7G3Y='
raw = (base64.b64decode(base64_data))
raw2 = XOR(map(ord,raw),map(ord,H3C_KEY))
random_key = raw2[16:]
random_key_str = "%02x%02x%02x%02x" %(random_key[0],random_key[1],random_key[2],random_key[3])
version_raw = XOR(raw2[:16],map(ord,random_key_str))
print "���ܰ汾��Ϊ�������ܰ������ɼ��ַ�������16���ƽ��Ϊ׼����"
print "�汾�Ÿ�ʽ����Ϊ�� EN V3.60-6708"
print map(chr,version_raw)
print "��Ӧ��16���ƽ��Ϊ��"
print map(hex,version_raw)



