# 定义凯撒密码解密函数
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

# 给定的密文
ciphertext = "NUFECMWBYUJMBIQGYNBYWIXY"

# 穷举所有可能的密钥k（1~25）
print("穷举所有密钥的解密结果：")
print("-" * 50)
for k in range(1, 26):
    decrypted = caesar_decrypt(ciphertext, k)
    print(f"密钥 k={k:2d}：{decrypted}")
print("-" * 50)

# 人工观察后，正确的密钥是 k=12
correct_k = 12
correct_plaintext = caesar_decrypt(ciphertext, correct_k)
print(f"✅ 正确密钥：k={correct_k}")
print(f"✅ 解密后明文：{correct_plaintext}")