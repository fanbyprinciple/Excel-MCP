import httpx

from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup

#initialise fastmcp
mcp = FastMCP(
    'Your MCP Tools',
    dependecies=['beautifulsoup4']

)

@mcp.tool(name='web_content_extractor',
          description='Extracts the content of a web page',
         )
def extract_web_content(url: str) -> str | None:
    """
    Extracts the content of a web page.
    :param url: The URL of the web page to extract content from.
    :return: The content of the web page, or None if an error occurred.
    """
    try:
        response = httpx.get(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            },
            timeout=10,
              follow_redirects=True,
          )  # Set a timeout for the request
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text().replace('\n', ' ').replace('\r', ' ').strip()
    except Exception as e:
        # Handle exceptions (e.g., network errors, parsing errors)      
        print(f"An error occurred while requesting {url}: {e}")
        return None
    
    if __name__ == '__main__':
        mcp.run(transport='stdio')
        