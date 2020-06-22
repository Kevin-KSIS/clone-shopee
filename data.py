
## Có thể thay đổi cho phù hợp
WEIGHT_DEFAULT = 500
HEIGHT_DEFAULT = 0
WIDTH_DEFAULT = 0
LENGTH_DEFAULT = 0
DELIVERY_DEFAULT = {
    'ghn': "Mở",
    'jnt': "Tắt",
    'ninja': "Tắt",
    'bestexpress': "Tắt",
    'viettelpost': "Tắt",
    'ghtk': "Tắt",
    'vnpost': "Tắt"
}

PRICE_BEFORE_DISCOUNT = True # Lấy giá trước khi giảm giá?

PRE_ORDER = '' # mặc định là không đặt hàng trước

MODIFY = {
    'PREFIX_NAME': '[NEW] ', # thêm trước tiêu đề
    'SUFFIX_NAME': '',   # thêm sau tiêu đề
    'PREFIX_DESCRIPTION':   # thêm trước mô tả
        '''Tiêu chí của shop là luôn bán sản phẩm chất lượng và mang đến trải nghiệm tốt nhất cho khách hàng
---''',
    'SUFFIX_DESCRIPTION':   # Thêm sau mô tả
        '''--- 
Facebook: https://facebook.com/cua.hang.sago
Số điện thoại: 037 000 0000
'''
}

EXPORT_FILENAME = 'export_shop.csv' # tên tập tin kết quả


## KHÔNG THAY ĐỔI
SHEET_DEFAULT = 'Bản đăng tải'

FAKE_HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://shopee.vn/',
    'X-Shopee-Language': 'vi',
    'X-Requested-With': 'XMLHttpRequest',
    'X-API-SOURCE': 'pc'
}

class COLUMN_DEFAULT(object):
    nganh_hang = 'ps_category'
    ten_san_pham = 'ps_product_name'
    mo_ta = 'ps_product_description'
    sku_san_pham = 'ps_sku_parent_short'
    ma_san_pham = 'et_title_variation_integration_no'
    ten_nhom_phan_loai_1 = 'et_title_variation_1'  # ex: size
    ten_phan_loai_nhom_1 = 'et_title_option_for_variation_1'  # ex: 40
    hinh_anh_phan_loai = 'et_title_image_per_variation'
    ten_nhom_phan_loai_2 = 'et_title_variation_2'  # ex: color
    ten_phan_loai_nhom_2 = 'et_title_option_for_variation_2'  # black
    gia = 'ps_price'
    kho = 'ps_stock'
    sku_phan_loai = 'ps_sku_short'
    anh_bia = 'ps_item_cover_image'
    hinh1 = 'ps_item_image_1'
    hinh2 = 'ps_item_image_2'
    hinh3 = 'ps_item_image_3'
    hinh4 = 'ps_item_image_4'
    hinh5 = 'ps_item_image_5'
    hinh6 = 'ps_item_image_6'
    hinh7 = 'ps_item_image_7'
    hinh8 = 'ps_item_image_8'
    can_nang = 'ps_weight'
    dai = 'ps_length'
    rong = 'ps_width'
    cao = 'ps_height'
    ghn = 'channel_id_50011'
    jnt = 'channel_id_50018'
    ninja = 'channel_id_50023'
    bestexpress = 'channel_id_50024'
    viettelpost = 'channel_id_50010'
    ghtk = 'channel_id_50012'
    vnpost = 'channel_id_50016'
    ps_product_pre_order_dts = 'ps_product_pre_order_dts'
# ---
