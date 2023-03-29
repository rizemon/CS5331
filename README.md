# CS5331

> A great place to start is the [Scenarios](#scenarios) section, followed by the [Demonstrating the exploits](#demonstrating-the-exploits) section.

- [CS5331](#cs5331)
  - [Network Setup](#network-setup)
  - [Scenarios](#scenarios)
    - [Bypassing access controls (`/protected`)](#bypassing-access-controls-protected)
    - [Forcing open-directs onto other users (`/redirected`)](#forcing-open-directs-onto-other-users-redirected)
    - [Forcing reflected XSS onto other users (`/reflected`)](#forcing-reflected-xss-onto-other-users-reflected)
    - [Stealing user's session cookies (`/captured`)](#stealing-users-session-cookies-captured)
  - [Relevant vulnerabilities](#relevant-vulnerabilities)
  - [Directory Layout](#directory-layout)
  - [Making Changes](#making-changes)
  - [PoC Scripts](#poc-scripts)
  - [Demonstrating the exploits](#demonstrating-the-exploits)
    - [Bypassing access controls](#bypassing-access-controls)
    - [Forcing open-directs onto other users](#forcing-open-directs-onto-other-users)
    - [Forcing reflected XSS onto other users](#forcing-reflected-xss-onto-other-users)
    - [Stealing user's session cookies](#stealing-users-session-cookies)


## Network Setup

```
[ browser ] <===> [ proxy (HAProxy) ] <===> [ backend (Gunicorn) ]
```

## Scenarios

### Bypassing access controls (`/protected`)

* **Background**: `backend` has a `/protected` page that is not meant to be accessible by the web browser as the `proxy` maps `/protected` to `/unauthorized`. This means that requesting for `/protected` via the `proxy` will result in getting the contents of `/unauthorized` from the `backend`.

* **Goal**: View the contents of `/protected` page.

### Forcing open-directs onto other users (`/redirected`)

* **Background**: `backend` has a `/redirected` page which has an `Open Redirect` vulnerability. It redirects the user based on the `Host` header of the request. This cannot be exploited for phishing-related acts on a victim as there is no way to override the `Host` header using normal means.

* **Goal**: Force a victim to be redirected to an arbitrary URL.

### Forcing reflected XSS onto other users (`/reflected`)

* **Background**: `backend` has a `/reflected` page which has an `Reflected XSS` vulnerability. It prints the contents of the `User-Agent` header of the request. This cannot be exploited to execute Javascript payloads on the victim as there is no way to override the `User-Agent` header using normal means.

* **Goal**: Force a victim to execute arbitrary Javascript code.

### Stealing user's session cookies (`/captured`)

* **Background**: `backend` has a `/captured` page that receives `content` from the body data of the request and stores it in an in-memory array, which can be viewed. 

* **Goal**: Force a victim's next request (containing a `FLAG` cookie) to be saved into the in-memory array.

## Relevant vulnerabilities
* Gunicorn (Apparently this was not assigned a CVE???): https://grenfeldt.dev/2021/04/01/gunicorn-20.0.4-request-smuggling/
* HAProxy CVE-2021-40346: https://nvd.nist.gov/vuln/detail/CVE-2021-40346

## Directory Layout

* `./backend/*`: Contains files to build the `backend` container
* `./proxy/*`: Contains files to build the `proxy` container
* `./poc/*`: Contains scripts to run attacks

## Making Changes

1) Make code changes
2) `docker-compose build`
3) `docker-compose up`
4) Repeat.

## PoC Scripts
* `poc1.py`: Exploits Gunicorn's vulnerability to poison the next user's request
    * `poc1_redirect.py`: Exploits Gunicorn's vulnerability to force the user to be redirected to `http://www.example.com`.
    * `poc1_xss.py`: Exploits Gunicorn's vulnerability to force the user's browser to execute `alert(document.domain)`.
    * `poc1_capture.py`: Exploits Gunicorn's vulnerability to capture the next user's request and store it into the server's in-memory array
* `poc2.py`: Exploits HAProxy's vulnerability to poison the next user's request

## Demonstrating the exploits

### Bypassing access controls

1) Execute `python3 poc1.py`.
2) **Within the next 5s**, browse to `http://localhost`.

### Forcing open-directs onto other users

1) Execute `python3 poc1_redirect.py`.
2) **Within the next 5s**, browse to `http://localhost`.

### Forcing reflected XSS onto other users

1) Execute `python3 poc1_xss.py`.
2) **Within the next 5s**, browse to `http://localhost`.

### Stealing user's session cookies

1) Execute `python3 poc1_capture.py`.
2) **Within the next 5s**, execute the following:
   ```bash
   curl http://localhost/ -H "Cookie: FLAG"
   ```
3) Browse to `http://localhost/captured`.