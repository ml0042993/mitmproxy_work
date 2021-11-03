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
    url = "http://yjpf.gsosc.cn/prod-api/app/bzCeShi/loadCsTiByDtId"
    exam_url = "http://yjpf.gsosc.cn/prod-api/app/bzCeShi/loadCsTiByDtId"
    wechat_url = 'https://shanxi.guangyusoft.com:12721/ShanXi3-3-5k/examsystem_getExamSystemQuestionById.action?uid='
    # if exam_url in flow.request.url:
    if exam_url in flow.request.url:
        mian(flow)
    elif url in flow.request.url:
        mian(flow)
    elif wechat_url in flow.request.url:
        wechat(flow)
def mian(flow):
    print(flow.response.text)
    results = json.loads(flow.response.text)
    datas: list = results.get("data")
    with open("info.txt", 'w', encoding='utf8') as f:
        file = []
        for data in datas:
            quetions = {}
            options = []
            quetions['title'] = data.get("timu")
            quetions['analyze'] = data.get("jieXi").replace("<br>", "")

            for option in data.get("options"):
                # quetions["options"] = option.get("options")
                options.append(option.get("bianHao") + ":" + option.get("options"))
            quetions["options"] = options
            # print(str(quetions))
            # tap :dict = quetions
            file.append(quetions)
        f.write(json.dumps(file, ensure_ascii=False))
def wechat(flow):
    print(flow.response.text)
    dict_responses = json.loads(flow.response.text)
    dict_response = dict_responses.get('question')

    que_info = {}
    que_info['title'] = dict_response.get('content')
    que_info['answer'] = dict_response.get('answer')
    que_info['option'] = []
    if dict_response.get('optionOne'):
        que_info['option'].append("A." + dict_response.get('optionOne'))
    if dict_response.get('optionTwo'):
        que_info['option'].append('B.' + dict_response.get('optionTwo'))
    if dict_response.get('optionThree'):
        que_info['option'].append('C.' + dict_response.get('optionThree'))
    if dict_response.get('optionFour'):
        que_info['option'].append('D.' + dict_response.get('optionFour'))
    if dict_response.get('optionFive'):
        que_info['option'].append('E.' + dict_response.get('optionFive'))
    if dict_response.get('optionSix'):
        que_info['option'].append('F.' + dict_response.get('optionSix'))
    if dict_response.get('optionSeven'):
        que_info['option'].append('G.' + dict_response.get('optionSeven'))
    if dict_response.get('optionEight'):
        que_info['option'].append('H.' + dict_response.get('optionEight'))
    if dict_response.get('optionNine'):
        que_info['option'].append('I.' + dict_response.get('optionNine'))

    print(que_info)
    with open('we_info.txt', 'w', encoding='utf8') as f:
        f.write(json.dumps(que_info, ensure_ascii=False))
