from flask import Flask
app = flask(_name_)

@app.route('/')
def index():
  return 'hello, world'
