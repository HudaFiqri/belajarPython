'''
di __init__.py merupakan file yang bertugas untuk memberikan tanda agar python membaca file tersebut adalah sebuah module yang dimana dibeberapa bahasa program ini biasa disebuat framework atau library,
dan dengan __init__.py jadi semua file python yang berada di folder yang ditaruh dengan file __init__.py akan terbaca menjadi module yang dapat dipakkai secara global.

ditulis pada: 05-01-2024
'''

# import dari folder exising sesuai dengan nama file dan import semua class yang ada didalam file python tersebut
# .app nama file
# * mengimport semua class didalam folder
from .app_1 import *
from .app_2 import *