from flask import Flask
app = Flask(_name_)

@app.route('/')
def index():
  return 'hello, world'

if __name__ == "__web__":
    app.run(host='0.0.0.0')
