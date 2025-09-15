import urllib.request
import xml.etree.ElementTree as ET
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AWS アップデート探索")

@mcp.tool()
def search_aws_updates(keyword: str) -> List[Dict[str, str]]:
    """
    AWSのアップデート情報を検索する関数。

    Args:
        keyword (str): 検索キーワード。

    Returns:
        List[Dict[str, str]]: 検索結果のリスト。各結果は辞書形式で、'title'と'link'を含む。
    """

    aws_new_feed = "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
    with urllib.request.urlopen(aws_new_feed) as response:
        feed_data = ET.fromstring(response.read())

    results = []

    for item in feed_data.findall('.//item'):
        title = getattr(item.find('title'), 'text', '') or ''
        discription = getattr(item.find('description'), 'text', '') or ''
        date = getattr(item.find('pubDate'), 'text', '') or ''

        if keyword.lower() in title.lower() or keyword.lower() in discription.lower():
            link = getattr(item.find('link'), 'text', '') or ''
            results.append({
                'title': title,
                'description': discription[:200] + '...' if len(discription) > 200 else discription,
                'link': link,
                'date': date
            })

            # 最大5件までに制限
            if len(results) >= 5:
                break

    return results

mcp.run()
