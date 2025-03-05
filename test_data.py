# test_data.py
import random
from app import db, app
from models import User, HealthRecord, Department, Announcement
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

import pytz 
# テストデータの生成
departments = ['hr', 'it', 'sales', 'marketing', 'finance']
names = [
    "豊嶋 貴美", "木村 雅英", "白澤 勝士", "越智 結衣", "川村 文哉", "佐々木 泰子", "吉田 萌", "原田 一彦",
    "徳原 隆嗣", "中谷 大祐", "森崎 勝久", "松本 睦", "村田 圭一", "橋本 誠司", "小島 政信", "本間 祐",
    "青柳 一恵", "山本 一郎", "久保田 邦恵", "坂本 昌也", "新見 健一", "三浦 秀平", "岸 正幸", "益田 剛",
    "大野 翔太", "鈴木 和裕", "結城 満", "松浦 智子", "藤井 健太郎", "伊藤 弥生", "大倉 幸生", "高橋 靖章",
    "桜井 祥江", "山下 健二", "小野 達也", "藤井 勇人", "中川 正也", "長谷川 剛", "遠藤 真実", "佐藤 大地",
    "小池 愛子", "今西 千里", "山田 勝弘", "磯谷 夏菜", "大野 正紘", "木下 雄一郎", "山内 順子", "勝浦 大作",
    "川邊 裕子", "渡辺 春美", "安田 加奈", "渡会 智子", "山田 和男", "玉木 沙織", "馬目 裕貴", "山下 晴之",
    "佐藤 直人", "武部 健太郎", "角田 啓一", "佐藤 聡美", "荒井 尚平", "村松 健一", "山田 信夫", "鈴木 優一",
    "井村 哲", "大江 竜太", "吉田 雄平", "竹崎 郁子", "佐々木 克也", "長谷川 栞", "本宮 清", "横山 浩嗣",
    "菱沼 幸恵", "大瀧 勉", "三浦 朱里", "金 陽太", "小島 哲也", "小早川 真理子", "森重 光子", "久保 美和子",
    "吉村 源", "土岐 洋子", "山岸 文", "上田 房江", "萬代 宏之", "池下 耕治", "百田 隆志", "中村 弘",
    "村上 はるか", "小山 久美", "下條 敏", "上原 達也", "玉田 智也", "田中 亮", "松本 朗", "高澤 由美子",
    "成田 晴子", "宮下 麻衣", "薬師寺 真一郎", "荒井 麻美", "鈴木 友美", "糟谷 あい子", "石森 愛", "三原 有香",
    "清水 満", "谷 千絵", "加藤 涼", "堀 豊", "石谷 佳那子", "北田 真美", "石山 直樹", "具志 賢一",
    "臼井 秀人", "太田 典子", "水谷 洸太", "藤野 朋子", "田中 鏡子", "佐藤 朗", "槙 真実", "鈴木 彩子",
    "横川 まどか", "伊藤 由記", "高田 智香", "大高 勤", "長谷川 慧", "丸山 嘉一", "原田 郁実", "島野 隆司",
    "荒木 大輔", "竹澤 旭", "平井 仁美", "北村 正人", "石井 和彦", "市原 博司", "半田 薫", "児玉 みく",
    "石塚 卓矢", "中山 裕司", "中上 香", "近藤 卓", "高田 咲子", "武井 正行", "北村 隆広", "若林 航",
    "林 尚", "石毛 桂子", "鈴木 邦明", "牧村 佑介", "蒲地 圭祐", "高瀬 祐太", "坂元 政明", "佐藤 幸弘",
    "青柳 伸哉", "中島 皓平", "北川 未来", "石谷 啓一郎", "三宅 健太郎", "郡司 憲", "川本 直行", "久保園 かほり",
    "竹田 明義", "新倉 晃弘", "前田 由香里", "塚田 優太", "寿 豊", "市川 正人", "千々和 真樹", "中村 拓也",
    "馬場 ゆうこ", "内山 哲志", "橋本 麻衣子", "新海 達彦", "田中 良徳", "岩田 みゆき", "矢野 幸雄", "藤井 雄一郎",
    "駒田 克佳", "加藤 源", "及川 敏浩", "星 美彩子", "吉村 雅昭", "石塚 洋", "松田 あやか", "渡辺 竜治",
    "斉木 和司", "柳瀬 由記子", "伊藤 育夫", "三井 進", "吉中 奈美", "大石 瞳", "神田 実", "橋本 寛",
    "安達 拓史", "高村 里美", "町田 正和", "守田 二郎", "加茂 昌弘", "荒川 秀男", "人見 貴洋", "水越 天"
]

