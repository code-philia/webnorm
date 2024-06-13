import sys 
sys.path.append("../")
from gptchecker import GPTChecker
import os
from dotenv import load_dotenv

# 加载 .env 文件
env_path = '../.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv('API_KEY')

logs1 = [
    "<logset1>2024-05-01 16:17:50.687 INFO   1 --- [http-nio-12340-exec-6] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 2 milliseconds, Result: Optional[User(userId=50d545f6-5735-4857-95b9-e09baf562ddc, username=liaoyifan, password=$2a$10$N8jaHcj1nNbgAcEG/cPo2eYyMyFUEEOH9Ct6krmXY2xO.n7W.tZau, roles=[ROLE_USER])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=liaoyifan, password=liaoyifan1998, verificationCode=1234)]Return: Response(status=1, msg=login success, data=TokenDto(userId=50d545f6-5735-4857-95b9-e09baf562ddc, username=liaoyifan, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsaWFveWlmYW4iLCJyb2xlcyI6WyJST0xFX1VTRVIiXSwiaWQiOiI1MGQ1NDVmNi01NzM1LTQ4NTctOTViOS1lMDliYWY1NjJkZGMiLCJpYXQiOjE3MTQ1NTE0NzAsImV4cCI6MTcxNDU1NTA3MH0.xAQ74dbyuSv5PB8GG3_lQa6eDXVtZPzh7mF4ZCriG7g))",
    "<logset2>2024-05-01 16:21:37.987 INFO   1 --- [http-nio-12340-exec-6] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 1 milliseconds, Result: Optional[User(userId=4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f, username=fdse_microservice, password=$2a$10$ZawaneSPvSqufjyvlE55HuJzT315CQz6pfreQcCmYnKTDIiimUc86, roles=[ROLE_USER])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=fdse_microservice, password=111111, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f, username=fdse_microservice, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTcxNDU1MTY5NywiZXhwIjoxNzE0NTU1Mjk3fQ.DWZCkfZal8dCUYgR7iwkbFYNiC3SyW91IG_P6Ykyujo))",
    "<logset3>2024-05-01 16:21:56.858 INFO   1 --- [http-nio-12340-exec-4] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 2 milliseconds, Result: Optional[User(userId=50d545f6-5735-4857-95b9-e09baf562ddc, username=liaoyifan, password=$2a$10$N8jaHcj1nNbgAcEG/cPo2eYyMyFUEEOH9Ct6krmXY2xO.n7W.tZau, roles=[ROLE_USER])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=liaoyifan, password=liaoyifan1998, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=50d545f6-5735-4857-95b9-e09baf562ddc, username=liaoyifan, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsaWFveWlmYW4iLCJyb2xlcyI6WyJST0xFX1VTRVIiXSwiaWQiOiI1MGQ1NDVmNi01NzM1LTQ4NTctOTViOS1lMDliYWY1NjJkZGMiLCJpYXQiOjE3MTQ1NTE3MTYsImV4cCI6MTcxNDU1NTMxNn0.O4OIvZEow7XJnmTIelpxdO1MwKlsriS8wVpk1aZ-AHA))",
    "<logset4>2024-05-01 16:22:19.796 INFO   1 --- [http-nio-12340-exec-7] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 2 milliseconds, Result: Optional[User(userId=50d545f6-5735-4857-95b9-e09baf562ddc, username=liaoyifan, password=$2a$10$N8jaHcj1nNbgAcEG/cPo2eYyMyFUEEOH9Ct6krmXY2xO.n7W.tZau, roles=[ROLE_USER])]  [http-nio-12340-exec-7] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=liaoyifan, password=liaoyifan1998, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=50d545f6-5735-4857-95b9-e09baf562ddc, username=liaoyifan, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsaWFveWlmYW4iLCJyb2xlcyI6WyJST0xFX1VTRVIiXSwiaWQiOiI1MGQ1NDVmNi01NzM1LTQ4NTctOTViOS1lMDliYWY1NjJkZGMiLCJpYXQiOjE3MTQ1NTE3MzksImV4cCI6MTcxNDU1NTMzOX0.T4rJJJRSaEbrzozRK_mutEWJIIBudxe-wvk6TcAyMkI))",
    "<logset5>2024-05-02 17:14:31.807 INFO   1 --- [http-nio-12340-exec-1] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 2 milliseconds, Result: Optional[User(userId=4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f, username=fdse_microservice, password=$2a$10$ZawaneSPvSqufjyvlE55HuJzT315CQz6pfreQcCmYnKTDIiimUc86, roles=[ROLE_USER])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=fdse_microservice, password=111111, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f, username=fdse_microservice, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTcxNDY0MTI3MSwiZXhwIjoxNzE0NjQ0ODcxfQ.Zx_X79xzn5CGXUEPzfb1zgTXKWaKlsWgS_cav-rsFpc))"
]

