from flask import Flask,request,jsonify 
from cipher.caesar.cipher_caesar import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher

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

vigenere_cipher = VigenereCipher()

@app.route("/api/vinegere/encrypt", methods=["POST"])
def vinegere_encrypt():
    data = request.json 
    plain_text = data['plain_text']
    key = data['key']
    encrypted_test = vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'encryted_message': encrypted_test})

@app.route("/api/vinegere/decrypt", methods=["POST"])
def vinegere_decrypt():
    data = request.json 
    plain_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(plain_text,key)
    return jsonify({'decryted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 8088, debug = True)