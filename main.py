import requests
import bs4
import re
import time


def get_url(url, limit):
    time.sleep(limit/100)
    # print(url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    regex = re.compile(r"^(/wiki/)((?!:).)*$")
    url_link = []
    for link in soup.find('div', {'id': 'bodyContent'}).find_all('a', href=regex):
        url_link.append('https://en.wikipedia.org' + link.attrs['href'])
    return url_link


def find(url1, url2, limit):
    print("Please wait! Searching!")
    url_list_1 = []
    url_list_2 = []
    url_list_3 = []
    url_list_4 = []
    url_list_5 = []
    url_list_6 = []
    url_visited = [url1]
    url_path = [url1, '', '', '', '', '', '']
    find = 0
    url_list_1.extend(get_url(url1, 1))
    for url_1 in url_list_1:
        if url_1 in url_visited:
            continue
        if url_1 == url2 or find == 1:
            find = 1
            break
        else:
            url_visited.append(url_1)
            url_path[1] = url_1
            url_list_2.extend(get_url(url_1, 1))
            for url_2 in url_list_2:
                if url_2 in url_visited:
                    continue
                if url_2 == url2 or find == 1:
                    find = 1
                    break
                else:
                    url_visited.append(url_2)
                    url_path[2] = url_2
                    url_list_3.extend(get_url(url_2, 1))
                    for url_3 in url_list_3:
                        if url_3 in url_visited:
                            continue
                        if url_3 == url2 or find == 1:
                            find = 1
                            break
                        else:
                            url_visited.append(url_3)
                            url_path[3] = url_3
                            url_list_4.extend(get_url(url_3, 1))
                            for url_4 in url_list_4:
                                if url_4 in url_visited:
                                    continue
                                if url_4 == url2 or find == 1:
                                    find = 1
                                    break
                                else:
                                    url_visited.append(url_4)
                                    url_path[4] = url_4
                                    url_list_5.extend(get_url(url_4, 1))
                                    for url_5 in url_list_5:
                                        if url_5 in url_visited:
                                            continue
                                        if url_5 == url2 or find == 1:
                                            find = 1
                                            break
                                        else:
                                            url_visited.append(url_5)
                                            url_path[5] = url_5
                                            url_list_6.extend(get_url(url_5, 1))
                                            for url_6 in url_list_6:
                                                if url_6 in url_visited:
                                                    continue
                                                else:
                                                    url_visited.append(url_6)
                                                if url_6 == url2 or find == 1:
                                                    find = 1
                                                    url_path[6] = url_6
                                                    break
        if url_path[6] != url2:
            del url_path[int(url_path.index(url2)):7]
    return url_path

'''
https://en.wikipedia.org/wiki/Six_degrees_of_separation
https://en.wikipedia.org/wiki/American_Broadcasting_Company
10
'''
if __name__ == "__main__":
    url1 = input()
    url2 = input()
    limit=input()
    url_list = []
    url_list.extend(find(url1, url2, limit))

    for i in range(0, len(url_list)):
        if i < len(url_list) - 1:
            print(url_list[i] + ' --> ', end='')
        else:
            print(url_list[i])
