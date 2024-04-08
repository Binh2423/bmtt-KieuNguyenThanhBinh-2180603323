from flask import Flask,request,jsonify 
from cipher.caesar.cipher_caesar import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json 
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_test = caesar_cipher.encrypt_text(plain_text,key)
    return jsonify({'encryted_message': encrypted_test})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json 
    plain_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(plain_text,key)
    return jsonify({'decryted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 8088, debug = True)