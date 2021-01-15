import requests
from lxml import etree

def spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

    response = requests.get(url='https://movie.douban.com/subject/33447642/comments?sort=new_score&status=P', headers=headers)
    # response = requests.get(url='https://movie.douban.com/subject/33447642/', headers=headers)

    content = etree.HTML(response.text)

    print(f'dou_ban : {content}')
    results = content.xpath('//div[@class="comment-item "]')
    print(f'dou_ban_div : {results}')
    count = 0
    items = []
    for result in results:
        result_text = etree.tostring(result)
        # print(f'dou_ban_header : {result_text} , {type(result_text)}')
        content_info = result.xpath('div/h3/span[@class="comment-info"]')[0]
        star = content_info.xpath('span[2]/@title')[0]
        create_date = content_info.xpath('span[3]/text()')[0].replace(' ', '').split('\n')[1]
        content_info_texts = result.xpath('div/h3/span[@class="comment-info"]')
        print(f'dou_ban_content_info_text : {star} , {type(star)}')
        print(f'dou_ban_content_info_text : {create_date} , {type(create_date)}')

        short_content_text = result.xpath('div/p/span')
        short_content_count = len(short_content_text)
        if short_content_count == 1:
            short_content = short_content_text[0].xpath('text()')[0]
        else:
            short_content = ''.join(short_content_text[1].xpath('text()')[0].split('\n'))
        print(f'dou_ban_text : {short_content}')

        count += 1
        item = dict(
            star=star,
            create_date=create_date,
            short_content=short_content,
            count=count,
                    )
        items.append(item)
        # print(f'count : {count}')
    return items

