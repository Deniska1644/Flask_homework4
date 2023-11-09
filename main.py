import argparse
import thread


if __name__ == '__main__':
    description = "1ым аргументом передайте каким образом начать скачивание\n 1 - многопоточно\n 2 - многопроцессорно\n 3 - асинхронно"
    parser = argparse.ArgumentParser(description="save images")
    parser.add_argument(f'url', type=str, nargs="+",
                        help=description)
    url_name = parser.parse_args()
    print(url_name.url[0])
    if url_name.url[0] == "1":
        thread.treads_(url_name.url)
    elif url_name.url[0] == "2":
        thread.proc(url_name.url)
    elif url_name.url[0] == "3":
        thread.main(url_name.url)
