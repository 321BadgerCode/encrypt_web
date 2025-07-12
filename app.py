from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
cipher = Fernet(key)

@app.route('/', methods=["GET", "POST"])
def index():
	result = ''
	operation = ''
	if request.method == "POST":
		text = request.form.get("text", '')
		mode = request.form.get("mode")
		try:
			if mode == "encrypt":
				result = cipher.encrypt(text.encode()).decode()
				operation = "Encrypted"
			elif mode == "decrypt":
				result = cipher.decrypt(text.encode()).decode()
				operation = "Decrypted"
		except Exception as e:
			result = f"Error: {str(e)}"
	return render_template("index.html", result=result, operation=operation)

if __name__ == "__main__":
	app.run(debug=True)