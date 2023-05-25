import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from dash.dependencies import Input, Output, State
import time
import plotly.graph_objs as go
from selenium.common.exceptions import NoSuchElementException



def lay_du_lieu_giay():
    # Khởi tạo trình điều khiển Chrome với WebDriver Manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Trang web cần lấy dữ liệu
    url = 'https://ananas.vn/product-list/?gender=men'

    # Mở trang web bằng Selenium
    driver.get(url)

    # Kéo hết trang
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Đợi 2 giây để trang tải
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Lấy dữ liệu từ trang đã kéo hết
    elements = driver.find_elements(By.CSS_SELECTOR, 'div.thumbnail')

    data = []
    for element in elements:
        ten_thiet_bi_element = element.find_element(By.CSS_SELECTOR, 'div.caption h3.name a')
        gia_element = element.find_element(By.CSS_SELECTOR, 'div.caption h3.price')
        gia_hien_tai = gia_element.text
        tinh_trang = ''

        try:
            gia_cu_element = gia_element.find_element(By.CSS_SELECTOR, 'span.price-real')
            gia_cu = gia_cu_element.text
            tinh_trang = 'Đang khuyến mãi'

        except NoSuchElementException:
            gia_cu = ''
        ten_thiet_bi = ten_thiet_bi_element.text



        data.append({'Tên': ten_thiet_bi, 'Giá hiện tại': gia_hien_tai, 'Giá cũ': gia_cu,'Tình trạng': tinh_trang})

    # Đóng trình duyệt
    driver.quit()

    # Tạo DataFrame từ dữ liệu lấy được
    data_tu_lanh = pd.DataFrame(data)
    return data_tu_lanh
def lay_du_lieu_giay_nu():
    # Khởi tạo trình điều khiển Chrome với WebDriver Manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Trang web cần lấy dữ liệu
    url = 'https://ananas.vn/product-list/?gender=women'

    # Mở trang web bằng Selenium
    driver.get(url)

    # Kéo hết trang
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Đợi 2 giây để trang tải
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Lấy dữ liệu từ trang đã kéo hết
    elements = driver.find_elements(By.CSS_SELECTOR, 'div.thumbnail')

    data = []
    for element in elements:
        ten_thiet_bi_element = element.find_element(By.CSS_SELECTOR, 'div.caption h3.name a')
        gia_element = element.find_element(By.CSS_SELECTOR, 'div.caption h3.price')
        gia_hien_tai = gia_element.text
        tinh_trang = ''

        try:
            gia_cu_element = gia_element.find_element(By.CSS_SELECTOR, 'span.price-real')
            gia_cu = gia_cu_element.text
            tinh_trang = 'Đang khuyến mãi'

        except NoSuchElementException:
            gia_cu = ''
        ten_thiet_bi = ten_thiet_bi_element.text



        data.append({'Tên': ten_thiet_bi, 'Giá hiện tại': gia_hien_tai, 'Giá cũ': gia_cu,'Tình trạng': tinh_trang})

    # Đóng trình duyệt
    driver.quit()

    # Tạo DataFrame từ dữ liệu lấy được
    data_tu_lanh = pd.DataFrame(data)
    return data_tu_lanh





def lay_du_lieu_giay_bitit():
    # Khởi tạo trình điều khiển Chrome với WebDriver Manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Trang web cần lấy dữ liệu
    url = 'https://bitis.com.vn/collections/nam?'

    # Mở trang web bằng Selenium
    driver.get(url)

    # Kéo hết trang
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) # Đợi 2 giây để trang tải
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Lấy dữ liệu từ trang đã kéo hết
    ten_thiet_bi_elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-box-info div.product-box-title h4 a')
    gia_elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-box-info div.product-box-price div.main-price, div.product-box-info div.product-box-price span.main-price-inner')

    ten_thiet_bi = [element.text for element in ten_thiet_bi_elements]
    gia = []
    for gia_element in gia_elements:
        if gia_element.tag_name == 'div':
            gia.append(gia_element.text)
        elif gia_element.tag_name == 'span':
            gia.append(gia_element.get_attribute('innerHTML'))

    # Đóng trình duyệt
    driver.quit()

    # Tạo DataFrame từ dữ liệu lấy được
    data_tu_lanh = pd.DataFrame({'Tên': ten_thiet_bi, 'Giá hiện tại': gia})

    return data_tu_lanh
