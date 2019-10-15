# 14/9/2019
# Gisele Tumutuyimana
# Hartwick bakery project
# cookies and candy sales for six months
cookies = []
candies = []


def cookies_input():
    for cookie in range(0, 6):
        cookie = int(input("Enter values for each month in a row for cookies :\n*"))
        cookies.append(cookie)
    print(cookies)


def candies_input():
    for candy in range(0, 6):
        candy = int(input("Enter values for each month in a row for candies :\n*"))
        candies.append(candy)
    print(candies)


def average_cookies():
    av_cookie = (cookies[0]+cookies[1]+cookies[2]+cookies[3]+cookies[4]+cookies[5])/6
    print("this is your average cookies!")
    print(av_cookie)


def average_candies():
    av_candies = (candies[0]+candies[1]+candies[2]+candies[3]+candies[4]+candies[5])/6
    print("this is your average candies")
    print(av_candies)


def av_co_pop():
    amount = (cookies[0]+cookies[1]+cookies[2]+cookies[3]+cookies[4]+cookies[5])/6
    return amount


def av_ca_pop():
    value = (candies[0]+candies[1]+candies[2]+candies[3]+candies[4]+candies[5])/6
    return value


def max_minimum_cookies():
    print("This is maximum number of cookies:\n", max(cookies))
    print("This is minimum number of cookies:\n", min(cookies))


def max_minimum_candies():
    print("This is maximum number of candies  :\n", max(candies))
    print("This is minimum number of candies: \n", min(candies))


def popular():
    if av_ca_pop() > av_co_pop():
        print("Candy is the more popular choice")
    elif av_co_pop() > av_ca_pop():
        print("Cookies are more popular")
    elif av_co_pop() == av_ca_pop():
        print("There is no popular choice")


# Now i will call the functions
cookies_input()
candies_input()
average_cookies()
average_candies()
max_minimum_candies()
max_minimum_cookies()
popular()
