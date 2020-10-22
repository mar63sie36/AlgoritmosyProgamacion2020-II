from flask import Flask, request, make_response, redirect
#Se crea un objeto de tipo app
app = Flask (__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    return f'¡Muchas gracias por visitarnos! tu ip es {user_ip} '
if __name__ == '__main__':
    app.run()