def lay_du_lieu_giay_bitit_nu():
    # Khởi tạo trình điều khiển Chrome với WebDriver Manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Trang web cần lấy dữ liệu
    url = 'https://bitis.com.vn/collections/nu'

    # Mở trang web bằng Selenium
    driver.get(url)

    # Kéo hết trang
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) # Đợi 2 giây để trang tải
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Lấy dữ liệu từ trang đã kéo hết
    ten_thiet_bi_elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-box-info div.product-box-title h4 a')
    gia_elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-box-info div.product-box-price div.main-price, div.product-box-info div.product-box-price span.main-price-inner')

    ten_thiet_bi = [element.text for element in ten_thiet_bi_elements]
    gia = []
    for gia_element in gia_elements:
        if gia_element.tag_name == 'div':
            gia.append(gia_element.text)
        elif gia_element.tag_name == 'span':
            gia.append(gia_element.get_attribute('innerHTML'))

    # Đóng trình duyệt
    driver.quit()

    # Tạo DataFrame từ dữ liệu lấy được
    data_tu_lanh = pd.DataFrame({'Tên': ten_thiet_bi, 'Giá hiện tại': gia})

    return data_tu_lanh



# Tạo ứng dụng Dash
app = dash.Dash(__name__)

# Định nghĩa giao diện người dùng (UI)
app.layout = html.Div(
    children=[
        html.H1('Kết quả lấy dữ liệu'),
        dcc.Dropdown(
            id='loai_thiet_bi',
            options=[
                {'label': 'Chọn loại thiết bị', 'value': 'all'},
                {'label': 'Giày nam', 'value': 'giay'},
                {'label': 'Giày nữ', 'value': 'giaynu'},

            ],
            value='all'
        ),
        html.Div(id='thong_tin_thiet_bi')
    ]
)

