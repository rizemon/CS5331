FROM python:3.8

# Setup working directory
RUN git clone https://github.com/ickerwx/tcpproxy 
WORKDIR /tcpproxy

# Copy files
COPY encoder.py ./proxymodules/encoder.py

# Install dependencies
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "-u", "tcpproxy.py", "-li", "0.0.0.0", "-lp", "80", "-ti", "backend", "-tp", "80", "-om", "encoder"]