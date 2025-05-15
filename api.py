import requests
from flask import Flask, request, jsonify

from apis.pc_apis import XHS_Apis

app = Flask(__name__)


class Data_Spider():
    def __init__(self):
        self.xhs_apis = XHS_Apis()


@app.route('/get_note_out_comment', methods=['POST'])
def get_note_out_comment():
    try:
        # 获取 POST 请求的参数
        data = request.json

        # 检查必要参数是否存在
        required_params = ['note_id', 'cursor', 'xsec_token', 'cookies_str']
        for param in required_params:
            if param not in data:
                return jsonify({'error': f'Missing required parameter: {param}'}), 400

        note_id = data['note_id']
        cursor = data['cursor']
        xsec_token = data['xsec_token']
        cookies_str = data['cookies_str']
        proxies = data.get('proxies', None)  # 可选参数

        try:
            data_spider = Data_Spider()

            print(cookies_str)
            print(proxies)
            print(xsec_token)
            print(note_id)
            success, msg, note_out_comment_list = data_spider.xhs_apis.get_note_all_out_comment(note_id=note_id,
                                                                                                xsec_token=xsec_token,
                                                                                                cookies_str=cookies_str,
                                                                                                proxies=proxies)

            print(note_out_comment_list)
            return jsonify({'msg': f'Internal server error: msg', 'data': note_out_comment_list}), 200

        except requests.exceptions.RequestException as e:
            return jsonify({'msg': f'Request failed: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'msg': f'Internal server error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004, debug=True)