logs2 = [
    "<logset1>2024-05-13 20:03:01.291 INFO   1 --- [http-nio-12340-exec-6] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 1 milliseconds, Result: Optional[User(userId=c4f1da0b-b6c6-412c-944c-d1b4ddb153cf, username=admin, password=$2a$10$IFVY7.rXvwHsqs/pzdBImu86bc3lnBmlWk82Sa8nSEcw65jSkS1bC, roles=[ROLE_ADMIN])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=admin, password=222222, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=c4f1da0b-b6c6-412c-944c-d1b4ddb153cf, username=admin, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInJvbGVzIjpbIlJPTEVfQURNSU4iXSwiaWQiOiJjNGYxZGEwYi1iNmM2LTQxMmMtOTQ0Yy1kMWI0ZGRiMTUzY2YiLCJpYXQiOjE3MTU2MDE3ODEsImV4cCI6MTcxNTYwNTM4MX0.vIlh1nHYdeg-jprrNpQ3qYijhXpJZfvOYPcvJd3_5XA))",
    "<logset2>2024-05-13 20:04:33.513 INFO   1 --- [http-nio-12340-exec-2] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 2 milliseconds, Result: Optional[User(userId=631c5093-a6bd-4c62-ad77-d2239c3b9991, username=miniship, password=$2a$10$caa2QtTkAQ5.BGFPeihAFe4jnkY7kRCYX78ENLtOE.bhn8n0W38LG, roles=[ROLE_ADMIN])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=miniship, password=miniship, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=631c5093-a6bd-4c62-ad77-d2239c3b9991, username=miniship, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaW5pc2hpcCIsInJvbGVzIjpbIlJPTEVfQURNSU4iXSwiaWQiOiI2MzFjNTA5My1hNmJkLTRjNjItYWQ3Ny1kMjIzOWMzYjk5OTEiLCJpYXQiOjE3MTU2MDE4NzMsImV4cCI6MTcxNTYwNTQ3M30.IQHMJP6QGuJVuFqHLgCqDLI_owjcBzSSUQk3p-qLzh0))",
    "<logset3>2024-05-13 20:05:57.116 INFO   1 --- [http-nio-12340-exec-4] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 1 milliseconds, Result: Optional[User(userId=631c5093-a6bd-4c62-ad77-d2239c3b9991, username=miniship, password=$2a$10$caa2QtTkAQ5.BGFPeihAFe4jnkY7kRCYX78ENLtOE.bhn8n0W38LG, roles=[ROLE_ADMIN])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=miniship, password=miniship, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=631c5093-a6bd-4c62-ad77-d2239c3b9991, username=miniship, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaW5pc2hpcCIsInJvbGVzIjpbIlJPTEVfQURNSU4iXSwiaWQiOiI2MzFjNTA5My1hNmJkLTRjNjItYWQ3Ny1kMjIzOWMzYjk5OTEiLCJpYXQiOjE3MTU2MDE5NTcsImV4cCI6MTcxNTYwNTU1N30.Icxy1zWYt0MURX33ktaCJjDdkOz4mp-oWsJe4EVztF8))",
    "<logset4>2024-05-13 20:06:40.314 INFO   1 --- [http-nio-12340-exec-9] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 1 milliseconds, Result: Optional[User(userId=c4f1da0b-b6c6-412c-944c-d1b4ddb153cf, username=admin, password=$2a$10$IFVY7.rXvwHsqs/pzdBImu86bc3lnBmlWk82Sa8nSEcw65jSkS1bC, roles=[ROLE_ADMIN])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=admin, password=222222, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=c4f1da0b-b6c6-412c-944c-d1b4ddb153cf, username=admin, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInJvbGVzIjpbIlJPTEVfQURNSU4iXSwiaWQiOiJjNGYxZGEwYi1iNmM2LTQxMmMtOTQ0Yy1kMWI0ZGRiMTUzY2YiLCJpYXQiOjE3MTU2MDIwMDAsImV4cCI6MTcxNTYwNTYwMH0.5EDmkYWQLh66s7oH6LTb3PKt1m9rOJkLuWrzB4SXpYc))",
    "<logset5>2024-05-13 20:07:16.784 INFO   1 --- [http-nio-12340-exec-4] a.s.LoggingAspect: Execution of repository method: findByUsername, Execution Time: 1 milliseconds, Result: Optional[User(userId=631c5093-a6bd-4c62-ad77-d2239c3b9991, username=miniship, password=$2a$10$caa2QtTkAQ5.BGFPeihAFe4jnkY7kRCYX78ENLtOE.bhn8n0W38LG, roles=[ROLE_ADMIN])] a.s.LoggingAspect: Entering in Method: getToken, Class: auth.service.impl.TokenServiceImpl, Arguments: [BasicAuthDto(username=miniship, password=miniship, verificationCode=1234)], Return: Response(status=1, msg=login success, data=TokenDto(userId=631c5093-a6bd-4c62-ad77-d2239c3b9991, username=miniship, token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaW5pc2hpcCIsInJvbGVzIjpbIlJPTEVfQURNSU4iXSwiaWQiOiI2MzFjNTA5My1hNmJkLTRjNjItYWQ3Ny1kMjIzOWMzYjk5OTEiLCJpYXQiOjE3MTU2MDIwMzYsImV4cCI6MTcxNTYwNTYzNn0.GZ0WGb1rYyARgb4htu9D-8SWa5p74uvsyFn9qhBWSVo))"
]

parent_url= "/api/v1/users/login"

child_url1 = "/api/v1/orderOtherService/orderOther/query"

child_url2 = "/api/v1/adminorderservice/adminorder"

checker = GPTChecker(
    api_key=api_key,
    model="gpt-4o",
    max_tokens=2048,
    top_p=0.9,
    temperature=0.0
)

result = checker.check_flow_constraint(
    parent_url,
    child_url1,
    child_url2,
    logs1,
    logs2
)
print(result)
