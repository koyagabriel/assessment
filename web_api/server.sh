echo "Starting Flask Server"
export FLASK_APP=manage.py
export FLASK_ENV=development
flask run -h "0.0.0.0" -p 5000
