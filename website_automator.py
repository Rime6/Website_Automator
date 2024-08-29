import sys
import webbrowser

URLS = {
    "work": ["https://mail.google.com/mail/u/0/#inbox", "https://docs.google.com/document/u/0/"],
    "personal": ["https://docs.google.com/document/u/1/", "https://www.youtube.com"]
}

def open_webpages(urls):
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
    for url in urls:
        webbrowser.get(edge_path).open_new_tab(url)

if __name__ == "__main__":
    print("Usage: python script.py <set_name>")
    print("Available sets:")
    for set_name in URLS.keys():
        print(f"- {set_name}")
    input_user = input("Please enter the set you would like: ")
    if input_user.lower() == "work":
        open_webpages(URLS["work"])
    if input_user.lower() == "personal":
        open_webpages(URLS["personal"])
    else:
        while input_user != "personal" or "work":
            printing = print("That is not an available set")
            print(printing)
            input_user = input("Please enter the set you would like: ")
            if input_user.lower() == "work":
                open_webpages(URLS["work"])
                break
            if input_user.lower() == "personal":
                open_webpages(URLS["personal"])
                break
            else:
                continue


        sys.exit(1)