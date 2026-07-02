import urllib.request, urllib.parse, json, time

base='http://127.0.0.1:8000'

def request(path, method='GET', data=None, headers=None):
    req = urllib.request.Request(base + path, method=method, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read().decode()
        return r.status, body

print('GET / ->', request('/')[0])
print('GET /analytics/hits ->', request('/analytics/hits')[0])
print('GET /external/joke ->', request('/external/joke')[0])

form = urllib.parse.urlencode({'username':'user@example.com','password':'password'}).encode()
status, body = request('/token', 'POST', data=form, headers={'Content-Type':'application/x-www-form-urlencoded'})
print('POST /token ->', status)
token = json.loads(body)['access_token']
status, body = request('/users/me', 'GET', headers={'Authorization':'Bearer ' + token})
print('GET /users/me ->', status)
payload = {'email': f'test{int(time.time())}@example.com','full_name':'Test User','password':'password'}
data = json.dumps(payload).encode()
status, body = request('/register', 'POST', data=data, headers={'Content-Type':'application/json'})
print('POST /register ->', status)
