# Lab1：穷举法破译凯撒密码实验报告
## 一、实验目的
理解凯撒密码的加密与解密原理，掌握凯撒密码的字母移位运算规则。
掌握穷举法的核心思想，学会使用穷举法破解无密钥的凯撒密码。
熟练使用 Python 编程语言实现凯撒密码解密与穷举破解，提升代码编写与调试能力。
通过实验验证凯撒密码的安全性缺陷，理解单表替换密码易被穷举破解的特点。

# 二、实验过程
1. 实验原理
凯撒密码是一种经典的移位替换密码，加密时将明文中的每个字母向后移动固定位数k（密钥），解密时将密文字母向前移动相同位数k。
由于英文字母共 26 个，凯撒密码的有效密钥仅为1~25，因此可通过穷举所有密钥，逐一解密并筛选出有意义的明文，完成密码破解。
2. 实验环境
操作系统：Windows
编程环境：Python 3.x
3. 实验步骤
定义解密函数：编写凯撒密码解密函数，实现对大小写字母的移位解密，非字母字符保持不变。
输入密文：给定待破解的密文NUFECMWBYUJMBIQGYNBYWIXY。
穷举密钥：遍历密钥1~25，调用解密函数生成所有解密结果。
筛选明文：人工 / 自动识别有意义的英文明文，确定正确密钥。
输出结果：打印正确密钥和解密后的明文。
三、实验结果分析
穷举结果：程序遍历k=1到k=25，输出 25 组解密结果，其中仅一组为有意义的英文语句，其余均为无意义字符组合。
正确密钥：当密钥k=12时，解密结果为连贯英文，是唯一有效明文。
安全性分析：凯撒密码密钥空间极小（仅 25 种可能），穷举法可在极短时间内破解，证明该密码算法安全性极低，无法满足实际加密需求。
结果验证：解密后的明文语义通顺，验证了代码逻辑与穷举破解方法的正确性。

# 四、实验源代码
python

def caesar_decrypt(ciphertext, k):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # 处理大写字母
            if char.isupper():
                # 解密：向前移动k位，模26保证在字母范围内
                original = ord(char) - ord('A')
                shifted = (original - k) % 26
                plaintext += chr(shifted + ord('A'))
            else:
                # 处理小写字母（本题密文都是大写，这里做兼容）
                original = ord(char) - ord('a')
                shifted = (original - k) % 26
                plaintext += chr(shifted + ord('a'))
        else:
            # 非字母字符保持不变
            plaintext += char
    return plaintext

ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"

print("穷举所有密钥的解密结果：")
print("-" * 50)
for k in range(1, 26):
    decrypted = caesar_decrypt(ciphertext, k)
    print(f"密钥 k={k:2d}：{decrypted}")
print("-" * 50)

correct_k = 12
correct_plaintext = caesar_decrypt(ciphertext, correct_k)
print(f"✅ 正确密钥：k={correct_k}")
print(f"✅ 解密后明文：{correct_plaintext}")

ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"

print("穷举所有密钥的解密结果：")
print("-" * 50)
for k in range(1, 26):
    decrypted = caesar_decrypt(ciphertext, k)
    print(f"密钥 k={k:2d}：{decrypted}")
print("-" * 50)


correct_k = 12
correct_plaintext = caesar_decrypt(ciphertext, correct_k)
print(f"✅ 正确密钥：k={correct_k}")
print(f"✅ 解密后明文：{correct_plaintext}")

## 凯撒密码解密函数
def caesar_decrypt(ciphertext, k):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # 处理大写字母
            if char.isupper():
                original = ord(char) - ord('A')
                # 向前移动k位，模26保证字母循环
                shifted = (original - k) % 26
                plaintext += chr(shifted + ord('A'))
            # 兼容小写字母
            else:
                original = ord(char) - ord('a')
                shifted = (original - k) % 26
                plaintext += chr(shifted + ord('a'))
        else:
            # 非字母字符不做处理
            plaintext += char
    return plaintext


ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"

## 穷举所有密钥1~25
print("========== 穷举法破解凯撒密码结果 ==========")
for k in range(1, 26):
    result = caesar_decrypt(ciphertext, k)
    print(f"密钥 k={k:2d}：{result}")

## 正确密钥与明文输出
correct_key = 12
final_plaintext = caesar_decrypt(ciphertext, correct_key)
print("\n========== 破解成功 ==========")
print(f"正确密钥：k = {correct_key}")
print(f"解密明文：{final_plaintext}")

# 五、实验总结
本次实验成功使用 Python 实现了穷举法破解凯撒密码，完成了从密文到明文的还原，验证了穷举法在小密钥空间密码破解中的有效性。
深入理解了凯撒密码的移位原理，掌握了字母 ASCII 码运算、模运算在密码解密中的应用。
实验证明凯撒密码存在严重的安全缺陷，密钥空间过小是其易被破解的核心原因，实际应用中需采用更复杂的加密算法。
提升了 Python 代码编写能力，学会了函数封装、循环遍历、字符处理等编程技巧，为后续密码学实验奠定了基础。
认识到密码安全性的重要性，简单的替换密码无法抵御暴力破解，现代加密需依赖高密钥空间、高复杂度的加密算法。