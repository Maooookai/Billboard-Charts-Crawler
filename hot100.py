import time

from selenium import webdriver
import xlsxwriter

print("Billboard History Hot 100 Crawler")
print("Get Chart Data From Current Day in Each Year")
beginYear = input("Please input the year starts from(for example: 2000):")
endYear = input("Please input the year ends with(for example: 2020):")
currentDay = input("Please input the date of current Tuesday(for example: 08-31):")
baseAddress = "https://www.billboard.com/charts/hot-100/"
ad = {11, 22, 33, 44, 55, 66, 77, 88, 99}  # 广告
xls = xlsxwriter.Workbook(
    r'Billboard_Hot100_' + beginYear + '-' + currentDay + '_' + endYear + '-' + currentDay +
    '_Created_At_' + time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime()) + '.xlsx')
bold = xls.add_format({'bold': True})
for i in range(int(beginYear), int(endYear) + 1):
    thisWeek = 1
    sheet = xls.add_worksheet(str(i))
    sheet.write(0, 0, 'Billboard Hot 100 ' + str(i) + '-' + currentDay)
    sheet.write(1, 0, '歌曲名', bold)
    sheet.write(1, 1, '艺术家', bold)
    sheet.write(1, 2, '本周排名', bold)
    sheet.write(1, 3, '上周排名', bold)
    sheet.write(1, 4, '最高排名', bold)
    sheet.write(1, 5, '在榜周数', bold)
    address = baseAddress + str(i) + "-" + currentDay
    browser = webdriver.Chrome(r'chromedriver.exe')
    browser.get(address)
    chart = browser.find_element_by_class_name('chart-list__elements')
    for j in range(1, 110):
        if j not in ad:
            name = chart.find_element_by_xpath('//ol/li[' + str(j) + ']/button/span[2]/span[1]').text
            singer = chart.find_element_by_xpath('//ol/li[' + str(j) + ']/button/span[2]/span[2]').text
            lastWeek = chart.find_element_by_xpath('//ol/li[' + str(
                j) + "]/button/div[1]/div[@class='chart-element__meta text--center color--secondary text--last']").text
            peak = chart.find_element_by_xpath('//ol/li[' + str(
                j) + "]/button/div[1]/div[@class='chart-element__meta text--center color--secondary text--peak']").text
            weeksOnChart = chart.find_element_by_xpath('//ol/li[' + str(
                j) + "]/button/div[1]/div[@class='chart-element__meta text--center color--secondary text--week']").text
            sheet.write(thisWeek + 1, 0, name)
            sheet.write(thisWeek + 1, 1, singer)
            sheet.write(thisWeek + 1, 2, thisWeek)
            sheet.write(thisWeek + 1, 3, lastWeek)
            sheet.write(thisWeek + 1, 4, peak)
            sheet.write(thisWeek + 1, 5, weeksOnChart)
            thisWeek = thisWeek + 1
    browser.quit()
xls.close()
