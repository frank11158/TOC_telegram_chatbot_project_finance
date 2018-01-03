# TOC Project 2017

Template Code for TOC Project 2017

A telegram bot based on a finite state machine

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8443
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "a"
		* Reply: "(In state1)
                  please enter stock code and duration
                  Ex: findstock,FB,2017-01-01,2017-05-01
                  (FB) for facebook,
                  (2017-01-01, 2017-05-01) for start date and end date"

	* Input: "b"
		* Reply: "(In state2)
                  please enter stock code
                  Ex: findcurrent,FB
                  (FB) for facebook"

	* Input: "c"
		* Reply: "(In state3)
                  please enter stock code
                  Ex: findoption,FB
                  (FB) for facebook"
* state1
	* Input: "findstock,FB,2017-01-01,2017-05-01"
		* Reply: stock price time series figure(png)


## Author
Frank-Chang
