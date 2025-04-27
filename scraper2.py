import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_all_drug_ingredients(drug_name):
    """
    Search for a drug and return all commercial drug names with their active ingredients.

    Args:
        drug_name (str): The name to search for

    Returns:
        list of tuples: [(commercial_name, active_ingredient), ...]
    """
    url = "http://www.drugeye.pharorg.com/drugeyeapp/android-search/drugeye-android-live-go.aspx"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url)
        time.sleep(3)

        search_input = driver.find_element(By.ID, "ttt")
        search_input.send_keys(drug_name)
        search_button = driver.find_element(By.ID, "b1")
        search_button.click()
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find("table", {"id": "MyTable"})
        if not table:
            return []

        rows = table.find_all("tr")
        results = []

        for i in range(0, len(rows), 6):
            try:
                commercial_name = rows[i].find("td").text.strip()
                active_ingredient = rows[i + 1].find("td").text.strip()
                results.append((commercial_name, active_ingredient))
            except:
                continue

        return results

    finally:
        driver.quit()


# Example usage
if __name__ == "__main__":
    drug_name = input("Enter drug name: ")
    info = get_all_drug_ingredients(drug_name)

    if info:
        print(f"\nAll results for '{drug_name}':\n")
        for i, (name, ingredient) in enumerate(info, 1):
            print(f"{i}. 📦 {name} ➜ 🧪 {ingredient}")
    else:
        print("❌ No results found.")
