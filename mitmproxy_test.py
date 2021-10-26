from mitmproxy import http
import json
# def request(flow):
#     url = "http://www.gsosc.cn/prod-api/app/dt/"
#     # if flow.request.method == "POST":
#     #     print("post")
#     if url in flow.request.url:
#         print(flow.request.pretty_url)

#         # print(flow.request.body)


#         # print(flow.request.get_text)
#         # print(flow.response.contents)
def response(flow) -> dict:
    url = "http://www.gsosc.cn/prod-api/app/dt/"
    exam_url = "http://www.gsosc.cn/prod-api/app/bzCeShi/loadCsTiByDtId"
    # if exam_url in flow.request.url:
    if exam_url in flow.request.url:
        print(flow.response.text)
        results = json.loads(flow.response.text)
        datas: list = results.get("data")
        with open("info.txt",'w',encoding='utf8') as f:
            file = []
            for data in datas:
                quetions = {}
                options = []
                quetions['title'] = data.get("timu")
                quetions['analyze'] = data.get("jieXi").replace("<br>", "")

                for option in data.get("options"):
                    # quetions["options"] = option.get("options")
                    options.append(option.get("bianHao")+":"+option.get("options"))
                quetions["options"] = options
                # print(str(quetions))
                # tap :dict = quetions
                file.append(quetions)
            f.write(json.dumps(file,ensure_ascii=False))
