from config import app
import views

if __name__ == '__main__':
	# Debug mode
	# app.run(port=8080, debug=True)
	# Production
	app.run(debug=False)
