# CS5331

## Network Setup

```
[ browser ] <===> [ proxy (HAProxy) ] <===> [ backend (Gunicorn) ]
```

* **Scenario**: `backend` has a `/protected` page that is not meant to be accessible by the web browser as the `proxy` maps `/protected` to `/unauthorized`. This means that requesting for `/protected` via the `proxy` will result in getting the contents of `/unauthorized` from the `backend`.
* **Goal**: Somehow view the `/protected` page, while having their request go through the `proxy`.

## Relevant vulnerabilities
* Gunicorn (Apparently this was not assigned a CVE???): https://grenfeldt.dev/2021/04/01/gunicorn-20.0.4-request-smuggling/
* HAProxy CVE-2021-40346: https://nvd.nist.gov/vuln/detail/CVE-2021-40346

## Directory Layout

* `./backend`: Contains files to build the `backend` container
* `./proxy`: Contains files to build the `proxy` container
* `./poc`: Contains scripts to run attacks

```
.
├── backend
│   ├── ...
├── proxy
│   ├── ...
├── poc
│   └── ...
├── docker-compose.yml
└── README.md
```

## Making Changes

1) Make code changes
2) `docker-compose build`
3) `docker-compose up`

## PoC list
* `poc1.py`: Exploits Gunicorn's vulnerability to poison the next user's request
* `poc2.py`: Exploits HAProxy's vulnerability to poison the next user's request

## Demonstrating the exploit

1) On terminal 1:
    ```bash
    $ curl http://127.0.0.1:80/protected
    Unauthorized page
    ```
2) On terminal 2:
    ```bash
    $ python3 poc/poc1.py OR python3 poc/poc2.py
    ...
    ```
2) On terminal 1:
    ```bash
    $ curl http://127.0.0.1:80/protected
    Protected page
    ```

## Todo:

- [ ] Embed a `Open Redirect` vulnerability in the `backend` code. The redirection URL must utilise the hostname found in the "Host" header.

- [ ] Embed a `Reflected XSS` vulnerability in the `backend` code. The redirection URL must utilise the value found in the "User-Agent" header.