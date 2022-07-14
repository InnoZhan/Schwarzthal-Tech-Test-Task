import pymongo
from parser import Parser

myclient = pymongo.MongoClient("localhost:2717")
mydb = myclient["data"]
mycol = mydb["companies"]

if __name__ == "__main__":
    parser = Parser()
    cvrs = parser.get_cvrs(1000)
    for cvr in cvrs:
        jsondata = parser.get_company_info_by_cvr(cvr)
        mycol.insert_one(jsondata)
    driver.close()
    driver.quit()

myclient.close()

