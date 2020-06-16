'''Write a function that when given a URL as a string, parses out just
the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"'''


def domainName(url):
    if url.find('//') != -1:
        url = url[url.find('//')+2:]
    if url.find('www') != -1:
        url = url[url.find('.')+1:]

    return url[:url.find('.')]


if __name__ == '__main__':
    url = "http://github.com/carbonfive/raygun"
    if domainName(url) == 'github':
        print 'PASS'
    else:
        print 'FAIL'
