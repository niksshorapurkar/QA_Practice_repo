import requests

#base URL
base_url = "https://reqres.in/"


#GET Request
def get_request():
    url = base_url + "/api/users?page=2"
    response = requests.get(url)
    data = response.json()
    assert response.status_code == 200, "Code doesn't match"
    assert data["total"] == 12


#POST Request
def post_request():
    url_post = base_url + "/api/users"
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response_post = requests.post(url_post, data=payload)
    code = response_post.status_code
    assert code == 201
    response1 = response_post.json()
    print(response1["id"])
    assert response1["name"] == "morpheus", "name is invalid"


#PUT Request
def put_request():
    put_url = base_url +"/api/user/2"
    put_payload = {
    "name": "morpheus",
    "job": "zion resident"
    }

    response_put = requests.put(put_url, data=put_payload)
    code_put = response_put.status_code
    assert code_put == 200
    response2 = response_put.json()
    print(response2["job"])
    assert response2["job"] == "zion resident", "updated job is invalid"

#DELETE Request
def del_request():
    del_url = base_url + "/api/users/2"
    resp_del = requests.delete(del_url)
    assert resp_del.status_code == 204
    print(del_url)




get_request()
post_request()
put_request()
del_request()