import sys
from flask import Flask, render_template, Response, request, render_template_string,url_for,redirect
users=[]
f = open('users_info.txt', 'r')
buf=[]
for line in f:
	buf.append(line)
f.close()
j=1
buf_user={}
cur_user_id=''
for i in buf:
	bb={1:'name',2:'login',3:'password',4:'status'}
	print(bb[j])
	buf_user[bb[j]]=i.replace("\n","")
	j+=1
	if j>4:
		users.append(buf_user)
		buf_user={}
		j=1
print(users)
def save_users():
	f = open('users_info.txt', 'w')
	for j in users:
		for i in j:
			f.write(j[i]+'\n')
	f.close()

#save_users(users)
app = Flask(__name__)
@app.route('/menu')
def menu():
	return render_template('base.html',_user=cur_user_id,_users_list=users)
@app.route('/')
def _main():
	print(123123)
	return render_template('index.html')
@app.route('/know')
def _know():
	print(123123)
	return render_template('know.html',_user=cur_user_id,_users_list=users)
@app.route('/regi', methods=['GET', 'POST'])
def _regi():
	if request.method == 'POST':
		name = request.form.get('name')
		username = request.form.get('login')
		password = request.form.get('password')
		same_check=False
		for i in users:
			if i['login']==username:
				print('error same nick',username)
				same_check=True
		if same_check==False:
			
			users.append({'name':name,'login':username,'password':password,'status':'USR'})
			save_users()
			return redirect(url_for('login'),301)
	

	# otherwise handle the GET request
	return render_template('regi.html')
@app.route('/login',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('login')
		password = request.form.get('password')
		users_check=True
		for i in users:
			if i['login']==username and i['password']==password:
				users_check=False
				#переход на след страницу
				global cur_user_id
				cur_user_id=users.index(i)
				cur_user_id=users.index(i)
				return redirect(url_for('menu'),301)
		if users_check==True:
			return render_template('login_error.html')
	

	# otherwise handle the GET request
	return render_template('login.html')
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
	# handle the POST request
	if request.method == 'POST':
		username = request.form.get('login')
		password = request.form.get('password')
		print(username,password)
		for i in users:
			if i['login']==username and i['password']==password:
				print(1)
				return '''
				<h1>The language value is: {}</h1>
				<h1>The framework value is: {}</h1>'''.format(username, password)


	# otherwise handle the GET request
	return render_template('index.html')

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

