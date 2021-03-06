# -*- coding: utf-8 -*-

import sys  # for open()
import binascii  # for binascii()

def bin2txt(r_path, w_path):
    with open(r_path, 'rb') as r_f:
        with open(w_path, 'w') as w_f:
            w_f.write("#ifndef __DATA_H__\r#define __DATA_H__\r\runsigned char argv[] = {\r")
            w_f.write("\t")
            counter = 0
            while 1:
                msg = r_f.read(1)
                if not msg:
                    w_f.write("\r};\r\r#endif\r")
                    r_f.close()
                    w_f.close()
                    return

                counter += 1
                if (counter == 1):
                    data_str = "0x" +  binascii.b2a_hex(msg).decode('utf-8')
                else:
                    data_str = ", 0x" + binascii.b2a_hex(msg).decode('utf-8')
                w_f.write(data_str)
                # 换行
                if (counter >= 8):
                    counter = 0;
                    w_f.write(",\r\t")

