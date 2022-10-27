import requests
import json


def get_data():
    cookies = {
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TOP_SERVICES': '2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '21606643800',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'searchType2': '3',
        '_ym_uid': '1600608225472446239',
        '_ym_d': '1665420454',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'ee26c13e-4987-4472-9dae-9f5ced87c9bf',
        'uxs_uid': '3f113550-48bb-11ed-8589-fbcf7188ea49',
        'flocktory-uuid': '5d750d26-4e19-47f0-9ce3-5fb1d4debd72-2',
        'afUserId': 'eeb438fc-fbd0-473c-9d71-ede77274f7b6-p',
        'MVID_CITY_ID': 'CityR_85',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_REGION_ID': '85',
        'MVID_REGION_SHOP': 'S978',
        'MVID_TIMEZONE_OFFSET': '5',
        'MVID_CITY_CHANGED': 'false',
        'MVID_KLADR_ID': '8900000600000',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'deviceType': 'desktop',
        '__ttl__widget__ui': '1665420558201-a6f8cfec7666',
        'cookie_ip_add': '178.155.5.10',
        'mindboxDeviceUUID': 'b527353f-0d32-40f2-b00a-358455d81de3',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22b527353f-0d32-40f2-b00a-358455d81de3%22%7D',
        '__lhash_': 'f03826010eff92d13a1697336cdb4d55',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'flacktory': 'no',
        '_gid': 'GA1.2.1784680921.1666894056',
        '_sp_ses.d61c': '*',
        '_ym_isad': '2',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '6d848cbead317fbc0046689c5245c81f',
        'tmr_lvidTS': '1600608225350',
        'advcake_track_id': '8d84d2af-7d40-e806-96e4-161b27d56186',
        'advcake_session_id': '15abd24e-d6b8-2e0e-061a-7504704b077b',
        'AF_SYNC': '1666894061515',
        'JSESSIONID': 'LrGqjhKJS655QWKRQTnGQw5TBmcL18Xv9wJ1Tx3yZBFsHpyGL3Dr!1180915958',
        'BIGipServeratg-ps-prod_tcp80': '1929698314.20480.0000',
        'bIPs': '2118529862',
        'MVID_GTM_BROWSER_THEME': '1',
        'BIGipServeratg-ps-prod_tcp80_clone': '1929698314.20480.0000',
        '__zzatgib-w-mvideo': 'MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UwRGglYEdeIkhaUGshC1E0NWYQSk9NRw03QF43V2EgDBYRTVZTeyUgFH5wI1gKDGE5Mzw0bXN4XCYKGlQ1XxlDak4NaTdsFzx1ZS8JMSxieTFSLxNLbD9HfDBILjQiDEJtNiRvL0tAZW9sKWIcOWMRXx9kQl9RLBkWKVQMLApYYxYfZ1IOZGRra1x2cU4JTV8aRg0kc08OLGdTCz5BezY0e0ptYTRWTgklIhJ8dChXcAxhQ0d1fC0+aSJiTVwRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyVJXVZ9KB4ReXEkS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0hKj/UA==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UwRGglYEdeIkhaUGshC1E0NWYQSk9NRw03QF43V2EgDBYRTVZTeyUgFH5wI1gKDGE5Mzw0bXN4XCYKGlQ1XxlDak4NaTdsFzx1ZS8JMSxieTFSLxNLbD9HfDBILjQiDEJtNiRvL0tAZW9sKWIcOWMRXx9kQl9RLBkWKVQMLApYYxYfZ1IOZGRra1x2cU4JTV8aRg0kc08OLGdTCz5BezY0e0ptYTRWTgklIhJ8dChXcAxhQ0d1fC0+aSJiTVwRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyVJXVZ9KB4ReXEkS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0hKj/UA==',
        'cfidsgib-w-mvideo': 'uzZGja7Upyi80wE9A/xEF+9uFtRKsh2AM4GSY7qHoroJxNFeFAQxEASCOTsaMs7J/hiKxJpq0uvVwBHNcCF41Kj6TB7Ms6xz2xhnED468QKaOPjERJjAmh8ii7BvZ/17UoNES2drfEmTNc9xl8aiiaFMVMUultlCcXni',
        'cfidsgib-w-mvideo': 'uzZGja7Upyi80wE9A/xEF+9uFtRKsh2AM4GSY7qHoroJxNFeFAQxEASCOTsaMs7J/hiKxJpq0uvVwBHNcCF41Kj6TB7Ms6xz2xhnED468QKaOPjERJjAmh8ii7BvZ/17UoNES2drfEmTNc9xl8aiiaFMVMUultlCcXni',
        'gsscgib-w-mvideo': 'X6oXdH6KwFZwSlkZkVqPzmI6dY3n7+Du6BgfVRsrCKoRk8eb30VqDqfnzzVac6DNvn6mPxQr+DvM4T+70MAxeNXkXWG9EesEYtO8i0fByb+B3Q96oVktPeYgmeiUHyB3/QaIlDXv+f9C6KBu5eKgFg9AY2w+hc+ukGR5/Isv3MUfKFupCE+g4lQ/Ej0rEKDiKtEYZ1IHRu8FM56WAgwCt/t93bIBUhEVM4ocvKolA+P8Mtdp9doYjS3vS5MTCA==',
        'gsscgib-w-mvideo': 'X6oXdH6KwFZwSlkZkVqPzmI6dY3n7+Du6BgfVRsrCKoRk8eb30VqDqfnzzVac6DNvn6mPxQr+DvM4T+70MAxeNXkXWG9EesEYtO8i0fByb+B3Q96oVktPeYgmeiUHyB3/QaIlDXv+f9C6KBu5eKgFg9AY2w+hc+ukGR5/Isv3MUfKFupCE+g4lQ/Ej0rEKDiKtEYZ1IHRu8FM56WAgwCt/t93bIBUhEVM4ocvKolA+P8Mtdp9doYjS3vS5MTCA==',
        'fgsscgib-w-mvideo': 'fRpQ4478f3d751b0687f99552f72e9449d235691',
        'fgsscgib-w-mvideo': 'fRpQ4478f3d751b0687f99552f72e9449d235691',
        'cfidsgib-w-mvideo': 'nRp0VRYWtINdwrQdgEEl2TWKe1wFdfcLKScyUzxM6Vx4e9f5pvy2RDFVWjKCDdNBvSU82fnwRi6+8IRPGk4xIBzZFb+TbFaPS2YqJeB3M31+i+oQzRs2eMjKV2MBh7WBAJGp/0QI0/cNF9W0imqpnlNdKPVM/PPzHXO+',
        'CACHE_INDICATOR': 'false',
        '_sp_id.d61c': 'bdfb95a0-c7e7-4610-9ab7-d5e437bbb0f0.1665420454.2.1666894356.1665420991.1009bcb2-3501-445e-8dd2-fb4bf65d7ec7.a9da1137-60dd-4684-987f-f908954ecbc1.32b66620-5a65-4b45-9be1-b14ed714b538.1666894055772.44',
        '_ga': 'GA1.2.1733869895.1665420454',
        'tmr_detect': '0%7C1666894361464',
        'tmr_reqNum': '449',
        'MVID_ENVCLOUD': 'prod1',
        '_ga_CFMZTSS5FM': 'GS1.1.1666894055.2.1.1666894396.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1666894055.2.1.1666894396.10.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=98c1bdf0557a410aa25b0a36ddee5438,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21606643800; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=3; _ym_uid=1600608225472446239; _ym_d=1665420454; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=ee26c13e-4987-4472-9dae-9f5ced87c9bf; uxs_uid=3f113550-48bb-11ed-8589-fbcf7188ea49; flocktory-uuid=5d750d26-4e19-47f0-9ce3-5fb1d4debd72-2; afUserId=eeb438fc-fbd0-473c-9d71-ede77274f7b6-p; MVID_CITY_ID=CityR_85; MVID_GEOLOCATION_NEEDED=false; MVID_REGION_ID=85; MVID_REGION_SHOP=S978; MVID_TIMEZONE_OFFSET=5; MVID_CITY_CHANGED=false; MVID_KLADR_ID=8900000600000; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; __ttl__widget__ui=1665420558201-a6f8cfec7666; cookie_ip_add=178.155.5.10; mindboxDeviceUUID=b527353f-0d32-40f2-b00a-358455d81de3; directCrm-session=%7B%22deviceGuid%22%3A%22b527353f-0d32-40f2-b00a-358455d81de3%22%7D; __lhash_=f03826010eff92d13a1697336cdb4d55; MVID_GLC=true; MVID_GLP=true; flacktory=no; _gid=GA1.2.1784680921.1666894056; _sp_ses.d61c=*; _ym_isad=2; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; SMSError=; authError=; tmr_lvid=6d848cbead317fbc0046689c5245c81f; tmr_lvidTS=1600608225350; advcake_track_id=8d84d2af-7d40-e806-96e4-161b27d56186; advcake_session_id=15abd24e-d6b8-2e0e-061a-7504704b077b; AF_SYNC=1666894061515; JSESSIONID=LrGqjhKJS655QWKRQTnGQw5TBmcL18Xv9wJ1Tx3yZBFsHpyGL3Dr!1180915958; BIGipServeratg-ps-prod_tcp80=1929698314.20480.0000; bIPs=2118529862; MVID_GTM_BROWSER_THEME=1; BIGipServeratg-ps-prod_tcp80_clone=1929698314.20480.0000; __zzatgib-w-mvideo=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UwRGglYEdeIkhaUGshC1E0NWYQSk9NRw03QF43V2EgDBYRTVZTeyUgFH5wI1gKDGE5Mzw0bXN4XCYKGlQ1XxlDak4NaTdsFzx1ZS8JMSxieTFSLxNLbD9HfDBILjQiDEJtNiRvL0tAZW9sKWIcOWMRXx9kQl9RLBkWKVQMLApYYxYfZ1IOZGRra1x2cU4JTV8aRg0kc08OLGdTCz5BezY0e0ptYTRWTgklIhJ8dChXcAxhQ0d1fC0+aSJiTVwRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyVJXVZ9KB4ReXEkS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0hKj/UA==; __zzatgib-w-mvideo=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UwRGglYEdeIkhaUGshC1E0NWYQSk9NRw03QF43V2EgDBYRTVZTeyUgFH5wI1gKDGE5Mzw0bXN4XCYKGlQ1XxlDak4NaTdsFzx1ZS8JMSxieTFSLxNLbD9HfDBILjQiDEJtNiRvL0tAZW9sKWIcOWMRXx9kQl9RLBkWKVQMLApYYxYfZ1IOZGRra1x2cU4JTV8aRg0kc08OLGdTCz5BezY0e0ptYTRWTgklIhJ8dChXcAxhQ0d1fC0+aSJiTVwRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyVJXVZ9KB4ReXEkS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0hKj/UA==; cfidsgib-w-mvideo=uzZGja7Upyi80wE9A/xEF+9uFtRKsh2AM4GSY7qHoroJxNFeFAQxEASCOTsaMs7J/hiKxJpq0uvVwBHNcCF41Kj6TB7Ms6xz2xhnED468QKaOPjERJjAmh8ii7BvZ/17UoNES2drfEmTNc9xl8aiiaFMVMUultlCcXni; cfidsgib-w-mvideo=uzZGja7Upyi80wE9A/xEF+9uFtRKsh2AM4GSY7qHoroJxNFeFAQxEASCOTsaMs7J/hiKxJpq0uvVwBHNcCF41Kj6TB7Ms6xz2xhnED468QKaOPjERJjAmh8ii7BvZ/17UoNES2drfEmTNc9xl8aiiaFMVMUultlCcXni; gsscgib-w-mvideo=X6oXdH6KwFZwSlkZkVqPzmI6dY3n7+Du6BgfVRsrCKoRk8eb30VqDqfnzzVac6DNvn6mPxQr+DvM4T+70MAxeNXkXWG9EesEYtO8i0fByb+B3Q96oVktPeYgmeiUHyB3/QaIlDXv+f9C6KBu5eKgFg9AY2w+hc+ukGR5/Isv3MUfKFupCE+g4lQ/Ej0rEKDiKtEYZ1IHRu8FM56WAgwCt/t93bIBUhEVM4ocvKolA+P8Mtdp9doYjS3vS5MTCA==; gsscgib-w-mvideo=X6oXdH6KwFZwSlkZkVqPzmI6dY3n7+Du6BgfVRsrCKoRk8eb30VqDqfnzzVac6DNvn6mPxQr+DvM4T+70MAxeNXkXWG9EesEYtO8i0fByb+B3Q96oVktPeYgmeiUHyB3/QaIlDXv+f9C6KBu5eKgFg9AY2w+hc+ukGR5/Isv3MUfKFupCE+g4lQ/Ej0rEKDiKtEYZ1IHRu8FM56WAgwCt/t93bIBUhEVM4ocvKolA+P8Mtdp9doYjS3vS5MTCA==; fgsscgib-w-mvideo=fRpQ4478f3d751b0687f99552f72e9449d235691; fgsscgib-w-mvideo=fRpQ4478f3d751b0687f99552f72e9449d235691; cfidsgib-w-mvideo=nRp0VRYWtINdwrQdgEEl2TWKe1wFdfcLKScyUzxM6Vx4e9f5pvy2RDFVWjKCDdNBvSU82fnwRi6+8IRPGk4xIBzZFb+TbFaPS2YqJeB3M31+i+oQzRs2eMjKV2MBh7WBAJGp/0QI0/cNF9W0imqpnlNdKPVM/PPzHXO+; CACHE_INDICATOR=false; _sp_id.d61c=bdfb95a0-c7e7-4610-9ab7-d5e437bbb0f0.1665420454.2.1666894356.1665420991.1009bcb2-3501-445e-8dd2-fb4bf65d7ec7.a9da1137-60dd-4684-987f-f908954ecbc1.32b66620-5a65-4b45-9be1-b14ed714b538.1666894055772.44; _ga=GA1.2.1733869895.1665420454; tmr_detect=0%7C1666894361464; tmr_reqNum=449; MVID_ENVCLOUD=prod1; _ga_CFMZTSS5FM=GS1.1.1666894055.2.1.1666894396.0.0.0; _ga_BNX5WPP3YK=GS1.1.1666894055.2.1.1666894396.10.0.0',
        'referer': 'https://www.mvideo.ru/komputernye-komplektuushhie-5427/videokarty-5429',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '98c1bdf0557a410aa25b0a36ddee5438-b9f7367306f0f87a-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36',
        'x-set-application-id': 'c7a81d13-a3ba-4caa-9758-cf0f60903f2d',
    }

    params = {
        'categoryId': '5429',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    #print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    print(products_ids)


def main():
    get_data()


if __name__ == '__main__':
    main()