from bottle import route, run, app, template,request
import bottle
import os

'''
@app.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root='./static')
'''
class UploadWebapp(object):
    def __init__(self):
        
         
        
        self.app =  bottle.Bottle()
        
        
    def set_routes(self):
        #self.bottle.route(self.base_path+'/', method="GET", callback=self.upload)
        self.app.route(path="/", method="GET", callback=self.index)
        self.app.route(path="/upload", method="GET", callback=self.get_upload)
        self.app.route(path="/upload", method="POST", callback=self.do_upload)


    def index(self):
        print("****************** index")
        return "Home page"

    def do_upload(self):
        #category   = request.forms.get('category')
        upload     = request.files.get('upload')
        name, ext = os.path.splitext(upload.filename)
        if ext not in ('.png','.jpg','.jpeg'):
            return 'File extension not allowed.'

        save_path = "/home/bere/cumucore/file/"
        upload.save(save_path) # appends upload.filename automatically
        return 'OK'
        
    def get_upload(self):
        return template("upload_form")

    def run_webapp(self):
        run(app=self.app, debug=True, reloader=True)

def main():
    webapp= UploadWebapp()
    webapp.set_routes()
    webapp.run_webapp()

if __name__==  '__main__':
    print("******************")
    main()
else:
   webapp= UploadWebapp()
   webapp.set_routes()
   app = application = webapp.app
 