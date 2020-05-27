# 医院处方点评系统

状态：开发完善中

首页：展示已点评的处方简要信息，以医生原始诊断为超链接，点击可以进入处方点评详细信息

处方点评：增加处方点评记录

登录：
- 以手机号码登录
- 用户名密码错误提示
- 登录成功后跳转到首页，浏览已点评记录信息

注册： 
- 首次注册需要提供：手机号码，用户名称，密码，重复密码
- 无手机验证码功能，后期添加上
- 两次输入密码校验
- 注册成功后跳转到登录页面

查询：
- 模糊查询功能，目前只做了基于诊断和点评内容的模糊查询。后期完善，加上基于日期，科室等条件的查询功能。
