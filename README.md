# flask-echo

JSON 데이터를 포함하는 POST 요청을 /echo 경로로 보내면 요청에 포함된 JSON 데이터를 응답에 포함해서 리턴합니다.

```
$ curl -X POST http://localhost/echo -H 'Content-Type: application/json' -d '{"key": "value"}'
{"key":"value"}
$
```