# 社員データの登録
def create_test_data():
    # 日本のタイムゾーンを設定
    tz = pytz.timezone('Asia/Tokyo')
    
    with open('employee_data.txt', 'w', encoding='utf-8') as f:
        for i in range(200):
            employee_number = f"EMP{i + 1:03}"
            name = names[i]
            department = random.choice(departments)
            phone = f"090-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
            email = f"{name.replace(' ', '_').lower()}@example.com"
            password = generate_password_hash("password123")
            
            # 管理者権限の設定(IDが20未満の社員は管理者権限を持つ)
            if i <= 20:
                is_admin = True 
            else:
                is_admin = False
            
            user = User(
                password_hash=password,
                employee_number=employee_number,
                department=department,
                name=name,
                phone=phone,
                email=email,
                is_admin=is_admin
            )
            
            db.session.add(user)
            db.session.commit()
            
            # 健康記録の登録(30日分のデータを生成)
            for day in range(30):
                record_date = datetime.now(tz) - timedelta(days=day)  # タイムゾーンを考慮して日付を生成
                Healthflag=0
                if day % 70 == 0 and 1 == random.randint(1, 10):
                    temperature = round(random.uniform(37.0, 38.5), 1)
                    Healthflag=1
                else:
                    temperature = round(random.uniform(36.0, 36.9), 1)
                
                if day % 70 == 0 and 1== random.randint(1, 10):
                    num_parts = random.randint(1, len(["頭", "右腕", "右足", "腹", "左足", "胸", "左腕"]))
                    selected_parts = random.sample(["頭", "右腕", "右足", "腹", "左足", "胸", "左腕"], num_parts)
                    Healthflag=1
                else:
                    selected_parts = []
                
                health_record = HealthRecord(
                    user_id=user.id,
                    temperature=temperature,
                    throat="normal",
                    fever="normal",
                    cough="no",
                    selected_parts=selected_parts,
                    date=record_date,
                    flag=Healthflag
                )
                db.session.add(health_record)

            db.session.commit()
            
            f.write(f"社員番号: {employee_number}, 名前: {name}, 部署: {department}, "
                    f"電話: {phone}, メール: {email}\n")
            print(f"社員 {i + 1} / {len(names)}: {employee_number}: {name}が登録されました。")
        
        print("全ての社員データの登録が完了しました。")


# 初期データを挿入する関数
def insert_initial_departments():
    departments = [
        {'name': '人事部', 'abbreviation': 'hr'},
        {'name': 'IT部門', 'abbreviation': 'it'},
        {'name': '営業部', 'abbreviation': 'sales'},
        {'name': 'マーケティング部', 'abbreviation': 'marketing'},
        {'name': '財務部', 'abbreviation': 'finance'}
    ]
    
    for dept in departments:
        # 新しい部門を作成
        new_department = Department(name=dept['name'], abbreviation=dept['abbreviation'])
        db.session.add(new_department)

    db.session.commit()
    print("全ての部門データの登録が完了しました。")  # 部門登録完了メッセージ

def creat_announcement_data():
    # 日本のタイムゾーンを設定
    tz = pytz.timezone('Asia/Tokyo')

    title = [
        "年末年始休業のお知らせ",
        "安全対策の呼びかけ",
        "設備点検に伴うライン停止のご案内"
    ]
    content = [
            """<p>日頃より当社の業務にご協力いただきありがとうございます。<br>
            年末年始の休業日についてお知らせします。<br>
            【休業期間】12月29日（金）～1月4日（木）<br>
            休業期間中は緊急対応を除き、すべての業務を停止します。
            <br>新年は1月5日（金）より通常営業を再開いたします。
            <br>どうぞよろしくお願いいたします。</p>""",
            
           """<p>いつもお疲れ様です。</p>
           <p>安全第一で作業を進めていただきありがとうございます。😊</p>
           <p>最近、工場内での軽微なケガの報告が増えています。<br>今週は安全確認週間とし、以下のポイントを再度確認してください：</p>
           <ol>
               <li>作業開始前に機器の点検を行う</li>
               <li>作業エリアの整理整頓を徹底する</li>
               <li><strong><span style="color: #e03e2d; font-size: 18pt;">安全靴</span></strong>、<strong><span style="color: #e03e2d; font-size: 18pt;">ヘルメット</span></strong>の着用を忘れない</li>
           </ol>
           <p>皆さんの協力をお願いします。</p>""",

            """<p>来週の11月30日（木）に、Aラインの定期設備点検を行います。
            <br>作業スケジュールに影響が出る可能性がありますので、該当ラインでの作業担当の方は事前に予定を調整してください。
            <br>【停止時間帯】<span style="color: #e03e2d; font-size: 18pt;">午前10時～午後4時</span><br>
            ご不明点は、製造部までお問い合わせください。</p>
            <p>製造部連絡先：<a href="https://ja.wikipedia.org/wiki/%E3%83%81%E3%83%B3%E3%83%91%E3%83%B3%E3%82%B8%E3%83%BC" target="_blank" rel="noopener">
            https://www.hasegawako-.seizobu</a></p>"""
        ]

    for i in range(len(title)):
        record_date = datetime.now(tz) - timedelta(days=i * 5)
        existing_announcement = Announcement.query.filter_by(title=title[i]).first()
        if not existing_announcement:
            announcement = Announcement(
                title=title[i],
                content=content[i],
                date=record_date,  # 修正
            )
            db.session.add(announcement)

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():  # アプリケーションコンテキストを設定
        insert_initial_departments()  # 初期データの部門登録
        create_test_data()  # テストデータの社員登録
        creat_announcement_data() # テストデータのお知らせ登録
    print("テストデータの登録が完了しました。")