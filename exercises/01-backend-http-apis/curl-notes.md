# EX-01-1 — HTTP/HTTPS & cURL Deep Dive

نتیجه کلی: **PASS** برای همه الزامات EX-01-1.

## منبع و دامنه

متن اصلی قبل از اجرای تست‌ها از [README اصلی](https://github.com/ekbatani/the-journey/blob/main/exercises/01-backend-http-apis/README.md) خوانده شد. نسخه دریافت‌شده در `evidence/original-README.md` است؛ این نسخه مربوط به main در زمان اجراست و به commit مشخص pin نشده است.

چهار الزام: اجرای curl -v روی endpoint عمومی؛ بررسی request line، TLS، هدرها و status line؛ ارسال Authorization و Content-Type سفارشی؛ ثبت مشاهدات در exercises/01-backend-http-apis/curl-notes.md.

فقط پوشه همین تمرین در workspace مستقل ساخته شد؛ هیچ پروژه موجودی ویرایش نشد و هیچ commit یا push انجام نشد. هیچ credential واقعی از حساب کاربر خوانده یا ارسال نشد. توکن ارسال‌شده صرفاً رشته ساختگی EX01-DUMMY-NOT-A-REAL-TOKEN است. امضاهای افزوده‌شده توسط زیرساخت در بدنه‌های echo با نشانگر REDACTED حذف شده‌اند؛ خطوط توصیف متغیرهای پراکسی هم از لاگ حذف شده‌اند. سایر شواهد درخواست و پاسخ حفظ شده‌اند.

## شرایط اجرا

زمان UTC ثبت نتایج: `2026-11-06T21:16:53.483651+00:00` (۷ نوامبر ۲۰۲۶ به وقت تهران).

نسخه ابزار: `curl 8.14.1 (x86_64-pc-linux-gnu) libcurl/8.14.1 OpenSSL/3.5.7 zlib/1.3.1 brotli/1.1.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.2 libssh2/1.11.1 nghttp2/1.64.0 nghttp3/1.8.0 librtmp/2.3 OpenLDAP/2.6.10`

HTTP/1.1 با --http1.1 انتخاب شد تا request/status line واضح باشد. --connect-timeout 10 و --max-time 35 زمان انتظار را محدود کردند؛ -q تنظیمات curlrc را غیرفعال کرد. از -k، credential واقعی، cookie یا دنبال‌کردن redirect استفاده نشد. گزینه‌های ثبت شواهد در اجرای واقعی: `-D <name>.headers -o <name>.body -w '%{json}'`؛ stderr در `<name>.verbose` و نتیجه در `<name>.result.json` ثبت شد.

## گزارش PASS / FAIL / NOT RUN

| مورد | وضعیت | شاهد واقعی |
|---|---|---|
| https-get | PASS | HTTP 200؛ exit=0؛ 5.714s؛ evidence/https-get.verbose |
| https-post | PASS | HTTP 200؛ exit=0؛ 5.710s؛ evidence/https-post.verbose |
| https-404 | PASS | HTTP 404؛ exit=0؛ 5.716s؛ evidence/https-404.verbose |
| http-get | PASS | HTTP 200؛ exit=0؛ 4.181s؛ evidence/http-get.verbose |
| هدرهای سفارشی و JSON | PASS | هدرهای Authorization و Content-Type و json در پاسخ POST تطابق کامل داشتند؛ بررسی ماشینی با assert گذشت. |
| بررسی request line، status line و TLS | PASS | خطوط واقعی در ادامه و فایل‌های verbose موجود است؛ SSL certificate verify ok و TLSv1.3 در هر سه HTTPS دیده شد. |
| تهیه یادداشت | PASS | همین فایل در مسیر خواسته‌شده ساخته شد. |
| اتصال مستقیم بدون پراکسی و گواهی اصلی origin | NOT RUN | خارج از الزام اصلی؛ محیط از پراکسی استفاده می‌کند و گواهی صادرشده توسط OpenAI دیده شد. |
| HTTP/2 و HTTP/3 | NOT RUN | خارج از دامنه این تمرین؛ HTTP/1.1 عمداً انتخاب شد. |

FAIL: هیچ موردی در تست‌های اجراشده وجود نداشت. NOT RUN به معنی اثبات‌نشدن آن حالت است، نه موفقیت یا شکست آن.

## مشاهدات و تفسیر

- در verbose، علامت `>` داده ارسالی، `<` داده دریافتی و `*` توضیح اتصال است.
- HTTPS ابتدا `CONNECT httpbin.org:443 HTTP/1.1` و پاسخ 200 پراکسی دارد؛ این پاسخ با پاسخ endpoint فرق دارد. بعد TLS handshake شامل Client hello، Server hello، Certificate و Finished دیده شد؛ سپس درخواست HTTP فرستاده شد.
- TLS مذاکره‌شده: `TLSv1.3 / TLS_AES_256_GCM_SHA384`. اعتبارسنجی محلی گواهی موفق بود و `ssl_verify_result=0` ثبت شد. صادرکننده گواهی `OpenAI, LLC` است؛ این محیط TLS را واسطه‌گری می‌کند و نمی‌توان از این آزمایش نتیجه گرفت اتصال TLS مستقیم تا سرور اصلی برقرار بوده است.
- HTTP معمولی بدون TLS handshake اجرا شد. به دلیل پراکسی، request target به شکل absolute URI یعنی `GET http://httpbin.org/get HTTP/1.1` دیده شد؛ HTTPS داخل tunnel از `/get` استفاده کرد. وضعیت 200 بدون redirect دریافت شد. در حالت HTTP، ssl_verify_result=0 به معنی امن‌بودن اتصال نیست؛ TLS اصلاً اجرا نشده است.
- `--data` روش POST را انتخاب کرد. Content-Type نوع بدنه ارسالی را مشخص می‌کند؛ Accept نوع پاسخ مطلوب را. Content-Length بدنه ارسالی 45 بایت بود. Bearer ساختگی صرفاً ارسال/echo هدر را آزمایش کرد و اثبات احراز هویت نیست.
- پاسخ GET و POST از نوع application/json بود. مسیر /status/404 وضعیت 404 با Content-Length: 0 داد. خالی‌بودن body در این مسیر طبیعی است.
- cURL بدون --fail برای HTTP 404 هم exit=0 می‌دهد: انتقال موفق بوده، ولی status برنامه 404 است. معیار این تست دریافت خود 404 بود.
- هدرهای Signature و Signature-Input در پاسخ echo توسط زیرساخت اضافه شدند، جزو هدرهای سفارشی ما نبودند و مقادیرشان در شواهد ذخیره‌شده حذف شده است.

## دستورها و شواهد واقعی

### https-get

```bash
curl -q -v --http1.1 --connect-timeout 10 --max-time 35 https://httpbin.org/get
```

نتیجه ثبت‌شده:

```json
{
  "name": "https-get",
  "command": "curl -q -v --http1.1 --connect-timeout 10 --max-time 35 https://httpbin.org/get",
  "exit_code": 0,
  "http_code": 200,
  "http_version": "1.1",
  "ssl_verify_result": 0,
  "time_total": 5.713951,
  "error": null
}
```

لاگ verbose اجرا (فقط خطوط توصیف متغیرهای پراکسی حذف شده‌اند):

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 127.0.0.1:44965...
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Establish HTTP proxy tunnel to httpbin.org:443
> CONNECT httpbin.org:443 HTTP/1.1
> Host: httpbin.org:443
> User-Agent: curl/8.14.1
> Proxy-Connection: Keep-Alive
> 

  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:05 --:--:--     0< HTTP/1.1 200 OK
< date: Fri, 06 Nov 2026 21:16:53 GMT
< 
* CONNECT phase completed
* CONNECT tunnel established, response 200
* ALPN: curl offers http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [1563 bytes data]
*  CAfile: /usr/local/share/ca-certificates/nebula-dns.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [1210 bytes data]
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
{ [1 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [21 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [1796 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [78 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519MLKEM768 / id-ecPublicKey
* ALPN: server accepted http/1.1
* Server certificate:
*  subject: CN=httpbin.org
*  start date: Nov  6 21:11:53 2026 GMT
*  expire date: Nov  7 21:16:53 2026 GMT
*  subjectAltName: host "httpbin.org" matched cert's "httpbin.org"
*  issuer: C=US; ST=California; L=San Francisco; O=OpenAI, LLC; CN=openai.com
*  SSL certificate verify ok.
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using sha256WithRSAEncryption
*   Certificate level 1: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* Connected to 127.0.0.1 (127.0.0.1) port 44965
* using HTTP/1.x
} [5 bytes data]
> GET /get HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.14.1
> Accept: */*
> 
* Request completely sent off
{ [5 bytes data]
< HTTP/1.1 200 OK
< access-control-allow-credentials: true
< access-control-allow-origin: *
< access-control-expose-headers: Retry-After, RateLimit, RateLimit-Policy
< content-length: 683
< content-type: application/json
< x-content-type-options: nosniff
< date: Fri, 06 Nov 2026 21:16:53 GMT
< x-envoy-upstream-service-time: 269
< server: envoy
< 
{ [683 bytes data]

100   683  100   683    0     0    119      0  0:00:05  0:00:05 --:--:--   144
100   683  100   683    0     0    119      0  0:00:05  0:00:05 --:--:--   183
* Connection #0 to host 127.0.0.1 left intact
```

بدنه پاسخ (امضاهای زیرساخت با REDACTED جایگزین شده‌اند):

```text
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "Signature": "[REDACTED: infrastructure-added signature]",
    "Signature-Agent": "\"https://chatgpt.com\"",
    "Signature-Input": "[REDACTED: infrastructure-added signature]",
    "User-Agent": "curl/8.14.1"
  },
  "method": "GET",
  "origin": "2a13:9500:1e4:13::57f:2",
  "url": "https://httpbin.org/get"
}
```

### https-post

```bash
curl -q -v --http1.1 --connect-timeout 10 --max-time 35 -H 'Authorization: Bearer EX01-DUMMY-NOT-A-REAL-TOKEN' -H 'Content-Type: application/json' --data '{"name":"Dummy Learner","exercise":"EX-01-1"}' https://httpbin.org/post
```

نتیجه ثبت‌شده:

```json
{
  "name": "https-post",
  "command": "curl -q -v --http1.1 --connect-timeout 10 --max-time 35 -H 'Authorization: Bearer EX01-DUMMY-NOT-A-REAL-TOKEN' -H 'Content-Type: application/json' --data '{\"name\":\"Dummy Learner\",\"exercise\":\"EX-01-1\"}' https://httpbin.org/post",
  "exit_code": 0,
  "http_code": 200,
  "http_version": "1.1",
  "ssl_verify_result": 0,
  "time_total": 5.709977,
  "error": null
}
```

لاگ verbose اجرا (فقط خطوط توصیف متغیرهای پراکسی حذف شده‌اند):

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 127.0.0.1:44965...
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Establish HTTP proxy tunnel to httpbin.org:443
> CONNECT httpbin.org:443 HTTP/1.1
> Host: httpbin.org:443
> User-Agent: curl/8.14.1
> Proxy-Connection: Keep-Alive
> 

  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:05 --:--:--     0< HTTP/1.1 200 OK
< date: Fri, 06 Nov 2026 21:16:53 GMT
< 
* CONNECT phase completed
* CONNECT tunnel established, response 200
* ALPN: curl offers http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [1563 bytes data]
*  CAfile: /usr/local/share/ca-certificates/nebula-dns.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [1210 bytes data]
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
{ [1 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [21 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [1796 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [79 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519MLKEM768 / id-ecPublicKey
* ALPN: server accepted http/1.1
* Server certificate:
*  subject: CN=httpbin.org
*  start date: Nov  6 21:11:53 2026 GMT
*  expire date: Nov  7 21:16:53 2026 GMT
*  subjectAltName: host "httpbin.org" matched cert's "httpbin.org"
*  issuer: C=US; ST=California; L=San Francisco; O=OpenAI, LLC; CN=openai.com
*  SSL certificate verify ok.
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using sha256WithRSAEncryption
*   Certificate level 1: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* Connected to 127.0.0.1 (127.0.0.1) port 44965
* using HTTP/1.x
} [5 bytes data]
> POST /post HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.14.1
> Accept: */*
> Authorization: Bearer EX01-DUMMY-NOT-A-REAL-TOKEN
> Content-Type: application/json
> Content-Length: 45
> 
} [45 bytes data]
* upload completely sent off: 45 bytes
{ [5 bytes data]
< HTTP/1.1 200 OK
< access-control-allow-credentials: true
< access-control-allow-origin: *
< access-control-expose-headers: Retry-After, RateLimit, RateLimit-Policy
< content-length: 982
< content-type: application/json
< x-content-type-options: nosniff
< date: Fri, 06 Nov 2026 21:16:53 GMT
< x-envoy-upstream-service-time: 263
< server: envoy
< 
{ [982 bytes data]

100  1027  100   982  100    45    171      7  0:00:06  0:00:05  0:00:01   218
100  1027  100   982  100    45    171      7  0:00:06  0:00:05  0:00:01   276
* Connection #0 to host 127.0.0.1 left intact
```

بدنه پاسخ (امضاهای زیرساخت با REDACTED جایگزین شده‌اند):

```text
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Authorization": "Bearer EX01-DUMMY-NOT-A-REAL-TOKEN",
    "Content-Length": "45",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "Signature": "[REDACTED: infrastructure-added signature]",
    "Signature-Agent": "\"https://chatgpt.com\"",
    "Signature-Input": "[REDACTED: infrastructure-added signature]",
    "User-Agent": "curl/8.14.1"
  },
  "method": "POST",
  "origin": "2a13:9500:1e4:13::1bd:12a",
  "url": "https://httpbin.org/post",
  "data": "{\"name\":\"Dummy Learner\",\"exercise\":\"EX-01-1\"}",
  "files": {},
  "form": {},
  "json": {
    "exercise": "EX-01-1",
    "name": "Dummy Learner"
  }
}
```

### https-404

```bash
curl -q -v --http1.1 --connect-timeout 10 --max-time 35 https://httpbin.org/status/404
```

نتیجه ثبت‌شده:

```json
{
  "name": "https-404",
  "command": "curl -q -v --http1.1 --connect-timeout 10 --max-time 35 https://httpbin.org/status/404",
  "exit_code": 0,
  "http_code": 404,
  "http_version": "1.1",
  "ssl_verify_result": 0,
  "time_total": 5.715993,
  "error": null
}
```

لاگ verbose اجرا (فقط خطوط توصیف متغیرهای پراکسی حذف شده‌اند):

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 127.0.0.1:44965...
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Establish HTTP proxy tunnel to httpbin.org:443
> CONNECT httpbin.org:443 HTTP/1.1
> Host: httpbin.org:443
> User-Agent: curl/8.14.1
> Proxy-Connection: Keep-Alive
> 

  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:05 --:--:--     0< HTTP/1.1 200 OK
< date: Fri, 06 Nov 2026 21:16:53 GMT
< 
* CONNECT phase completed
* CONNECT tunnel established, response 200
* ALPN: curl offers http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [1563 bytes data]
*  CAfile: /usr/local/share/ca-certificates/nebula-dns.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [1210 bytes data]
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
{ [1 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [21 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [1796 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [80 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519MLKEM768 / id-ecPublicKey
* ALPN: server accepted http/1.1
* Server certificate:
*  subject: CN=httpbin.org
*  start date: Nov  6 21:11:53 2026 GMT
*  expire date: Nov  7 21:16:53 2026 GMT
*  subjectAltName: host "httpbin.org" matched cert's "httpbin.org"
*  issuer: C=US; ST=California; L=San Francisco; O=OpenAI, LLC; CN=openai.com
*  SSL certificate verify ok.
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using sha256WithRSAEncryption
*   Certificate level 1: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* Connected to 127.0.0.1 (127.0.0.1) port 44965
* using HTTP/1.x
} [5 bytes data]
> GET /status/404 HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.14.1
> Accept: */*
> 
* Request completely sent off
{ [5 bytes data]
< HTTP/1.1 404 Not Found
< access-control-allow-credentials: true
< access-control-allow-origin: *
< access-control-expose-headers: Retry-After, RateLimit, RateLimit-Policy
< content-length: 0
< content-type: text/html; charset=utf-8
< x-content-type-options: nosniff
< date: Fri, 06 Nov 2026 21:16:53 GMT
< x-envoy-upstream-service-time: 269
< server: envoy
< 

  0     0    0     0    0     0      0      0 --:--:--  0:00:05 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:05 --:--:--     0
* Connection #0 to host 127.0.0.1 left intact
```

بدنه پاسخ (امضاهای زیرساخت با REDACTED جایگزین شده‌اند):

```text
[empty body; 0 bytes]
```

### http-get

```bash
curl -q -v --http1.1 --connect-timeout 10 --max-time 35 http://httpbin.org/get
```

نتیجه ثبت‌شده:

```json
{
  "name": "http-get",
  "command": "curl -q -v --http1.1 --connect-timeout 10 --max-time 35 http://httpbin.org/get",
  "exit_code": 0,
  "http_code": 200,
  "http_version": "1.1",
  "ssl_verify_result": 0,
  "time_total": 4.181349,
  "error": null
}
```

لاگ verbose اجرا (فقط خطوط توصیف متغیرهای پراکسی حذف شده‌اند):

```text
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 127.0.0.1:44965...
* Connected to 127.0.0.1 (127.0.0.1) port 44965
* using HTTP/1.x
> GET http://httpbin.org/get HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.14.1
> Accept: */*
> Proxy-Connection: Keep-Alive
> 
* Request completely sent off

  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0< HTTP/1.1 200 OK
< access-control-allow-credentials: true
< access-control-allow-origin: *
< access-control-expose-headers: Retry-After, RateLimit, RateLimit-Policy
< content-length: 684
< content-type: application/json
< x-content-type-options: nosniff
< date: Fri, 06 Nov 2026 21:16:51 GMT
< x-envoy-upstream-service-time: 171
< server: envoy
< 
{ [684 bytes data]

100   684  100   684    0     0    163      0  0:00:04  0:00:04 --:--:--   163
* Connection #0 to host 127.0.0.1 left intact
```

بدنه پاسخ (امضاهای زیرساخت با REDACTED جایگزین شده‌اند):

```text
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "Signature": "[REDACTED: infrastructure-added signature]",
    "Signature-Agent": "\"https://chatgpt.com\"",
    "Signature-Input": "[REDACTED: infrastructure-added signature]",
    "User-Agent": "curl/8.14.1"
  },
  "method": "GET",
  "origin": "2a13:9500:1e4:13::1bd:12a",
  "url": "http://httpbin.org/get"
}
```

## اصالت نسخه ذخیره‌شده الزامات

SHA-256 فایل original-README.md: `0cd8db6ef4fae70d5b2d70267964fb6bb13d6aa69268838642c9da0fc1881111`
