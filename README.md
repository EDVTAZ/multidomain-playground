## Docker compose based environment to test various web based cross domain functionality easily and reproducibly.

Currently only one test/experiment is set up, which is checking the way cookies are set and are readable from domains and subdomains. The focus so far has been on creating an environment where it is easy to set up tests between different domains and subdomains. In the future I might add more tests.

To try it, run `docker compose up` and you can run the `cookies.py` file in the client container (`docker exec -it multidomain-playground-client-1 /bin/bash`) with:

```
root@08bdae2dabe6:/pwscripts# python cookies.py
Cookies after 1st page load:
[]
Cookies after fetch load:
[{'name': 'general', 'value': 'kenobi', 'domain': '.a.com', 'path': '/', 'expires': -1, 'httpOnly': False, 'secure': False, 'sameSite': 'Lax'}, {'name': 'hello', 'value': 'there', 'domain': 'a.com', 'path': '/', 'expires': -1, 'httpOnly': False, 'secure': False, 'sameSite': 'Lax'}]
Cookies from JS on a.com: general=kenobi; hello=there
Cookies from JS on sub1.a.com: general=kenobi
Cookies from JS on b.com:
```

---

The image setup for nginx and the flask is originally forked from: https://github.com/smallwat3r/docker-nginx-gunicorn-flask-letsencrypt
