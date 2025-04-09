from flask import Flask, request, jsonify
import logging

from translator_funcs import translate_word

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')

    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(request.json, response)

    logging.info(f'Response:  {response!r}')

    return jsonify(response)


def handle_dialog(req, res):
    if req['session']['new']:
        res['response']['text'] = ('Привет! Введи запрос в формате «Переведите (переведи) слово: *слово*»,'
                                   ' чтобы я перевела твоё слово!')
        return
    req_for_check = req['request']['original_utterance'].lower().split()
    if req_for_check[0] == 'переведите' or req_for_check[0] == 'переведи':
        if req_for_check[1] == 'слово':
            res['response']['text'] = translate_word(req_for_check[2])
            return
    res['response']['text'] = ('Введи запрос в формате «Переведите (переведи) слово: *слово*»,'
                               ' чтобы я перевела твоё слово!')
    return


if __name__ == '__main__':
    app.run()
