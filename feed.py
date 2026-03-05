import yaml
import xml.etree.ElementTree as ET

with open('feed.yaml', 'r') as f:
    feed_data = yaml.safe_load(f)

    rss = ET.Element('rss', {
        'version':'2.0' ,
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    })

channel_element = ET.SubElement(rss, 'channel')
link_prefix = feed_data['link']
ET.SubElement(channel_element, 'title').text = feed_data['title']
ET.SubElement(channel_element, 'format').text = feed_data['format']
ET.SubElement(channel_element, 'subtitle').text = feed_data['subtitle']
ET.SubElement(channel_element, 'itunes:author').text = feed_data['author']
ET.SubElement(channel_element, 'description').text = feed_data['description']
ET.SubElement(channel_element, 'itunes:image', {'href': link_prefix + feed_data['image']})
ET.SubElement(channel_element, 'language').text = feed_data['language']
ET.SubElement(channel_element, 'link').text = link_prefix
ET.SubElement(channel_element, 'itunes:category', {'text': feed_data['category']})

for item in feed_data['item']:
    item_element = ET.SubElement(channel_element, 'item')
    ET.SubElement(item_element, 'title').text = item['title']
    ET.SubElement(item_element, 'description').text = item['description']
    ET.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': str(item['length'])
    })

output_tree = ET.ElementTree(rss)
output_tree.write('feed.xml', encoding='utf-8', xml_declaration=True)