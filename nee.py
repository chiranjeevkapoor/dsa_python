import requests
from bs4 import BeautifulSoup

def print_secret_message(url):
    """
    Fetches data from a published Google Doc containing character coordinates,
    parses the 2D grid, and prints the correctly oriented secret message.
    """
    try:
        # 1. Fetch the published Google Doc HTML content
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the document: {e}")
        return

    # 2. Parse HTML table data
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if not table:
        print("Error: No table found in the provided document URL.")
        return

    grid_data = {}
    max_x = 0
    max_y = 0

    # 3. Extract rows from the table (skipping the header row)
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            try:
                # Clean up any extra spaces or hidden characters in the text
                x_str = cols[0].get_text(strip=True)
                char = cols[1].get_text() # Preserve exact character spacing/spaces
                y_str = cols[2].get_text(strip=True)
                
                # Check for unexpected non-numeric headers repeated or bad rows
                if not (x_str.isdigit() and y_str.isdigit()):
                    continue
                    
                x = int(x_str)
                y = int(y_str)
                
                # Store character using coordinate tuple as key
                grid_data[(x, y)] = char
                
                # Update boundary sizes dynamically
                if x > max_x: max_x = x
                if y > max_y: max_y = y
            except (ValueError, IndexDimError):
                continue

    # 4. Render and print the grid
    # y decreases from top to bottom; x increases from left to right
    for y in range(max_y, -1, -1):
        row_chars = []
        for x in range(max_x + 1):
            # Fallback to a space character if the position is empty
            row_chars.append(grid_data.get((x, y), ' '))
        print("".join(row_chars))

# Example Usage:
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_secret_message(url)