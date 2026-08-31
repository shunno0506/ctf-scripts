from pwn import *

BINARY = "./password_cracking.out" #バイナリファイル名を書き換える

FAIL_KEYWORD = b"Wrong" # バイナリが「不正解」を示すときに出す文字列（実際の問題に合わせて書き換える）

for pin in range(10000):
    pin_str = f"{pin:04d}"
    
    p=process(BINARY)
    response = p.recvuntil(b":", timeout=3) #プロント部分を読み飛ばす
    p.sendline(pin_str.encode()) #PINを送信
    result = p.recvall(timeout=3) #結果を受信
    
    if FAIL_KEYWORD not in result:
        print(f"[+] Found correct PIN: {pin_str}")
        print(result.decode(errors="ignore"))
        p.close()
        break
    else:
        print(f"[-] Tried PIN: {pin_str} - Incorrect")
        p.close()