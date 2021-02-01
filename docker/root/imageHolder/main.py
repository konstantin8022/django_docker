import os, json
from bottle import route,response, request, static_file, run

@route('/')
def root():
    return "Hello Bottle From Vasya" 

@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        response.status = 400 
        return "File extension not allowed."

    save_path = "/tmp/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    try: 
        upload.save(file_path)
    except:
        response.status = 200 
        response.content_type = "application/json"
        return json.dumps({"file": save_path})
    response.status = 200 
    response.content_type = "application/json"
    return json.dumps({"file": save_path})

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000)
