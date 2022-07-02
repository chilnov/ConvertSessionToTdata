# ConvertSessionToTdata

Tool convert session chưa set pass2fa sang tdata, sau đó set avatar, set pass2fa, set username và xuất file info, chưa số điện thoại,username,pass2fa


## Yêu cầu:
- Cài đặt python3
- Cài đặt các thư viện python: opentele, anyascii, python-socks[asyncio]
```
pip install opentele, anyascii, python-socks[asyncio]
```

- Nếu muốn build file exe thì cài thêm: pyinstaller, sau đó chạy lệnh trong file build.bat
```
pip install pyinstaller
```
### Lưu ý:
  Avatar lấy từ thư mục images, nên để kích thước ảnh to to 1 xíu, nhỏ quá sẽ lỗi :>
  
## Cách chạy
- Nếu chạy từ python: ```python path\to\file\session mode pass2fa hint [proxy-ip] [proxy-port]```
- Nếu chạy từ exe: ```ConvertSessionToTdata.exe path\to\file\session mode pass2fa hint [proxy-ip] [proxy-port]```

### Ví dụ:
  ```python session\+84392057868\+84392057868.session 1 12345 1234```  
  
  Nếu cần proxy thì thêm vào, nếu không cần thì bỏ qua. Chạy tương tự với bản exe
 
Trong đó: mode 0 là ```UseCurrentSession```, mode 1 là ```CreateNewSession```. Không khuyến khích dùng mode 0
