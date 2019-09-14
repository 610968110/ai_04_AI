import pandas as pd


def run():
    books = pd.read_csv("./books.csv")
    # print(books.columns)
    # print(books.info())

    # 取当前列不为Nan的
    # books = books[pd.notnull(books["original_publication_year"])]
    # g = books.groupby(by="original_publication_year").count()["title"]
    # print(g)

    # b = books.groupby(by="ratings_count").count().sort_values(by="ratings_count", ascending=False)[
    #         "title"][:10]
    b = books.groupby(by="title").count().sort_values(by="ratings_count", ascending=False)[
            "ratings_count"][:10]
    print(b)


if __name__ == '__main__':
    run()
