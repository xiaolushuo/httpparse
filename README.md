抓包
Parse and display http traffic from network device or pcap file. This is a go version of origin pcap-parser, thanks to gopacket project, this tool has simpler code base and is more efficient.

For origin python implementation, [refer to this branch](https://github.com/clearthesky/httpparse/tree/pcap-parser-python).

# install & requirement
Build httpparse requires libpcap-dev and cgo enabled.
## libpcap
for ubuntu/debian:

```sh
sudo apt install libpcap-dev
```

for centos/redhat/fedora:

```sh
sudo yum install libpcap-devel
```

for osx:

Libpcap and header files already installed.

## build

```sh
go get github.com/clearthesky/httpparse
```


# Usage
httpparse can read from pcap file, or capture data from network interfaces:

```
-device string
    Which network interface to capture. If any, capture all interface traffics (default "any")
-domain string
    Filter by request domain, suffix match
-file string
    Read from pcap file. If not specified, will capture from network devices
-filter string
    Filter by ip/port, format: [ip][:port], eg: 192.168.122.46:50792, 192.168.122.46, :50792
-force
    Force print unknown content-type http body even if it seems not to be text content
-level string
    Print level, url(only url) | header(http headers) | all(headers, and textuary http body) (default "header")
-output string
    Write result to file [output] instead of stdout
-pretty
    Try to format and prettify json content
-urlPath string
    Filter by request url path, contains match
```

## samples
A simple capture:

```
$ httpparse
192.168.110.48:56585  ----->  101.201.170.152:80
GET / HTTP/1.1
Host: geek.csdn.net
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
DNT: 1
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: uuid_tt_dd=-7445280944848876972_20160309; _JQCMT_ifcookie=1; _JQCMT_browser=8cc6c51a0610de98f19cf86af0855a3e; lzstat_uv=24444940273412920400|2839507@3117794@3311294


101.201.170.152:80  <-----  192.168.110.48:56585
HTTP/1.1 200 OK
Server: openresty
Date: Tue, 31 May 2016 02:40:14 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Keep-Alive: timeout=20
Vary: Accept-Encoding
Vary: Accept-Encoding
Content-Encoding: gzip

{body size: 15482 , set level arg to all to display body content}
```

More:

```sh
# parse pcap file
sudo tcpdump -wa.pcap tcp
httpparse -file a.pcap

# capture specified device:
httpparse -device eth0

# filter by ip and/or port
httpparse -filter :80  # filter by port
httpparse -filter 101.201.170.152 # filter by ip
httpparse -filter 101.201.170.152:80 # filter by ip and prot
```
