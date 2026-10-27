import requests
from bs4 import BeautifulSoup
def main(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    html_table = None
    for table in soup.find_all("table"):
        if "x-coordinate" in table.get_text():
            html_table = table
            break
    if html_table is None:
        return False
    table_data = [[cell.get_text(strip=True) for cell in row.find_all(["th", "td"])] for row in table.find_all(['tr'])]
    #fill in the landscape with empty values
    max_x, max_y = 0, 0
    for i in range(1, len(table_data), 1):
        max_x = max(max_x, int(table_data[i][0]) )
        max_y = max(max_y, int(table_data[i][2]) )
    landscape = [[" " for x in range(max_x+1)] for y in range(max_y+1)]
    for i in range(1, len(table_data), 1):
        x, y = int(table_data[i][0]), max_y - int(table_data[i][2])
        landscape[y][x] = table_data[i][1]
    for i in range(1, len(landscape), 1):
        line = ''.join(landscape[i])
        print(line)
if __name__=="__main__":
    examples_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    main(examples_url)