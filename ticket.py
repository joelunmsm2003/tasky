import requests

url ="http://xiencias.com:8000/add_tarea/"
params = {'username':'joel','password':123,'asunto':'Automatic Error','tipo':1,'descripcion':'Esto es un problema'}
r=requests.post(url,params=params)


print r.text


f = open('ticket.html','w')
f.write(r.text)
f.close()

