# yd_api
字典里使用"""
字符串''


注意
soted排序后会自动将中文转成ascii码，排序涉及到中文时，先将编码decode成unicode，sorted后再encode回utf8
json.dump(data, ensure_ascii=False)防止json格式自动转ascii