# Định nghĩa phần điều khiển (callback) để xử lý sự kiện chọn của người dùng
@app.callback(
    Output('thong_tin_thiet_bi', 'children'),
    Input('loai_thiet_bi', 'value')
)
def update_thong_tin_thiet_bi(loai_thiet_bi):
    if loai_thiet_bi == 'giay':
        data_tu_lanh = lay_du_lieu_giay_bitit()
        data_ananas = lay_du_lieu_giay()
        
        # Tạo tên file Excel dựa trên thời gian hiện tại
        excel_file_name = f'data_giaynam_ananas.xlsx'
        excel_file_name1 = f'data_giaynam_biti.xlsx'

        


                # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        data_tu_lanh['Giá hiện tại'] = data_tu_lanh['Giá hiện tại'].apply(lambda x: float(str(x).replace('₫', '').replace(',', '').replace('.', '').split()[0]))
        data_ananas['Giá hiện tại'] = data_ananas['Giá hiện tại'].apply(lambda x: float(str(x).replace(' VND', '').replace(',', '').replace('.', '').split()[0]))

        # Sắp xếp dữ liệu theo giá tăng dần
        data_tu_lanh = data_tu_lanh.sort_values('Giá hiện tại')
        data_ananas = data_ananas.sort_values('Giá hiện tại')

        # Lưu dữ liệu vào file Excel
        data_tu_lanh.to_excel(excel_file_name1, index=False, sheet_name='biti')
        data_ananas.to_excel(excel_file_name, index=False, sheet_name='Ananas')

        



        # Chọn 10 sản phẩm có giá cao nhất từ mỗi trang web
        top_10_giay_bitit = data_tu_lanh.nlargest(10, 'Giá hiện tại')
        top_10_giay_ananas = data_ananas.nlargest(10, 'Giá hiện tại')

        top_10_giay_bitit = data_tu_lanh.nlargest(10, 'Giá hiện tại')
        top_10_giay_ananas = data_ananas.nlargest(10, 'Giá hiện tại')

        top_10_tu_lanh = data_tu_lanh.head(10)
        top_10_ananas = data_ananas.head(10)

        return [
            html.H3('Dữ liệu từ Bitis'),
            html.Table(
                children=[
                    html.Thead(
                        html.Tr(
                            children=[
                                html.Th(column_name, style={'background-color': 'grey', 'color': 'white'}) for column_name in data_tu_lanh.columns
                            ]
                        )
                    ),
                    html.Tbody(
                        [
                            html.Tr(
                                children=[
                                    html.Td(data_row[column_name]) for column_name in data_tu_lanh.columns
                                ]
                            ) for _, data_row in data_tu_lanh.iterrows()
                        ]
                    )
                ]
            ),
            html.H3('Dữ liệu từ Ananas'),
            html.Table(
                children=[
                    html.Thead(
                        html.Tr(
                            children=[
                                html.Th(column_name, style={'background-color': 'grey', 'color': 'white'}) for column_name in data_ananas.columns
                            ]
                        )
                    ),
                    html.Tbody(
                        [
                            html.Tr(
                                children=[
                                    html.Td(data_row[column_name]) for column_name in data_ananas.columns
                                ]
                            ) for _, data_row in data_ananas.iterrows()
                        ]
                    )
                ]
            ),
            html.H3('Đồ thị top 10 giày giá cao nhất'),
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=top_10_giay_bitit['Tên'],
                            y=top_10_giay_bitit['Giá hiện tại'],
                            name='Bitis'
                        ),
                        go.Bar(
                            x=top_10_giay_ananas['Tên'],
                            y=top_10_giay_ananas['Giá hiện tại'],
                            name='Ananas'
                        )
                    ],
                    layout=go.Layout(
                        title='Top 10 giày giá cao nhất',
                        xaxis={'title': 'Tên sản phẩm'},
                        yaxis={'title': 'Giá (VND)'},
                        barmode='group'
                    )
                )
            ),
            html.H3('Đồ thị top 10 giày giá thấp nhất'),
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=top_10_tu_lanh['Tên'],
                            y=top_10_tu_lanh['Giá hiện tại'],
                            name='Bitis'
                        ),
                        go.Bar(
                            x=top_10_ananas['Tên'],
                            y=top_10_ananas['Giá hiện tại'],
                            name='Ananas'
                        )
                    ],
                    layout=go.Layout(
                        title='Top 10 giày giá cao nhất',
                        xaxis={'title': 'Tên sản phẩm'},
                        yaxis={'title': 'Giá (VND)'},
                        barmode='group'
                    )
                )
            )
        ]
    elif loai_thiet_bi == 'giaynu':
        data_tu_lanh = lay_du_lieu_giay_bitit_nu()
        data_ananas = lay_du_lieu_giay_nu()
        
        # Tạo tên file Excel dựa trên thời gian hiện tại
        excel_file_name = f'data_giaynam_ananas.xlsx'
        excel_file_name1 = f'data_giaynam_biti.xlsx'

        


                # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        # Chuyển đổi kiểu dữ liệu của cột 'Giá' sang dạng số
        data_tu_lanh['Giá hiện tại'] = data_tu_lanh['Giá hiện tại'].apply(lambda x: float(str(x).replace('₫', '').replace(',', '').replace('.', '').split()[0]))
        data_ananas['Giá hiện tại'] = data_ananas['Giá hiện tại'].apply(lambda x: float(str(x).replace(' VND', '').replace(',', '').replace('.', '').split()[0]))

        # Sắp xếp dữ liệu theo giá tăng dần
        data_tu_lanh = data_tu_lanh.sort_values('Giá hiện tại')
        data_ananas = data_ananas.sort_values('Giá hiện tại')

        # Lưu dữ liệu vào file Excel
        data_tu_lanh.to_excel(excel_file_name1, index=False, sheet_name='biti')
        data_ananas.to_excel(excel_file_name, index=False, sheet_name='Ananas')

        



        # Chọn 10 sản phẩm có giá cao nhất từ mỗi trang web
        top_10_giay_bitit = data_tu_lanh.nlargest(10, 'Giá hiện tại')
        top_10_giay_ananas = data_ananas.nlargest(10, 'Giá hiện tại')

        top_10_giay_bitit = data_tu_lanh.nlargest(10, 'Giá hiện tại')
        top_10_giay_ananas = data_ananas.nlargest(10, 'Giá hiện tại')

        top_10_tu_lanh = data_tu_lanh.head(10)
        top_10_ananas = data_ananas.head(10)

        return [
            html.H3('Dữ liệu từ Bitis'),
            html.Table(
                children=[
                    html.Thead(
                        html.Tr(
                            children=[
                                html.Th(column_name, style={'background-color': 'grey', 'color': 'white'}) for column_name in data_tu_lanh.columns
                            ]
                        )
                    ),
                    html.Tbody(
                        [
                            html.Tr(
                                children=[
                                    html.Td(data_row[column_name]) for column_name in data_tu_lanh.columns
                                ]
                            ) for _, data_row in data_tu_lanh.iterrows()
                        ]
                    )
                ]
            ),
            html.H3('Dữ liệu từ Ananas'),
            html.Table(
                children=[
                    html.Thead(
                        html.Tr(
                            children=[
                                html.Th(column_name, style={'background-color': 'grey', 'color': 'white'}) for column_name in data_ananas.columns
                            ]
                        )
                    ),
                    html.Tbody(
                        [
                            html.Tr(
                                children=[
                                    html.Td(data_row[column_name]) for column_name in data_ananas.columns
                                ]
                            ) for _, data_row in data_ananas.iterrows()
                        ]
                    )
                ]
            ),
            html.H3('Đồ thị top 10 giày nữ giá cao nhất'),
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=top_10_giay_bitit['Tên'],
                            y=top_10_giay_bitit['Giá hiện tại'],
                            name='Bitis'
                        ),
                        go.Bar(
                            x=top_10_giay_ananas['Tên'],
                            y=top_10_giay_ananas['Giá hiện tại'],
                            name='Ananas'
                        )
                    ],
                    layout=go.Layout(
                        title='Top 10 giày giá cao nhất',
                        xaxis={'title': 'Tên sản phẩm'},
                        yaxis={'title': 'Giá (VND)'},
                        barmode='group'
                    )
                )
            ),
            html.H3('Đồ thị top 10 giày nữ giá thấp nhất'),
            dcc.Graph(
                figure=go.Figure(
                    data=[
                        go.Bar(
                            x=top_10_tu_lanh['Tên'],
                            y=top_10_tu_lanh['Giá hiện tại'],
                            name='Bitis'
                        ),
                        go.Bar(
                            x=top_10_ananas['Tên'],
                            y=top_10_ananas['Giá hiện tại'],
                            name='Ananas'
                        )
                    ],
                    layout=go.Layout(
                        title='Top 10 giày giá cao nhất',
                        xaxis={'title': 'Tên sản phẩm'},
                        yaxis={'title': 'Giá (VND)'},
                        barmode='group'
                    )
                )
            )
        ]
    else:
        return html.P('Vui lòng chọn loại thiết bị')
    


# Định nghĩa callback để xử lý sự kiện click nút lưu Excel
@app.callback(
    Output('save-excel-giay-bitit', 'n_clicks'),
    Input('save-excel-giay-bitit', 'n_clicks'),
    State('thong_tin_thiet_bi', 'children')
)
def save_excel(n_clicks, table_div):
    if n_clicks > 0:
        data_tu_lanh = lay_du_lieu_giay_bitit()
        data_tu_lanh.to_excel('thong_tin_giay_bitit.xlsx', index=False)
        return n_clicks
    else:
        return n_clicks

if __name__ == '__main__':
    app.run_server(debug=True)
