
import json
from datetime import date

from itemadapter import ItemAdapter
import mysql.connector


class ZameenhomePipeline:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self,spider):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='homes_db'
            )
            self.cursor = self.conn.cursor()
            check_query = """
                                SELECT home_url,date FROM `homes`

                            """
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        today_date = date.today()

        home_url = item.get('home_url', '')

        check_query = """
                    SELECT COUNT(*) FROM `homes`
                    WHERE `home_url` = %s AND `date` = %s
                """
        self.cursor.execute(check_query, (home_url, today_date))
        result = self.cursor.fetchone()

        if result[0] > 0:
            return item

        sql_statement = """
            INSERT INTO `homes`
            (`date`,`home_url`, `deal_type`, `is_titanium`, `is_trusted`, `is_verified`, `address`, `title`, `currency`, `house_type`, `price`, `price_in_rupees`, `area`, `purpose`, `location`, `bedrooms`, `bath`, `added`, `description`, `amenities`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        values = (
            today_date,
            item.get('home_url', ''),
            ' '.join(item.get('deal_type', [])) or '',
            item.get('is_titanium', 0),
            item.get('is_trusted', 0),
            item.get('is_verified', 0),
            item.get('address', ''),
            item.get('title', ''),
            item.get('currency', ''),
            item.get('house_type', ''),
            item.get('price', 0),
            item.get('price_in_rupees', 0),
            item.get('area', ''),
            item.get('purpose', ''),
            item.get('location', ''),
            item.get('bedrooms', 0),
            item.get('bath', 0),
            item.get('added', ''),
            ' '.join(item.get('description', [])) or '',
            json.dumps(item.get('amenities', {}))
        )

        self.cursor.execute(sql_statement, values)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()