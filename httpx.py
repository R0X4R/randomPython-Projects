#!/usr/bin/env python3
# Author: R0X4R (Eshan Singh)
import sys
import requests
from bs4 import BeautifulSoup as beauty
import re
import argparse

parser = argparse.ArgumentParser(description="HTTP Probing tool with some cool features.")
parser.add_argument('-l', '--list', help="Domains/IPs list.", default=False)

cmd = parser.parse_args()
try:
    if cmd.list:
        try:
            file = open(cmd.list, "r")
            url = file.readlines()
            file.close()
            for domain in url:
                try:
                    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
                    if ":80" in str(domain.strip()):
                        link = str('http://' + domain.strip())
                    elif ("https://" in str(domain.strip())) or ("http://" in str(domain.strip())):
                        link = str(domain.strip())
                    else:
                        link = str('https://' + domain.strip())
                    #print(link)
                    response = requests.get(link, headers=header, timeout=10, allow_redirects=False)
                    status_code = response.status_code
                    content_type = response.headers["Content-Type"]
                    content_length = response.headers["Content-Length"]
                    soup = beauty(response.content, 'html.parser')
                    title = soup.find('title')
                    try:
                        if int(status_code) <= 300:
                            print(link, "[\033[92m{}\033[0m]".format(int(status_code)), "[\033[93m{}\033[0m]".format(str(title.text.strip())), "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                        elif (int(status_code) == 301) or (int(status_code) == 302) or (int(status_code) == 307):
                            print(link, "[\033[36m{}\033[0m]".format(int(status_code)), "[\033[93m{}\033[0m]".format(str(title.text.strip())), "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                        else:
                            print(link, "[\033[91m{}\033[0m]".format(int(status_code)), "[\033[93m{}\033[0m]".format(str(title.text.strip())), "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                    except AttributeError:
                        if int(status_code) <= 300:
                            print(link, "[\033[92m{}\033[0m]".format(int(status_code)), "[]", "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                        elif (int(status_code) == 301) or (int(status_code) == 302) or (int(status_code) == 307):
                            print(link, "[\033[36m{}\033[0m]".format(int(status_code)), "[]", "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                        else:
                            print(link, "[\033[91m{}\033[0m]".format(int(status_code)), "[]", "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                except requests.Timeout:
                    pass
                except KeyboardInterrupt:
                    print("\nCTRL+C, pressed... Exiting")
                    sys.exit(0)
                except requests.ConnectionError:
                    pass
                except:
                    pass
        except FileNotFoundError:
            print("File doesn't exists. Please check once again")
            sys.exit(127)
    else:
        for domain in sys.stdin.readlines():
            try:
                header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
                if ":80" in str(domain.strip()):
                    link = str('http://' + domain.strip())
                elif ("https://" in str(domain.strip())) or ("http://" in str(domain.strip())):
                    link = str(domain.strip())
                else:
                    link = str('https://' + domain.strip())
                #print(link)
                response = requests.get(link, headers=header, timeout=10, allow_redirects=False)
                status_code = response.status_code
                content_type = response.headers["Content-Type"]
                content_length = response.headers["Content-Length"]
                soup = beauty(response.content, 'html.parser')
                title = soup.find('title')
                try:
                    if int(status_code) <= 300:
                        print(link, "[\033[92m{}\033[0m]".format(int(status_code)), "[\033[93m{}\033[0m]".format(str(title.text.strip())), "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                    elif (int(status_code) == 301) or (int(status_code) == 302) or (int(status_code) == 307):
                        print(link, "[\033[36m{}\033[0m]".format(int(status_code)), "[\033[93m{}\033[0m]".format(str(title.text.strip())), "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                    else:
                        print(link, "[\033[91m{}\033[0m]".format(int(status_code)), "[\033[93m{}\033[0m]".format(str(title.text.strip())), "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                except AttributeError:
                    if int(status_code) <= 300:
                        print(link, "[\033[92m{}\033[0m]".format(int(status_code)), "[]", "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                    elif (int(status_code) == 301) or (int(status_code) == 302) or (int(status_code) == 307):
                        print(link, "[\033[36m{}\033[0m]".format(int(status_code)), "[]", "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
                    else:
                        print(link, "[\033[91m{}\033[0m]".format(int(status_code)), "[]", "[\033[34m{}\033[0m]".format(str(content_type)), "[\033[35m{}\033[0m]".format(int(content_length)))
            except requests.Timeout:
                pass
            except KeyboardInterrupt:
                print("\nCTRL+C, pressed... Exiting")
                sys.exit(0)
            except requests.ConnectionError:
                pass
            except:
                pass
except KeyboardInterrupt:
                print("\nCTRL+C, pressed... Exiting")
                sys.exit(0)
